# Quantitative Risk Management: ML in Retail Credit Scoring

## Project Overview
[cite_start]This project examines whether Machine Learning (ML) can effectively reduce institutional risk in retail credit scoring compared to traditional industry standards[cite: 4, 28]. [cite_start]While ML offers high predictive flexibility, this research evaluates its performance under realistic regulatory and organizational constraints[cite: 28, 55].

[cite_start]I developed a comparative modeling framework using the South German Credit dataset to estimate the Probability of Default (PD)[cite: 69, 85].

## Key Research Question
> [cite_start]"Does the use of machine learning in retail credit risk modeling reduce overall institutional risk when evaluated under realistic regulatory and organizational constraints?" [cite: 28]

## Technical Implementation
### The Modeling Stack
* [cite_start]**Logistic Regression:** Serves as the industry baseline for interpretability and regulatory acceptance[cite: 44, 111].
* [cite_start]**Random Forest:** An ensemble approach used to capture non-linear borrower behavior[cite: 61, 117].
* [cite_start]**XGBoost:** A gradient boosting implementation representing high structural flexibility in capturing higher-order interactions[cite: 123, 127].

### Advanced Evaluation Design
Unlike standard data science projects, this analysis evaluates risk through an institutional and regulatory lens:
* [cite_start]**Discrimination:** Using ROC-AUC and PR-AUC to rank borrower risk independent of specific approval thresholds[cite: 135, 137].
* [cite_start]**Cost-Based Optimization:** Analyzing asymmetric loss where missing a default is more expensive than rejecting a solvent borrower, using 5:1 and 10:1 cost ratios[cite: 148, 152].
* [cite_start]**Probability Calibration:** Using Brier Scores and Reliability Diagrams to ensure predicted probabilities match real-world default frequencies[cite: 159, 209].

## Key Findings
* [cite_start]**Performance:** Tree-based models achieved higher discrimination (Random Forest ROC-AUC 0.777) compared to Logistic Regression (0.756)[cite: 171].
* [cite_start]**Risk Sensitivity:** Relative model performance depends on the decision threshold and loss asymmetry; ranking performance alone does not determine the optimal model[cite: 193, 194].
* [cite_start]**Governance:** Analysis of the Population Stability Index (PSI) showed that flexible models can exhibit extreme distributional sensitivity, reinforcing the need for continuous monitoring[cite: 288, 294].
* [cite_start]**Interpretability:** Feature importance consistency was verified using SHAP values to meet transparency requirements under frameworks like the EU AI Act[cite: 297, 302].

## Technologies
* [cite_start]**Language:** Python [cite: 309]
* [cite_start]**Libraries:** `scikit-learn`, `XGBoost`, `SHAP`, `Pandas`, `Matplotlib` [cite: 309]
* [cite_start]**Domain:** Quantitative Risk Management, Basel IRB Framework, Credit Scoring [cite: 5, 154]