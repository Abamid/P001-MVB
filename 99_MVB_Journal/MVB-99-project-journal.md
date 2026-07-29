Project Code: P001-MVB
Stage: 99_MVB_Journal
Author: Abubakar Amidu
Programme: 3MTT DeepTech Cohort 2 — DS/ML Mentorship
Last Updated: 28 July 2026

---

# MVB Project Journal
Explainable and Responsible AI for Differentiating Bacterial and Viral Meningitis
3MTT DeepTech Cohort 2 — Case Study 001, Responsible AI Series

---

### 2026-07-20
**Stage:** 00 — Proposal
- Submitted deliverable 1: written project proposal.
- Pivoted project from original concept ("Predicting Meningitis Outbreaks Using Environmental and Social Factors") to a clinical classification system, due to lack of a comprehensive, publicly available state-level epidemiological dataset within the mentorship timeline.
- New framing keeps the Responsible AI dimension that motivated the original proposal, now applied to bacterial vs. viral meningitis classification using CSF lab values.
- Finalized project structure and naming convention: project code `MVB`, folder 08 tagged `Responsible-AI-Governance` with `RAI`-prefixed filenames, positioned as Case Study 001 in a broader Responsible AI project series.

---

### 2026-07-21
**Stage:** 01 — Data Acquisition
- Profiled the raw Kaggle dataset: 1,200 rows × 14 columns, no missing values, no duplicates.
- Target variable `Diagnosis` found to have three classes, not two: Bacterial (595), Viral (538), Unknown (67) — flagged for a Stage 02 decision, since the project is a binary classifier.
- Found `Risk_Level` coincidentally shares a count with the Unknown diagnosis class (67 each) but confirmed via cross-tab that only 20 rows actually overlap — not the same population.
- Flagged Age=0 (n=2) as plausible infant cases, and Age>100 (n=43) as needing further plausibility review.

---

### 2026-07-22
**Stage:** 02 — Data Preparation
- Decided to drop the 67 "Unknown" diagnosis rows, justified primarily by the binary classification objective — not by any secondary finding.
- Investigated the Age>100 subgroup further: found a disproportionate association with the Unknown diagnosis class (39.5% vs. 5.6% baseline) and a lab profile that doesn't cleanly track either diagnosis pattern. Decided to retain these rows but document them as a limitation reflecting uncertainty, not confirmed poor data quality.
- Found `WBC_Count` values far exceed real-world CSF white cell count ranges — first concrete evidence that this dataset may not be calibrated to real clinical data.
- Cleaned dataset finalized at 1,133 rows.

---

### 2026-07-24
**Stage:** 03 — Exploratory Data Analysis
- Major finding: `Pathogen_Present` matches the diagnosis label in 94% of cases — a near-perfect proxy rather than an independent clinical signal.
- Ran a separability check across individual blood markers and found several (Hemoglobin, WBC_Blood_Count, CRP_Level) achieve 86–94% classification accuracy completely on their own — far beyond what any single real-world lab marker would achieve. This, combined with the `WBC_Count` scale issue from Stage 02, led to characterizing the dataset as "clinically-inspired but not clinically-calibrated" throughout the rest of the project.
- This finding directly shaped the Stage 04 decision to treat `Pathogen_Present` as a problem to be tested for, not just a feature to include.

---

### 2026-07-25
**Stage:** 04 — Feature Engineering / 05 — Model Training (started)
- Rather than simply including or excluding `Pathogen_Present`, decided to build two parallel feature sets — Full (with it) and Restricted (without) — turning an open question into a direct point of comparison.
- Evaluated engineering a CSF-to-blood-glucose ratio (a real clinical tool) but found the dataset has no paired blood glucose column, so declined to fabricate an approximation.
- Began training six model variants (Logistic Regression, Random Forest, XGBoost × two feature sets). Logistic Regression needed feature scaling to converge; tree-based models didn't.
- Early result: Feature Set B (without `Pathogen_Present`) performed nearly identically to Feature Set A — meaning the model doesn't actually need the proxy feature to work well. This became one of the more important findings of the whole project.

---

### 2026-07-26
**Stage:** 06 — Evaluation / 07 — Explainability
- Selected the final model by Bacterial recall specifically, not aggregate accuracy — per the project's stated clinical priority. Logistic Regression beat Random Forest and XGBoost on this metric (0.958 vs. 0.950 vs. 0.941 recall) despite having lower ROC-AUC. This was a concrete demonstration of why the evaluation criterion matters, not just a footnote.
- Chose Logistic Regression on Feature Set B as the final model — it tied for the best recall while avoiding the `Pathogen_Present` proxy feature, at the cost of a negligible precision difference.
- Ran SHAP analysis on the selected model and confirmed every meaningfully-weighted feature aligns with real clinical understanding of bacterial vs. viral meningitis.
- Examined the model's 5 false-negative test cases individually and found they share conflicting evidence across multiple features, not one dominant misleading marker — this became the concrete basis for one of the Pre-Decision Verification Checkpoint's trigger conditions.

---

### 2026-07-27
**Stage:** 08 — Responsible AI Governance / 09 — Deployment (started)
- Wrote the Model Card, AI Risk Assessment, and Pre-Decision Verification Checkpoint framework — the last of these ties directly back to a real AI deployment failure encountered in a separate education-sector project (TaRL Africa Nigeria), where an LLM confidently recommended something a ground-truth check later proved wrong. That experience is the actual origin of why this project treats human verification as mandatory, not optional.
- Defined six concrete trigger conditions for the checkpoint, each grounded in a specific finding from this project rather than invented abstractly.
- Retrospectively applied the checkpoint to the model's own false negatives and found all five would have been flagged — a genuinely useful piece of evidence that the framework isn't just theoretical.
- Began building the Streamlit application, implementing the model, SHAP explanations, and the checkpoint as actual working logic rather than static documentation.

---

### 2026-07-28
**Stage:** 09 — Deployment (completed) / repository packaging
- Finished the deployment app — five of the six Pre-Decision Verification Checkpoint triggers are implemented as live logic, with the remaining data-quality validation trigger (Trigger 6) partially implemented as a placeholder pending a real input-validation source. Trigger 5 (clinician-initiated escalation) was added as a checkbox in this final round.
- Working through GitHub/Streamlit Cloud deployment prep: requirements.txt, README, LICENSE, and .gitignore all created and reviewed for consistency with the actual repository structure.
- Reflection: the project ended up being less about the classifier itself (which was always going to perform well, given the dataset's separability) and more about the governance layer — proving that a model can be selected, explained, and constrained in a way that's honest about its own limitations. That's the part worth carrying into the next project in this Responsible AI series.

---

### [next entry]
**Stage:**
-
