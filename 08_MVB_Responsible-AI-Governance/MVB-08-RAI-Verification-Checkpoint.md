Project Code: P001-MVB
Stage: 08_MVB_Responsible-AI-Governance
Document Version: v1.0
Model Version: v1.0
Author: Abubakar Amidu
Programme: 3MTT DeepTech Cohort 2 — DS/ML Mentorship
Last Updated: 28 July 2026

MVB-08 — Pre-Decision Verification Checkpoint (PDVC)

Project: P001-MVB — Explainable and Responsible AI for Differentiating Bacterial and Viral Meningitis: A Clinical Decision Support System

Document History

Version| Date| Author| Description
v1.0| 27 Jul 2026| Abubakar Amidu| Initial Pre-Decision Verification Checkpoint framework
v1.1| 28 Jul 2026| Abubakar Amidu| Added implementation status note aligning trigger count with the Stage 09 deployed prototype

Purpose

Define the specific conditions under which a prediction produced by the MVB Meningitis Classifier must be flagged for mandatory clinician verification before it is permitted to influence diagnostic or treatment decisions, thereby operationalising the project's central Responsible AI governance concept into a practical clinical workflow.

Origin of the Concept

The Pre-Decision Verification Checkpoint (PDVC) originated from a governance concept developed prior to this project following a real-world AI deployment experience during a 10-state TaRL Africa Nigeria education needs assessment. In that project, a Large Language Model confidently recommended a language-of-instruction strategy based on available policy documents. However, subsequent verification with education officials revealed that actual classroom practice differed from the AI's recommendation.

That experience highlighted an important governance lesson: in high-impact domains, AI outputs should not directly influence important decisions without structured human verification against reliable evidence.

This project represents the first practical implementation of that governance concept within an evaluated machine learning system. Rather than presenting the idea only as a theoretical principle, the framework is grounded in empirical evidence collected throughout Stages 02–07 of this project.

Governance Principles

The Pre-Decision Verification Checkpoint is built around four core Responsible AI principles:

1. Human Authority

Final responsibility for diagnosis and treatment always remains with the clinician, never the AI model.

2. Transparency

Every verification request clearly communicates why the checkpoint was triggered.

3. Evidence-Based Escalation

Verification is initiated using predefined, documented trigger conditions rather than subjective judgement alone.

4. Accountability

Every verification event is recorded to support auditing, continuous improvement, and future model evaluation.

What Triggers the Checkpoint

A prediction is routed to mandatory clinician verification whenever any of the following conditions is satisfied. Each trigger is supported either by evidence generated during this project or by established Responsible AI governance practice.

Trigger| Condition| Basis
1. Moderate or Low Model Confidence| Predicted probability falls between 0.60–0.90 (moderate confidence) or below 0.60 (low confidence).| Stage 08 AI Risk Assessment
2. Conflicting Feature-Level Evidence| SHAP explanations show important features simultaneously supporting both Bacterial and Viral predictions.| Stage 07 — all five false-negative cases displayed this pattern.
3. Age Outside the Well-Characterised Range| Patient age exceeds 100 years.| Stage 02 data quality assessment.
4. Out-of-Distribution Feature Values| One or more laboratory values fall outside the minimum or maximum ranges observed during model training.| Standard Responsible AI safeguard against unreliable extrapolation.
5. Clinician-Initiated Escalation| A clinician requests verification despite no automatic trigger being activated.| Preserves clinician authority.
6. Data Quality Validation Failure| Required laboratory measurements are missing, inconsistent, invalid, or fail input validation before prediction.| Responsible AI good practice and Stage 02 data-quality principles.

Implementation note: In the current Stage 09 research prototype, Triggers 1–5 are fully implemented. Trigger 6 (Data Quality Validation Failure) is partially implemented as a placeholder pending more comprehensive input-validation logic.

What Happens at the Checkpoint

When any trigger activates, the following workflow is enforced:

1. The model prediction and its explainability output remain visible to the clinician.

2. The system clearly displays the reason(s) why verification has been triggered.

3. The clinician is instructed to review additional evidence such as patient history, physical examination findings, repeat laboratory investigations, CSF culture results, imaging, or other clinically appropriate confirmatory information.

4. The clinician records the final clinical judgement alongside the model prediction.

5. No prediction meeting any PDVC trigger may directly influence diagnosis or treatment until clinician verification has been completed.

6. Every verification event is stored within an audit log containing:

   - Trigger(s) activated
   - Model prediction
   - Prediction probability
   - SHAP explanation (where applicable)
   - Clinician decision
   - Timestamp
   - Model version

Worked Example — Application to Stage 07 False-Negative Cases

Retrospective analysis of the five false-negative Bacterial cases identified during Stage 06 demonstrates the practical value of the PDVC framework.

All five cases exhibited conflicting feature-level evidence during the Stage 07 SHAP analysis. Consequently, every one of these cases would have activated Trigger 2 (Conflicting Feature-Level Evidence) and therefore required mandatory clinician verification before the model's Viral prediction could influence clinical decision-making.

Importantly, this retrospective analysis does not demonstrate that the checkpoint would necessarily have prevented every missed diagnosis. Rather, it demonstrates that each false-negative prediction would have been prevented from reaching an unreviewed conclusion, ensuring additional clinical assessment before any decision could be influenced by the model.

Explicit Limitations

The proposed framework has several important limitations.

1. Research Prototype

The PDVC is a proposed governance framework and has not been validated within routine clinical practice.

2. Confidence Thresholds

The probability thresholds defined in this framework were derived from the project's evaluation dataset and require recalibration before any operational deployment.

3. Alert Fatigue

Repeated verification requests could eventually reduce user responsiveness if the framework generated excessive alerts, a well-recognised challenge within clinical decision-support systems.

4. Technical Dependencies

Trigger 4 requires accurate implementation of training-data range monitoring, while Trigger 6 requires robust input validation before model inference.

5. Prospective Validation

Although retrospective evaluation demonstrates that all five false-negative evaluation cases would have activated the checkpoint, prospective clinical studies would be required to determine whether the framework genuinely improves clinician decision-making, diagnostic accuracy, or patient outcomes.

Relationship to Other Governance Documents

The three governance documents produced in Stage 08 serve complementary purposes.

Document| Purpose
Model Card| Describes the model, intended use, limitations, and appropriate deployment context.
AI Risk Assessment| Identifies potential harms, failure modes, and governance controls.
Pre-Decision Verification Checkpoint (PDVC)| Converts those governance controls into an operational workflow specifying when mandatory human verification is required.

Together, these documents form the Responsible AI governance framework for the MVB project.

Summary

The Pre-Decision Verification Checkpoint transforms a governance concept—originally motivated by a real-world AI deployment experience—into six concrete, evidence-based trigger conditions for this explainable clinical decision-support system.

Unlike traditional AI pipelines that simply present model predictions, the PDVC introduces a mandatory verification stage whenever predefined risk conditions are detected. Retrospective evaluation demonstrates that every false-negative case identified during model testing would have activated the checkpoint and therefore required clinician review before influencing decision-making.

This work should be viewed as a proof-of-concept implementation of the Pre-Decision Verification Checkpoint within an explainable AI clinical decision-support system. While the framework demonstrates practical feasibility within this project, prospective evaluation using real clinical workflows would be required before considering any operational healthcare deployment.

Stage Status

Status: Completed

Primary Deliverables Produced

- MVB-08-RAI-Model-Card.md
- MVB-08-RAI-AI-Risk-Assessment.md
- MVB-08-RAI-Verification-Checkpoint.md

Input for Next Stage

- Selected model (LR_B)
- Stage 01–07 project outputs
- Complete Stage 08 governance documentation

Next Stage

09_MVB_Deployment — Develop the Streamlit application integrating the trained model, SHAP explainability, Model Card summary, AI Risk Assessment highlights, and the Pre-Decision Verification Checkpoint as an interactive Responsible AI safeguard.
