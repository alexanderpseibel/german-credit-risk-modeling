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

### Advanced Evaluation Design
Unlike standard data science projects, this analysis evaluates risk through an institutional and regulatory lens:
* **Discrimination:** Using ROC-AUC and PR-AUC to rank borrower risk independent of specific approval thresholds.
* **Cost-Based Optimization:** Analyzing asymmetric loss where missing a default is more expensive than rejecting a solvent borrower, using 5:1 and 10:1 cost ratios.
* **Probability Calibration:** Using Brier Scores and Reliability Diagrams to ensure predicted probabilities match real-world default frequencies.

## Key Findings
* **Performance:** Tree-based models achieved higher discrimination (Random Forest ROC-AUC 0.777) compared to Logistic Regression (0.756).
* **Risk Sensitivity:** Relative model performance depends on the decision threshold and loss asymmetry; ranking performance alone does not determine the optimal model.
* **Governance:** Analysis of the Population Stability Index (PSI) showed that flexible models can exhibit extreme distributional sensitivity, reinforcing the need for continuous monitoring.
* **Interpretability:** Feature importance consistency was verified using SHAP values to meet transparency requirements under frameworks like the EU AI Act.

## Technologies
* **Language:** Python
* **Libraries:** `scikit-learn`, `XGBoost`, `SHAP`, `Pandas`, `Matplotlib`
* **Domain:** Quantitative Risk Management, Basel IRB Framework, Credit Scoring
