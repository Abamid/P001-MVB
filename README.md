# P001-MVB — Explainable and Responsible AI for Differentiating Bacterial and Viral Meningitis

A Clinical Decision Support System | 3MTT DeepTech Cohort 2 — DS/ML Mentorship Programme

**Author:** Abubakar Amidu
**Project Code:** P001-MVB (Case Study 001 in a planned Responsible AI portfolio series)

⚠️ **RESEARCH PROTOTYPE — NOT FOR CLINICAL USE.** This project has not undergone clinical validation, regulatory review, or certification. See [Limitations](#limitations) below.

---

## Live Demo

## Live Resources

### 🚀 Live Streamlit Application

https://p001-mvb-iq6ziqmh6yr9tbdamggaqc.streamlit.app/

**Launch the deployed application to explore:**

- Interactive clinical decision support
- Logistic Regression (Restricted Feature Set) prediction
- SHAP feature-level explanations
- Pre-Decision Verification Checkpoint (PDVC)
- Confidence scoring
- Audit log generation
- Responsible AI governance safeguards

---

### 🐙 GitHub Repository

https://github.com/Abamid/P001-MVB

Complete source code, notebooks, documentation, governance artefacts, and deployment files.

---

### 📊 Presentation

**Placeholder:** Final presentation (PDF) will be linked here.

---

### Application Preview

**Placeholder:** Insert a full-width screenshot of the deployed Streamlit home screen here.

---

## Overview

Meningitis is a medical emergency where rapid, accurate diagnosis directly affects patient outcomes. Bacterial meningitis progresses quickly and can be fatal without prompt treatment; viral meningitis is typically self-limiting. This project builds a machine learning classifier to differentiate bacterial from viral meningitis using cerebrospinal fluid (CSF) and blood laboratory values — paired with a Responsible AI governance framework ensuring the model supports, rather than replaces, clinical judgment.

The governance approach is informed by a real-world AI deployment failure encountered during a separate 10-state education needs assessment project, where an AI-generated recommendation was later found incorrect upon verification with ground-truth sources. That experience motivated the **Pre-Decision Verification Checkpoint** — a structured framework, implemented here as working software, that flags predictions for mandatory human review under specific, evidence-based conditions.

---

## Objectives

1. Build a classifier differentiating bacterial from viral meningitis using CSF and blood laboratory features.
2. Prioritize recall (sensitivity) for bacterial meningitis, since missed cases carry the greatest clinical risk.
3. Apply SHAP explainability so predictions are interpretable rather than a black box.
4. Design and implement a Pre-Decision Verification Checkpoint defining when clinician review is mandatory.
5. Produce a Model Card and AI Risk Assessment documenting intended use, limitations, and prohibited uses.
6. Deploy an interactive Streamlit application demonstrating the full pipeline end to end.

---

## Dataset

**Source:** [Meningitis Classification (Kaggle, ChanTest)](https://www.kaggle.com/)
**Records:** 1,200 original → 1,133 after cleaning (67 records with an "Unknown" diagnosis excluded)
**Target:** Bacterial (595, 52.5%) vs. Viral (538, 47.5%)
**Features used:** Age, Gender, WBC_Count, Protein_Level, Glucose_Level, Hemoglobin, WBC_Blood_Count, Platelets, CRP_Level

**Important caveat:** Analysis across Stages 01–03 found this dataset shows separability characteristics well beyond real-world clinical data (e.g., several individual lab markers alone achieve 86–94% classification accuracy — far higher than any single marker would in practice). The dataset is treated throughout this project as **clinically-inspired but not clinically-calibrated**, and this is reflected explicitly in the Model Card's limitations. See `MVB-01-schema-notes.md` and `MVB-03-eda-notes.md` for full detail.

---

## Technology Stack

- Python
- Streamlit
- Scikit-learn
- SHAP
- Pandas
- NumPy
- Matplotlib
- Jupyter Notebook
- Git & GitHub
- Google Colab

---

## Project Structure

```text
P001-MVB/
├── README.md                          ← you are here
├── LICENSE
├── requirements.txt
├── .gitignore
│
├── 00_MVB_Proposal/                   Project proposal
├── 01_MVB_Data-Acquisition/           Dataset profiling
├── 02_MVB_Data-Preparation/           Cleaning, validation
├── 03_MVB_EDA/                        Exploratory analysis, separability findings
├── 04_MVB_Feature-Engineering/        Feature Set A (Full) / B (Restricted)
├── 05_MVB_Model-Training/             6 trained models (LR/RF/XGBoost × A/B)
├── 06_MVB_Evaluation/                 Model comparison, final selection
├── 07_MVB_Explainability/             SHAP analysis
├── 08_MVB_Responsible-AI-Governance/  Model Card, Risk Assessment, PDVC framework
├── 09_MVB_Deployment/                 Streamlit application
└── 99_MVB_Journal/                    Development journal
```

Each stage folder contains a Jupyter notebook, a markdown documentation file, and any generated figures/results — see the individual `MVB-##-*-notes.md` files for full detail on that stage's decisions and findings.

> **Note:** Folders `10_MVB_Documentation/` and `11_MVB_Presentation/` are planned but not yet created — this structure reflects the repository as it currently exists.

---

## Methodology Summary

| Stage | Summary |
|---|---|
| 01 — Acquisition | Profiled raw dataset; no missing values or duplicates |
| 02 — Preparation | Removed 67 "Unknown"-diagnosis records; documented Age>100 subgroup as a limitation |
| 03 — EDA | Found `Pathogen_Present` is a 94%-match near-proxy for the target; found unusually strong single-feature separability |
| 04 — Feature Engineering | Built two feature sets: Full (with `Pathogen_Present`) and Restricted (without) |
| 05 — Model Training | Trained Logistic Regression, Random Forest, XGBoost on both feature sets (6 models total) |
| 06 — Evaluation | Selected model by **Bacterial recall**, not aggregate accuracy — Logistic Regression outperformed tree-based models on this metric despite lower ROC-AUC |
| 07 — Explainability | SHAP confirmed the model relies on clinically plausible markers, in clinically expected directions |
| 08 — Governance | Produced Model Card, AI Risk Assessment, and Pre-Decision Verification Checkpoint |
| 09 — Deployment | Built a Streamlit app implementing the model, SHAP explanations, and PDVC as live logic |

---

## Model Performance

**Selected model: Logistic Regression, Feature Set B (Restricted)**

| Metric | Value |
|---|---|
| Accuracy | 0.934 |
| Bacterial Recall | 0.958 |
| Bacterial Precision | 0.919 |
| False Negatives | 5 / 119 |
| False Positives | 10 / 108 |

Selected over Random Forest and XGBoost specifically because it achieved the **highest recall for the Bacterial class** — the priority metric given the clinical stakes of a missed diagnosis — despite those models showing higher ROC-AUC. Selected over an equally-performing Logistic Regression variant that included `Pathogen_Present` because this restricted version achieves near-identical performance **without depending on a near-proxy feature**. Full comparison in `06_MVB_Evaluation/MVB-06-evaluation-notes.md`.

---

## Explainability

SHAP (`LinearExplainer`) provides exact, non-approximated feature attributions for the selected linear model. Global feature importance confirms the model relies on clinically established markers (Hemoglobin, CRP, WBC counts, Platelets, Glucose) in directions consistent with known bacterial-vs-viral meningitis patterns. Full analysis, including individual case explanations for all five test-set false negatives, is in `07_MVB_Explainability/MVB-07-explainability-notes.md`.

---

## Responsible AI Governance

This project treats governance as a core deliverable, not an afterthought. Three documents in `08_MVB_Responsible-AI-Governance/`:

- **[Model Card](08_MVB_Responsible-AI-Governance/MVB-08-RAI-Model-Card.md)** — intended use, performance, training data characterization, limitations, prohibited uses
- **[AI Risk Assessment](08_MVB_Responsible-AI-Governance/MVB-08-RAI-AI-Risk-Assessment.md)** — potential harms, failure modes, confidence thresholds, out-of-distribution risks
- **[Pre-Decision Verification Checkpoint](08_MVB_Responsible-AI-Governance/MVB-08-RAI-Verification-Checkpoint.md)** — six concrete, evidence-grounded conditions under which a prediction requires mandatory clinician review before it can inform any decision

The Verification Checkpoint isn't just documented — it's implemented as live logic in the deployed application (see below).

---

## Deployment

An interactive Streamlit application (`09_MVB_Deployment/09_MVB_streamlit-app/app.py`) implements:

- The selected Logistic Regression (Feature Set B) model.
- SHAP explanations (waterfall plot and ranked feature contribution table) for every prediction.
- The Pre-Decision Verification Checkpoint (PDVC), with five of the six governance triggers fully implemented.
- An audit log entry for every prediction.
- A persistent research-prototype warning and human-in-the-loop decision support messaging.

### Streamlit Community Cloud

Deployment is currently in progress.

Once deployment is complete, this section will include:

- **Live Application:** *URL to be added*
- **GitHub Repository:** *URL to be added*

The application will be publicly accessible through Streamlit Community Cloud and will run directly from the GitHub repository.

---

## Limitations

- Training data could not be confirmed as real clinical data — it is characterized throughout this project as clinically-inspired but not clinically-calibrated, and reported performance metrics should not be read as real-world clinical performance estimates.
- No external validation, hyperparameter tuning, or cross-validation was performed.
- The application prototype has no authentication, does not persist audit logs, and has one PDVC trigger (data quality validation) only partially implemented.
- This is a research and educational demonstration only. See the [Model Card](08_MVB_Responsible-AI-Governance/MVB-08-RAI-Model-Card.md) for the full deployment statement and prohibited uses.

---

## Future Improvements

- External validation using real clinical datasets.
- Hyperparameter optimisation.
- Cross-validation and calibration analysis.
- User authentication and role-based access.
- Persistent audit logging.
- Integration with hospital information systems.
- Automated data-quality validation (PDVC Trigger 6).

---

## Acknowledgements

Developed as part of the 3MTT DeepTech Cohort 2 mentorship programme, under mentorship from Chukwukadibia Onyekwere.

---

## License

See [LICENSE](LICENSE).
