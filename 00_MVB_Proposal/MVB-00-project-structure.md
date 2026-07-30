# MVB — Project Structure & Naming Convention

**Project 001 in a Responsible AI Series**
Explainable and Responsible AI for Differentiating Bacterial and Viral Meningitis: A Clinical Decision Support System
3MTT DeepTech Cohort 2 — DS/ML Mentorship Programme

---

## Project Code

**MVB** — Meningitis Viral/Bacterial

This project is positioned as **Case Study 001** in a broader Responsible AI series. The recurring contribution across the series is the **Pre-Decision Verification Checkpoint** framework, applied to different application domains. MVB stands on its own technical merit as an end-to-end classification system, with Responsible AI governance as an explicit, first-class deliverable rather than an afterthought.

---

## Folder & File Structure
P001-MVB/
├── README.md
├── LICENSE
├── requirements.txt
├── .gitignore
├── environment.yml (optional)
│
├── 00_MVB_Proposal/
├── 01_MVB_Data-Acquisition/
├── 02_MVB_Data-Preparation/
├── 03_MVB_EDA/
├── 04_MVB_Feature-Engineering/
├── 05_MVB_Model-Training/
├── 06_MVB_Evaluation/
├── 07_MVB_Explainability/
├── 08_MVB_Responsible-AI-Governance/
├── 09_MVB_Deployment/
├── 10_MVB_Documentation/
├── 11_MVB_Presentation/
└── 99_MVB_Journal/
---

## Naming Convention Rules

1. **Folders** are prefixed with a two-digit sequence number so Drive and GitHub both sort them in pipeline order automatically.
2. **Files** carry the project code (`MVB`) plus the same sequence number as their folder, so a file's origin is traceable even if it's moved.
3. **Responsible AI deliverables** (folder 08) additionally carry an `RAI` tag in the filename, making the governance focus unmistakable.
4. **`00`** is reserved for planning/scoping deliverables — they precede the numbered technical pipeline.
5. **`99`** is reserved for the running journal — it bookends the pipeline rather than sitting inside it.

---

## Series Positioning

| # | Project | Domain |
|---|---------|--------|
| 001 | **MVB** — Explainable & Responsible AI for Meningitis Classification | Clinical decision support |
| 002 | *(future)* Responsible AI for Loan Approval Models | Financial services |
| 003 | *(future)* Responsible AI for Educational Risk Prediction | Education |
| 004 | *(future)* Responsible AI for Environmental Health Forecasting | Environmental health |

Each project stands independently on technical merit; the Pre-Decision Verification Checkpoint framework is the connecting thread across the series.
