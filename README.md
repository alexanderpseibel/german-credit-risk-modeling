# Quantitative Risk Management: ML in Retail Credit Scoring

## Project Overview
This project examines whether Machine Learning (ML) can effectively reduce institutional risk in retail credit scoring compared to traditional industry standards. While ML offers high predictive flexibility, this research evaluates its performance under realistic regulatory and organizational constraints.

I developed a comparative modeling framework using the South German Credit dataset to estimate the Probability of Default (PD).

## Key Research Question
> "Does the use of machine learning in retail credit risk modeling reduce overall institutional risk when evaluated under realistic regulatory and organizational constraints?"

## Technical Implementation
### The Modeling Stack
* **Logistic Regression:** Serves as the industry baseline for interpretability and regulatory acceptance.
* **Random Forest:** An ensemble approach used to capture non-linear borrower behavior.
* **XGBoost:** A gradient boosting implementation representing high structural flexibility in capturing higher-order interactions.

### Evaluation Design
Models are evaluated across three dimensions:
* **Discrimination:** ROC-AUC and PR-AUC measure ranking quality independent of any specific decision threshold.
* **Cost-based optimization:** Asymmetric loss functions (5:1 and 10:1 FN:FP ratios) determine cost-optimal thresholds, reflecting that missing a default is more costly than rejecting a solvent borrower.
* **Probability calibration:** Brier scores and reliability diagrams verify that predicted PDs match observed default frequencies — a requirement under Basel IRB and IFRS 9.

## Key Findings
* **Performance:** Tree-based models achieved higher discrimination (Random Forest ROC-AUC 0.777) compared to Logistic Regression (0.756).
* **Risk Sensitivity:** Relative model performance depends on the decision threshold and loss asymmetry; ranking performance alone does not determine the optimal model.
* **Governance:** Analysis of the Population Stability Index (PSI) showed that flexible models can exhibit extreme distributional sensitivity, reinforcing the need for continuous monitoring.
* **Interpretability:** Feature importance consistency was verified using SHAP values to meet transparency requirements under frameworks like the EU AI Act.

## Technologies
* **Language:** Python
* **Libraries:** `scikit-learn`, `XGBoost`, `SHAP`, `Pandas`, `Matplotlib`
* **Domain:** Quantitative Risk Management, Basel IRB Framework, Credit Scoring
