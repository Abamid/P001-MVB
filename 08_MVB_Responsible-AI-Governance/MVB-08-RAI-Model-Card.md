Project Code: P001-MVB
Stage: 08_MVB_Responsible-AI-Governance
Document Version: v1.0
Model Version: v1.0
Author: Abubakar Amidu
Programme: 3MTT DeepTech Cohort 2 — DS/ML Mentorship
Last Updated: 27 July 2026

MVB-08 — Model Card

Project: P001-MVB — Explainable and Responsible AI for Differentiating Bacterial and Viral Meningitis: A Clinical Decision Support System

Document History

Version| Date| Author| Description
v1.0| 27 Jul 2026| Abubakar Amidu| Initial Model Card

Model Overview

Model name: MVB Meningitis Classifier (LR_B)

Model version: v1.0

Model type: Logistic Regression (Binary Classifier)

Task: Differentiate Bacterial from Viral meningitis using cerebrospinal fluid (CSF) and blood laboratory values.

Feature set: Restricted (9 features)

- Age
- Gender
- WBC_Count
- Protein_Level
- Glucose_Level
- Hemoglobin
- WBC_Blood_Count
- Platelets
- CRP_Level

Positive class: Bacterial (1)

Negative class: Viral (0)

Selected in: Stage 06 based on the highest Bacterial Recall (0.958) while deliberately excluding the near-proxy Pathogen_Present feature to strengthen Responsible AI and generalisability.

Intended Use

Intended Purpose

The MVB Meningitis Classifier is designed as a clinical decision-support aid to assist clinicians in differentiating bacterial from viral meningitis using CSF and blood laboratory measurements. It is intended to complement—not replace—clinical assessment, patient history, physical examination, and confirmatory diagnostic investigations.

Intended Users

- Physicians
- Neurologists
- Infectious disease specialists
- Emergency physicians
- Other qualified healthcare professionals capable of interpreting laboratory findings and exercising independent clinical judgement.

Intended Setting

A research prototype and educational demonstration delivered through the Stage 09 Streamlit application to illustrate how Explainable AI and Responsible AI governance can be integrated into AI-assisted clinical decision support.

Deployment Statement

This model is intended solely for research and educational demonstration. It has not undergone prospective clinical validation, regulatory review, external validation, or certification required for deployment within real healthcare environments.

Explicitly Prohibited Uses

The model must not be used for:

- Autonomous diagnosis or treatment decisions.
- Deployment on real patient data without independent clinical validation.
- Replacement of confirmatory diagnostic investigations (e.g., lumbar puncture, CSF culture, PCR testing) where clinically indicated.
- Use in healthcare settings or patient populations not represented in the training data without additional validation.
- Overriding clinician judgement, particularly when the Pre-Decision Verification Checkpoint has been triggered.
- Screening, triage, or emergency treatment decisions without qualified clinician oversight.

Training Data

Dataset Source

Kaggle — Meningitis Classification dataset (ChanTest)

Original Dataset Size

1,200 observations

Final Dataset After Stage 02

1,133 observations

- Bacterial: 595 (52.5%)
- Viral: 538 (47.5%)

Data Quality Assessment

Throughout this project the dataset is characterised as clinically-inspired but not clinically-calibrated.

Evidence supporting this assessment includes:

- CSF WBC_Count values substantially exceed those typically observed in real clinical datasets.
- Several individual biomarkers (Hemoglobin, WBC_Blood_Count, and CRP_Level) achieve exceptionally high single-feature discrimination (approximately 86–94%), indicating unusually strong class separation.
- Pathogen_Present matches the diagnosis label in approximately 94% of observations, making it a near-proxy variable.
- Collectively, these characteristics are consistent with either a synthetically generated dataset or a heavily curated educational dataset, although this cannot be confirmed from the available documentation.

Implication

Performance metrics reported in this Model Card describe performance only on this dataset and should not be interpreted as estimates of real-world clinical performance.

Performance

The final model was evaluated using a stratified 20% hold-out test set (n = 227) following the methodology established in Stages 05 and 06.

Metric| Value
Accuracy| 0.934
Bacterial Recall| 0.958
Bacterial Precision| 0.919
False Negatives| 5
False Positives| 10

The model was selected by prioritising Bacterial Recall, reflecting the project's clinical objective of minimising missed bacterial cases rather than maximising overall accuracy or ROC-AUC.

Comprehensive comparisons against Logistic Regression (Feature Set A), Random Forest, and XGBoost are documented in Stage 06.

Explainability

Explainability analysis was performed during Stage 07 using SHAP LinearExplainer.

Because Logistic Regression is a linear model, SHAP generates exact feature attributions that correspond directly to the model coefficients rather than relying on approximation methods required for many black-box algorithms.

Global explainability analysis identified the model's primary clinical drivers as:

- Hemoglobin
- CRP_Level
- WBC_Count
- WBC_Blood_Count
- Platelets
- Glucose_Level

Each contributes in the clinically expected direction when distinguishing bacterial from viral meningitis.

Protein_Level contributes very little independent information because of multicollinearity with WBC_Count, demonstrating that the model appropriately accounts for redundancy between correlated biomarkers instead of treating them as independent evidence.

Known Limitations

1. The training dataset has not been confirmed to originate from routine clinical practice; therefore, reported performance may not generalise to real patients.

2. Forty-three observations with Age greater than 100 years were retained because they belonged primarily to the excluded "Unknown" diagnosis class and could not be confidently classified as erroneous.

3. The five false-negative bacterial cases exhibited conflicting laboratory evidence across multiple biomarkers, demonstrating situations in which model predictions alone should not be relied upon.

4. External validation using an independent clinical dataset has not been performed.

5. Hyperparameter optimisation and cross-validation were intentionally omitted. Reported performance reflects default hyperparameters evaluated on a single train-test split.

6. The model has only been evaluated retrospectively and has not yet been prospectively evaluated within a live clinical workflow.

Recommended Safeguards

The model should only operate within a Human-in-the-Loop clinical decision-support workflow.

Predictions exhibiting:

- Low or moderate confidence,
- Conflicting SHAP explanations,
- Atypical laboratory profiles,
- Missing or invalid input data,
- Patient characteristics outside the model's training distribution,

must be routed through the project's Pre-Decision Verification Checkpoint (PDVC) before any clinical action is considered.

The complete PDVC framework is documented separately within Stage 08.

Monitoring After Deployment

If future clinical validation, regulatory approval, and governance review support deployment, continuous monitoring should include:

- Monitoring for changes in patient populations.
- Detection of data drift.
- Monitoring model performance degradation.
- Routine review of false-negative rates.
- Investigation of unexpected prediction patterns.
- Periodic review of SHAP explanations and feature importance.
- Controlled model retraining only after documented investigation, approval, and governance review.

Responsible AI Summary

This model was developed according to Responsible AI principles by:

- Prioritising patient safety through selection based on Bacterial Recall rather than overall accuracy.
- Deliberately excluding the near-proxy Pathogen_Present feature.
- Providing transparent explanations using exact SHAP attributions from a linear model.
- Incorporating mandatory human oversight through the proposed Pre-Decision Verification Checkpoint (PDVC).
- Clearly documenting intended use, prohibited uses, known limitations, governance controls, and deployment constraints.

Relationship to Other Governance Documents

This Model Card forms one component of the Stage 08 Responsible AI governance package.

Document| Primary Purpose
Model Card| Describes the model, intended use, performance, limitations, safeguards, and deployment context.
AI Risk Assessment| Identifies potential harms, failure modes, and governance controls.
Pre-Decision Verification Checkpoint (PDVC)| Defines the operational workflow for mandatory human verification before model outputs may influence clinical decisions.

Together, these documents provide a transparent governance framework for the MVB clinical decision-support prototype.

Stage Status

Status: Completed

Primary Deliverables Produced

- MVB-08-RAI-Model-Card.md
- MVB-08-RAI-AI-Risk-Assessment.md
- MVB-08-RAI-Verification-Checkpoint.md

Input for Next Stage

- Final selected model (LR_B)
- Stage 01–07 project outputs
- Complete Stage 08 Responsible AI governance documentation

Next Stage

09_MVB_Deployment — Develop the Streamlit application integrating the trained model, SHAP explainability, Model Card summary, AI Risk Assessment highlights, and the Pre-Decision Verification Checkpoint (PDVC) as an interactive Responsible AI safeguard.
