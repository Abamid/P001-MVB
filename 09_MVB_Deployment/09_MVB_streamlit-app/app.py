"""
MVB Meningitis Classifier — Clinical Decision Support Prototype
Project: P001-MVB
Stage: 09_MVB_Deployment
Model: Logistic Regression (LR_B), Feature Set B (Restricted)
Author: Abubakar Amidu
Programme: 3MTT DeepTech Cohort 2 — DS/ML Mentorship

IMPORTANT: This is a research prototype only. See the Model Card and
AI Risk Assessment (Stage 08) for full deployment constraints.
"""

import streamlit as st
import pandas as pd
import numpy as np
import pickle
import shap
import matplotlib.pyplot as plt
from datetime import datetime

# ============================================================
# Page config
# ============================================================
st.set_page_config(page_title="MVB Meningitis Classifier", layout="wide")

# ============================================================
# Load model, scaler, and SHAP explainer (fitted once on a
# representative background sample, not the full training set)
# ============================================================
@st.cache_resource
def load_artifacts():
    with open("../05_MVB_Model-Training/Models/MVB-05-lr-B.pkl", "rb") as f:
        model = pickle.load(f)
    with open("../05_MVB_Model-Training/Models/MVB-05-scaler-B.pkl", "rb") as f:
        scaler = pickle.load(f)
    df_b = pd.read_csv("../04_MVB_Feature-Engineering/MVB-04-results/MVB-04-feature-set-B-restricted.csv")
    feature_cols = [c for c in df_b.columns if c != "Diagnosis"]
    X_train_background = scaler.transform(df_b[feature_cols])
    # Use a representative sample rather than the full training set — reduces memory
    # footprint while producing equivalent explanations for a linear model
    background = shap.sample(X_train_background, 100, random_state=42)
    explainer = shap.LinearExplainer(model, background)
    return model, scaler, explainer, len(df_b)

model, scaler, explainer, n_training_records = load_artifacts()

FEATURE_COLS = ["Age", "Gender", "WBC_Count", "Protein_Level", "Glucose_Level",
                 "Hemoglobin", "WBC_Blood_Count", "Platelets", "CRP_Level"]

# Training data observed ranges (Stage 03 profiling) — used for Trigger 4 (out-of-distribution)
TRAINING_RANGES = {
    "Age": (0, 118),
    "WBC_Count": (2008, 24716),
    "Protein_Level": (2, 299),
    "Glucose_Level": (1, 148),
    "Hemoglobin": (1, 18),
    "WBC_Blood_Count": (4022, 19991),
    "Platelets": (100088, 399479),
    "CRP_Level": (0, 99),
}

# ============================================================
# Header and prototype banner
# ============================================================
st.title("MVB Meningitis Classifier")
st.caption("Explainable and Responsible AI for Differentiating Bacterial and Viral Meningitis")

st.warning(
    "⚠️ **RESEARCH PROTOTYPE — NOT FOR CLINICAL USE.** This tool has not undergone "
    "clinical validation, regulatory review, or certification. It must never be used "
    "for autonomous diagnosis or treatment decisions. See the Model Card (Stage 08) "
    "for full deployment constraints."
)

# ============================================================
# Model information (expandable)
# ============================================================
with st.expander("ℹ️ Model Information"):
    st.markdown(f"""
    **Model:** Logistic Regression (LR_B)
    **Version:** 1.0
    **Training Records:** {n_training_records}
    **Selected because:**
    - Highest Bacterial Recall (95.8%)
    - Avoided the `Pathogen_Present` proxy feature (Stage 06 decision)
    """)

# ============================================================
# Input form
# ============================================================
st.header("Patient Laboratory Values")

col1, col2, col3 = st.columns(3)
with col1:
    age = st.number_input("Age (years)", min_value=0, max_value=120, value=40)
    gender = st.selectbox("Gender", ["Female", "Male"])
    wbc_count = st.number_input("CSF WBC Count", min_value=0, value=8000)
with col2:
    protein_level = st.number_input("CSF Protein Level", min_value=0, value=50)
    glucose_level = st.number_input("CSF Glucose Level", min_value=0, value=60)
    hemoglobin = st.number_input("Hemoglobin (g/dL)", min_value=0.0, value=13.0, step=0.1)
with col3:
    wbc_blood = st.number_input("Blood WBC Count", min_value=0, value=9000)
    platelets = st.number_input("Platelets", min_value=0, value=200000)
    crp_level = st.number_input("CRP Level", min_value=0, value=20)

clinician_override = st.checkbox(
    "Clinician requests manual verification regardless of model output"
)
missing_or_invalid = False  # placeholder for real input validation against a live data source

submit = st.button("Generate Prediction", type="primary")

# ============================================================
# Confidence banding helper
# ============================================================
def confidence_band(confidence):
    if confidence >= 0.90:
        return "High"
    elif confidence >= 0.60:
        return "Moderate"
    else:
        return "Low"

# ============================================================
# Pre-Decision Verification Checkpoint — trigger logic
# ============================================================
def check_pdvc_triggers(input_values, confidence, shap_vals, feature_names,
                         clinician_override=False, missing_or_invalid=False):
    triggers = []

    # Trigger 1: moderate or low confidence
    if confidence < 0.60:
        triggers.append(("Low model confidence", f"Confidence {confidence:.1%} is below 60%. Prediction is inconclusive."))
    elif confidence < 0.90:
        triggers.append(("Moderate model confidence", f"Confidence {confidence:.1%} is between 60–90%."))

    # Trigger 2: conflicting SHAP evidence (both positive and negative contributions present, roughly balanced)
    positive_sum = sum(v for v in shap_vals if v > 0)
    negative_sum = sum(abs(v) for v in shap_vals if v < 0)
    if positive_sum > 0 and negative_sum > 0:
        ratio = min(positive_sum, negative_sum) / max(positive_sum, negative_sum)
        if ratio > 0.4:  # meaningful opposing evidence, not a one-sided case
            triggers.append(("Conflicting feature-level evidence",
                              "Multiple features point in opposing directions (toward both Bacterial and Viral)."))

    # Trigger 3: age outside well-characterized range
    if input_values["Age"] > 100:
        triggers.append(("Age outside well-characterized range", "Patient age exceeds 100 years."))

    # Trigger 4: out-of-distribution feature values
    for feat, (lo, hi) in TRAINING_RANGES.items():
        val = input_values[feat]
        if val < lo or val > hi:
            triggers.append((f"Out-of-distribution value: {feat}",
                              f"{feat}={val} falls outside the training data range [{lo}, {hi}]."))

    # Trigger 5: clinician-initiated escalation
    if clinician_override:
        triggers.append(("Clinician-requested verification", "The attending clinician requested manual review."))

    # Trigger 6: data quality validation failure
    if missing_or_invalid:
        triggers.append(("Data quality validation failure", "One or more required values are missing or invalid."))

    return triggers

# ============================================================
# Prediction and explanation
# ============================================================
if submit:
    input_dict = {
        "Age": age, "Gender": 1 if gender == "Male" else 0,
        "WBC_Count": wbc_count, "Protein_Level": protein_level, "Glucose_Level": glucose_level,
        "Hemoglobin": hemoglobin, "WBC_Blood_Count": wbc_blood, "Platelets": platelets, "CRP_Level": crp_level,
    }
    X_input = pd.DataFrame([input_dict])[FEATURE_COLS]
    X_input_scaled = scaler.transform(X_input)

    proba_bacterial = model.predict_proba(X_input_scaled)[0][1]
    proba_viral = 1 - proba_bacterial
    prediction = model.predict(X_input_scaled)[0]
    predicted_label = "Bacterial" if prediction == 1 else "Viral"
    confidence = max(proba_bacterial, proba_viral)
    band = confidence_band(confidence)

    st.header("AI Decision Support Output")
    col_a, col_b, col_c = st.columns(3)
    with col_a:
        st.metric("Model Prediction", predicted_label)
    with col_b:
        st.metric("Model Confidence", f"{confidence:.1%}")
    with col_c:
        st.metric("Confidence Band", band)

    st.write(f"**Probability (Bacterial):** {proba_bacterial:.1%}  |  **Probability (Viral):** {proba_viral:.1%}")

    st.info(
        "ℹ️ This prediction is intended to support — not replace — clinical judgement. "
        "All treatment decisions remain the responsibility of the attending clinician."
    )

    # Explain this specific prediction using the pre-fitted explainer
    shap_values = explainer(X_input_scaled)

    st.subheader("Explanation")
    plt.figure(figsize=(8, 5))
    shap.plots.waterfall(shap_values[0], show=False)
    st.pyplot(plt.gcf())
    plt.close()

    # Simple ranked contribution table, for non-technical users
    contrib_df = pd.DataFrame({
        "Feature": FEATURE_COLS,
        "SHAP Contribution": shap_values.values[0]
    }).sort_values("SHAP Contribution", key=abs, ascending=False)
    st.dataframe(contrib_df.style.format({"SHAP Contribution": "{:+.3f}"}), use_container_width=True)

    # Run Pre-Decision Verification Checkpoint
    triggers = check_pdvc_triggers(
        input_dict, confidence, shap_values.values[0], FEATURE_COLS,
        clinician_override, missing_or_invalid
    )

    st.header("Pre-Decision Verification Checkpoint")
    if triggers:
        st.error(f"⚠️ **VERIFICATION REQUIRED** — {len(triggers)} trigger(s) activated. "
                  "This prediction must NOT influence any clinical decision without clinician review.")
        for i, (name, reason) in enumerate(triggers, start=1):
            st.write(f"**Trigger {i}: {name}**")
            st.write(reason)
        st.info(
            "Recommended action: review additional clinical evidence (patient history, physical "
            "examination, repeat laboratory investigations, CSF culture, or imaging) before considering "
            "this prediction. Record your final clinical judgement below."
        )
    else:
        st.success("✅ No verification triggers activated. Clinician review is still required before any clinical action — this model does not make autonomous decisions.")

    # Audit log entry (per PDVC framework — Stage 08)
    st.subheader("Audit Log Entry")
    log_entry = {
        "Timestamp": datetime.now().isoformat(),
        "Model_Version": "LR_B v1.0",
        "Prediction": predicted_label,
        "Prediction_Probability_Bacterial": round(proba_bacterial, 4),
        "Confidence": round(confidence, 4),
        "Confidence_Band": band,
        "PDVC_Triggers": [f"Trigger {i}: {t[0]}" for i, t in enumerate(triggers, start=1)] if triggers else "None",
    }
    st.json(log_entry)
    st.caption(
        "In a full deployment, this entry would be automatically recorded, together with the "
        "clinician's final decision, per the audit requirements in the AI Risk Assessment (Stage 08)."
    )

# ============================================================
# Footer — governance references
# ============================================================
st.markdown("---")
st.caption(
    "This tool implements the Pre-Decision Verification Checkpoint framework defined in "
    "MVB-08-RAI-Verification-Checkpoint.md. See also MVB-08-RAI-Model-Card.md and "
    "MVB-08-RAI-AI-Risk-Assessment.md for full governance documentation."
)
