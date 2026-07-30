3MTT DeepTech Cohort 2 — DS/ML Mentorship Programme

Submitted by: Abubakar Amidu
Date: July 20, 2026

# Project Title

Explainable and Responsible AI for Differentiating Bacterial and Viral Meningitis: A Clinical Decision Support System

# Problem Statement

Meningitis remains a medical emergency in which rapid, accurate diagnosis directly determines patient outcomes. Bacterial meningitis progresses quickly and can be fatal if untreated, while viral meningitis is typically self-limiting and generally does not require antibiotic therapy. Distinguishing between the two often relies on cerebrospinal fluid (CSF) analysis and clinical presentation, but delays or misclassification can lead to serious consequences—including unnecessary antibiotic treatment or failure to promptly treat bacterial meningitis.

Machine learning models trained on CSF laboratory results and clinical features have the potential to support faster and more consistent differentiation. However, deploying AI in a diagnostic context introduces significant risks: a highly confident but incorrect prediction, if accepted without verification, can directly affect patient safety. This project therefore treats Responsible AI as a core design principle rather than an afterthought by combining a predictive classification model with a governance framework that ensures the model supports, rather than replaces, clinical judgment.

This governance approach is informed by my experience during a 10-state TaRL Africa Nigeria education needs assessment, where AI-generated analytical outputs required verification against ground-truth evidence before informing recommendations. That experience reinforced the importance of structured verification checkpoints for high-impact AI-assisted decision-making.

# Objectives

1. Build a machine learning classifier to differentiate bacterial from viral meningitis using CSF laboratory values and clinical features.
2. Evaluate multiple machine learning algorithms and select the best-performing model using metrics appropriate for high-stakes healthcare applications, with recall (sensitivity) for bacterial meningitis prioritized to minimize missed cases.
3. Apply explainability techniques using SHAP (with LIME explored where appropriate) so model predictions are understandable to clinicians rather than functioning as a black box.
4. Design and document a Pre-Decision Verification Checkpoint that defines when a clinician must review, verify, or override model predictions before they influence treatment decisions, including explicit handling of low-confidence predictions and high-risk scenarios.
5. Produce a Model Card documenting the model's intended use, performance, assumptions, limitations, and explicitly prohibited uses (e.g., autonomous diagnosis or treatment decisions).
6. Produce an AI Risk Assessment covering intended users, potential harms, high-risk failure modes, human oversight requirements, confidence thresholds, deployment assumptions, out-of-distribution risks, and recommended governance controls.
7. Deploy the final model as an interactive Streamlit application that presents predictions together with model explanations and the clinician verification checkpoint, rather than providing a standalone diagnostic decision.

# Proposed Dataset

Source: Kaggle — Meningitis Classification (ChanTest)

The dataset consists of patient-level clinical records containing cerebrospinal fluid (CSF) laboratory values and relevant clinical or demographic features labeled according to meningitis type.

Unit of Analysis: One patient case per row.

The exact feature set, dataset size, class distribution, and metadata will be confirmed during Phase 2 (Data Acquisition) through detailed profiling of the raw dataset before model development begins.

# Proposed Tools and Libraries

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- XGBoost
- Random Forest
- SHAP (with LIME explored where appropriate)
- Jupyter Notebook
- Streamlit

# Methodology

## 1. Data Acquisition
- Download and inspect the Kaggle dataset.
- Document dataset schema, feature descriptions, class balance, and data quality.

## 2. Data Preparation and Validation
- Handle missing values.
- Remove duplicate records.
- Validate feature ranges against known clinical plausibility (e.g., CSF glucose and protein values).
- Verify label consistency.

## 3. Exploratory Data Analysis
- Examine feature distributions.
- Explore relationships between CSF biomarkers and diagnosis.
- Investigate correlations.
- Assess class imbalance.

## 4. Feature Engineering
- Create clinically meaningful derived variables where appropriate (e.g., CSF-to-blood glucose ratio).
- Evaluate feature usefulness for classification.

## 5. Model Training
Train and compare multiple classification algorithms including:
- Logistic Regression
- Random Forest
- XGBoost

Perform hyperparameter tuning and cross-validation.

## 6. Model Evaluation and Ethics
Evaluate using:
- Accuracy
- Precision
- Recall (priority metric)
- F1-score
- ROC-AUC

Conduct detailed analysis of false-negative errors due to their clinical implications.

## 7. Model Explainability
Use SHAP to:
- Explain individual predictions.
- Identify the most influential clinical features.
- Assess whether explanations align with accepted clinical reasoning.

## 8. Responsible AI and Clinical Decision Governance
Design a governance workflow that includes:
- A Pre-Decision Verification Checkpoint.
- Human review requirements.
- Confidence thresholds triggering mandatory clinician verification.
- Recommended usage boundaries.
- Guidance for handling uncertain predictions.

## 9. Deployment
Develop a Streamlit application that:
- Predicts meningitis type.
- Displays prediction confidence.
- Provides feature-level explanations.
- Clearly indicates that clinician verification is required before clinical use.

## 10. Documentation
Produce:
- README
- Data Dictionary
- Methodology Report
- Model Card
- AI Risk Assessment
- Installation Guide
- Reproducibility Guide

## 11. Presentation
Prepare a final project presentation demonstrating:
- Data preparation
- Model development
- Explainability
- Responsible AI governance framework
- Live Streamlit demonstration

# Expected Outcome

A functioning, explainable machine learning system capable of differentiating bacterial and viral meningitis from patient clinical and CSF laboratory features.

The project will be paired with a documented Responsible AI governance framework for AI-assisted clinical decision support, demonstrating how explainability, structured human verification, and risk management can be incorporated into high-stakes machine learning workflows. The resulting system is intended to support clinicians in decision-making and must not be used as an autonomous diagnostic or treatment tool.

# Why This Project

This project integrates three complementary areas of my experience:

- Public health field experience through UNICEF and Save the Children programmes across Nigeria's meningitis belt.
- Applied machine learning experience from previous predictive health modeling projects.
- Ongoing research interest in AI Governance and Responsible AI, particularly the design of Pre-Decision Verification Checkpoints for high-impact AI systems.

While my original proposal focused on predicting meningitis outbreaks using environmental and social factors, the absence of a comprehensive, publicly available state-level epidemiological dataset made that project impractical within the mentorship timeline.

This reformulated project leverages a high-quality, publicly available clinical dataset while preserving—and strengthening—the Responsible AI dimension that motivated the original proposal.

# Next Steps

1. Download and profile the Kaggle dataset.
2. Confirm dataset schema, class distribution, feature definitions, and metadata.
3. Document dataset limitations and assumptions.
4. Finalize the AI Risk Assessment structure and Pre-Decision Verification Checkpoint framework.
5. Begin Exploratory Data Analysis and feature engineering.
