# Loan Approval Prediction

**HuggingFace**

https://huggingface.co/spaces/SGVKE/LoanApproval

**Objective(Background)**

As part of the data science team in this company, I have been assigned to develop a predictive model aimed at streamlining and supporting the efforts of the marketing team. Currently, the marketing team spends a significant amount of time manually identifying potential loan approvals, which can be time-consuming and inefficient. The goal of this predictive model is to allow the marketing team to focus solely on applicants who are most likely to have their loans approved, based on data-driven insights.

By using the model, applicants predicted to be approved can receive more attention, while those predicted to be not approved can be deprioritized. This approach ensures that the marketing team doesn't waste valuable time on low-probability candidates, allowing them to increase efficiency, improve decision-making, and ultimately drive more successful loan conversions.

This predictive system will reduce the workload of the marketing team, enabling them to focus their efforts on high-quality leads and boosting overall productivity and ROI for the company.

**Data Source**

The data source consists of information about individual applicant details, financial metrics, and loan-specific factors. You can view the data using this [link]('https://www.kaggle.com/datasets/itshappy/ps4e9-original-data-loan-approval-prediction').

**Data Description**

The data contains 32,581 entries across 12 columns with 7 numerical colums, 4 categorical columns and 1 column as target.

 Columns | Data Type | Decription
 ---|---|---
 person_age | Int | Applicant's age in years.
 person_income | Float | Annual income of the applicant in USD.
 person_home_ownership | Object | Status of homeownership.
 person_emp_length | Float | Length of employment in years.
 loan_intent | Object | Purpose of the loan.
 loan_grade | Object | Risk grade assigned to the loan, assessing the applicant's creditworthiness.
 loan_amnt | Float | Total loan amount requested by the applicant.
 loan_int_rate | Float | Interest rate associated with the loan.
 loan_status (target) | Object | The approval status of the loan(approved or not approved).
 loan_percent_income | Float | Percentage of the applicant's income allocated towards loan repayment.
 cb_person_default_on_file | Object | Indicates if the applicant has a history of default ('Y' for yes, 'N' for no).
 cb_person_cred_hist_length | Int | Length of the applicant's credit history in years.

**Conclusion**

1. Recall Performance Analysis:
    - Cross-Validation Improvement: The slight increase in cross-validation recall (from 0.849 to 0.855) indicates enhanced generalization but highlights the need for further refinement in capturing diverse applicant scenarios.
    - Test Recall Decline: The drop in test recall (from 0.731 to 0.72) post-tuning suggests potential overfitting, where the model fails to generalize effectively to new data. This indicates the need for more robust validation methods.
2. High AUC Performance: 
    - Both before and after tuning, the AUC score remains excellent (~0.897–0.898), indicating strong model performance in distinguishing between approved and rejected loans.
3. Opportunity Loss:
    - Missed Approvals: The current test recall implies that 28% of potential loan approvals are missed, which translates to significant revenue loss and missed opportunities for the marketing team to engage high-probability applicants.
4. Resource Allocation:
    - Reallocation for Efficiency: By identifying patterns in applicant data that correlate with successful approvals, the bank can allocate resources more effectively, focusing efforts on applicants who are statistically more likely to be approved.