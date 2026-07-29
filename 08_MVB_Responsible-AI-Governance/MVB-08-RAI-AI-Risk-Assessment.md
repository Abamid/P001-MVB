Project Code: P001-MVB
Stage: 08_MVB_Responsible-AI-Governance
Document Version: v1.0
Model Version: v1.0
Author: Abubakar Amidu
Programme: 3MTT DeepTech Cohort 2 — DS/ML Mentorship
Last Updated: 27 July 2026

MVB-08 — AI Risk Assessment

Project: P001-MVB — Explainable and Responsible AI for Differentiating Bacterial and Viral Meningitis: A Clinical Decision Support System

Document History

Version| Date| Author| Description
v1.0| 27 Jul 2026| Abubakar Amidu| Initial AI Risk Assessment

Purpose

Assess the potential harms, failure modes, and governance requirements associated with the MVB Meningitis Classifier (LR_B), and define the governance controls and ongoing monitoring mechanisms required to mitigate identified risks if this model were ever considered beyond a research prototype.

Intended Users and Use Context

Primary users: Clinicians and healthcare professionals trained to interpret CSF and blood laboratory values while exercising independent clinical judgement over any model output.

Use context: Research and educational demonstration only (Stage 09 Streamlit application). The model has not been clinically validated or approved for real-world medical decision-making.

Out-of-scope users:

- Patients or caregivers directly interpreting model outputs.
- Non-clinical staff.
- Autonomous clinical systems.
- Any triage or emergency workflow operating without qualified clinician oversight.

Governance assumption: This assessment assumes the model is used solely as a clinical decision-support tool and never as an autonomous clinical decision-maker.

Overall Risk Rating

Category| Rating
Clinical Risk| High
Technical Risk| Medium
Explainability Risk| Low
Deployment Readiness| Research Prototype Only

Overall Assessment

If applied to real clinical care, this model should be regarded as High Risk because it has not undergone external clinical validation or regulatory evaluation. Within its intended research context, the identified risks are appropriately mitigated through documentation, transparency, explainability, and mandatory human oversight.

Potential Harms

Harm| Description| Severity
Missed Bacterial diagnosis (False Negative)| Clinician over-relies on model output and delays treatment for a patient incorrectly classified as Viral.| Critical
Unnecessary treatment (False Positive)| Clinician initiates antibiotic treatment for a Viral case because of excessive reliance on model output.| Moderate
False confidence from explainability| SHAP explanations are interpreted as proof that a prediction is correct rather than an explanation of the model's reasoning.| Moderate–High
Inappropriate generalisation| Model is applied to patient populations or healthcare settings not represented in the training data.| High
Automation bias| Clinician gradually defers to model recommendations instead of exercising independent clinical judgement.| High
Data quality mismatch| Differences in laboratory measurement units, calibration procedures, or reporting standards between deployment sites and the training dataset result in unreliable predictions.| High

High-Risk Failure Modes

1. Atypical clinical presentations

Stage 06 and Stage 07 identified five false-negative Bacterial cases whose laboratory profiles contained conflicting clinical evidence across multiple biomarkers rather than one obvious distinguishing feature. These represent precisely the situations where independent clinician assessment remains essential.

2. Deployment without external validation

The dataset used throughout this project is characterised as clinically-inspired but not clinically-calibrated. Consequently, real-world error rates remain unknown and may differ substantially from those observed during model evaluation.

3. Model drift and data drift

Changes in patient populations, disease characteristics, laboratory equipment, reporting standards, or healthcare practice could reduce predictive performance over time if the model were deployed without continuous monitoring.

4. Confidence threshold misuse

Applying a single fixed decision threshold without uncertainty handling may cause borderline predictions to appear equally reliable as high-confidence predictions, increasing the risk of inappropriate clinical reliance.

Human Oversight Requirements

The following governance controls are considered mandatory for any future deployment:

- Every prediction must be reviewed by a qualified clinician before influencing diagnosis or treatment.
- Every case satisfying the Pre-Decision Verification Checkpoint (PDVC) criteria must undergo mandatory clinician verification before the prediction is considered.
- Periodic independent auditing should compare model predictions against confirmed clinical outcomes.
- The user interface must clearly communicate that the model remains a research prototype and has not been clinically validated.
- Clinicians should receive appropriate training covering the model's intended use, limitations, explainability outputs, and appropriate interpretation before using the system.

Confidence Threshold Guidance

The model outputs both a predicted class and an associated probability.

The following thresholds are proposed as governance guidance for this research prototype.

Predicted Probability| Interpretation| Recommended Action
>0.90| High confidence| Display prediction with explanation. Clinician review remains mandatory.
0.60–0.90| Moderate confidence| Display uncertainty warning and activate the Pre-Decision Verification Checkpoint.
<0.60| Low confidence| Treat prediction as inconclusive. Recommend confirmatory diagnostic testing irrespective of predicted class.

Important Note

These thresholds represent proposed governance thresholds for this research prototype rather than clinically validated operating thresholds. They should be recalibrated using real-world clinical validation data before any operational deployment.

Out-of-Distribution Risks

Age Extremes

The retained subgroup of patients aged greater than 100 years (n = 43) displayed anomalous characteristics during Stage 02, including disproportionate association with the excluded "Unknown" diagnosis category and inconsistent laboratory profiles. Predictions involving such patients should therefore receive additional scrutiny.

Population Differences

The dataset contains limited demographic information beyond Age and Gender. Consequently, the model's behaviour across different ethnic groups, geographical regions, healthcare systems, disease prevalence levels, or comorbidity profiles remains unknown.

Laboratory Measurement Differences

Stage 02 identified WBC_Count values that differ substantially from typical real-world CSF measurement scales. Differences in laboratory units, calibration procedures, or reporting conventions could significantly reduce model reliability unless appropriately standardised before deployment.

Recommended Governance Controls

The following controls are recommended before any consideration of clinical deployment:

1. Do not deploy the model without independent validation using ethically sourced real clinical datasets.

2. Maintain the Pre-Decision Verification Checkpoint (PDVC) as a mandatory, non-bypassable governance safeguard.

3. Record every prediction together with clinician decisions and confirmed outcomes to enable auditing and performance monitoring.

4. Establish clearly defined accountability, including named clinical and technical owners responsible for model oversight.

5. Reassess this AI Risk Assessment whenever the model, feature set, deployment environment, or intended use changes.

6. Conduct periodic fairness and performance reviews whenever the model is retrained or evaluated within a new healthcare environment, particularly if future datasets include sufficient demographic information for subgroup analysis.

Residual Risk Assessment

Even after implementing all recommended governance controls, residual risk remains because:

- The model has not undergone external validation.
- The training dataset may not accurately represent real clinical practice.
- Rare or atypical patient presentations may continue to produce incorrect predictions.
- Clinical decision-support systems cannot eliminate diagnostic uncertainty.

Accordingly, governance measures reduce—but do not eliminate—the risks associated with this prototype.

Summary

This assessment identifies missed Bacterial diagnosis (false negatives) as the highest-risk failure mode, consistent with the clinical objective that guided model selection during Stage 06. The principal risk mitigations are mandatory clinician oversight, the Pre-Decision Verification Checkpoint, explainable model outputs, documented confidence threshold guidance, continuous monitoring, and explicit restrictions on deployment without external validation.

Collectively, these governance controls reduce—but do not eliminate—the risks associated with the current research prototype and should be regarded as the minimum requirements before any future clinical evaluation.

Stage Status

Status: Completed

Completed within Stage 08

- Model Card
- AI Risk Assessment

Remaining Documents

- Pre-Decision Verification Checkpoint (PDVC)
- Responsible AI Governance Summary
- Stage 09 deployment documentation
