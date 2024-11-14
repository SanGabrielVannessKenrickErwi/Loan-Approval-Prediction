# import libraries
import pandas as pd

# streamlit
import streamlit as st

# Visualization
import matplotlib.pyplot as plt
import seaborn as sns

def run():
    # title
    st.title("Exploratory Data Analysis - Loan Approval")

    # horizontal line
    st.write("---")

    # input banner
    st.image('eda.jpg')

    # section dataframe
    # load dataset
    data = pd.read_csv('D:\p1-ftds021-hck-m2-SanGabrielVannessKenrickErwi\credit_risk_dataset.csv')

    # subheader
    st.write('## Dataframe')

    # show the dataframe
    st.dataframe(data.head())

    # Section EDA
    # subheader
    st.write('## Exploratory Data Analysis')

    # title
    st.write('### Basic Information')

    # subheader
    st.write('#### Numerical Columns')
    
    # Show the basic information of descriptive statistics from numerical columns
    st.dataframe(data.describe(exclude='object').drop(columns='loan_status').T)

    # subheader
    st.write('#### Categorical Columns')
    
    # Show the basic information of categorical columns
    st.dataframe(data.describe(include='object').T)

    # title
    st.write('### Distribution of Loan Status')
    
    # create canvas
    fig = plt.figure(figsize=(15,10))
    # Count the occurrences of each loan status
    loan_status_counts = data['loan_status'].value_counts(normalize=True) * 100

    # Plot the bar chart
    fig = plt.figure(figsize=(6, 4))
    sns.barplot(x=loan_status_counts.index, y=loan_status_counts.values, palette='Blues_d')
    plt.ylabel('Percentage (%)')
    plt.xlabel('Loan Status')

    # Show the percentage on the bars
    for i, value in enumerate(loan_status_counts.values):
        plt.text(i, value + 1, f'{value:.2f}%', ha='center')

    plt.tight_layout()

    # show the plot
    st.pyplot(fig)

    # insight
    st.write('''- The distribution of loan_status shows that only 21.82% of the loans are approved, while 78.18% are not approved.
            \n- The data is highly imbalanced, with a significantly larger proportion of loans being rejected.''')

    # title
    st.write('### Distribution of Loan Intent')

    # Count the occurrences of each loan intent
    loan_intent_counts = data['loan_intent'].value_counts(normalize=True) * 100

    # Plot the bar chart
    fig = plt.figure(figsize=(8, 6))
    sns.barplot(x=loan_intent_counts.index, y=loan_intent_counts.values, palette='muted')
    plt.ylabel('Percentage (%)')
    plt.xlabel('Loan Intent')

    # Show the percentage on the bars
    for i, value in enumerate(loan_intent_counts.values):
        plt.text(i, value + 1, f'{value:.2f}%', ha='center')

    plt.xticks(rotation=45)
    plt.tight_layout()

    # show the plot
    st.pyplot(fig)

    # insight
    st.write('''- The most common loan intent is education, accounting for 19.81% of the data, while the least common is home improvement, at 11.06%.
            \n- The high percentage of education-related loans suggests that a significant portion of applicants are using loans to invest in their education, potentially indicating younger individuals seeking to finance their studies.''')
    
    # title
    st.write('### Distribution of Loan Grades')
    
    # Count the occurrences of each loan grade
    loan_grade_counts = data['loan_grade'].value_counts(normalize=True) * 100

    # Plot the bar chart for loan_grade distribution
    fig = plt.figure(figsize=(8, 6))
    sns.barplot(x=loan_grade_counts.index, y=loan_grade_counts.values, palette='Reds_d')
    plt.ylabel('Percentage (%)')
    plt.xlabel('Loan Grade')

    # Show percentage on top of bars
    for i, value in enumerate(loan_grade_counts.values):
        plt.text(i, value + 0.5, f'{value:.2f}%', ha='center')

    plt.tight_layout()
    # show the plot
    st.pyplot(fig)

    # insight
    st.write('''
    1. **Grades A and B dominate**:  - Over 65% of applicants fall into loan grades A (33.08%) and B (32.08%), indicating that the majority of applicants are considered to have high creditworthiness.

    2. **Grade C is moderately common**: - About 19.82% of applicants are in grade C, suggesting a moderate level of risk for these borrowers.

    3. **Lower grades are rare**: - Grades D, E, F, and G have fewer applicants. Grade D accounts for 11.13%, and it drops significantly for grades E (2.96%), F (0.74%), and G (0.20%). This shows that fewer applicants are classified as higher risk.
    ''')

    # title
    st.write('### Distribution of Loan Amount by Loan Status')

    # Create the histogram
    fig = plt.figure(figsize=(12, 6))
    sns.histplot(data=data, x='loan_amnt', hue='loan_status', multiple='stack', bins=30, palette={1 : 'green', 0 : 'orange'})
    plt.xlabel('Loan Amount')
    plt.ylabel('Frequency')
    plt.grid()
    # show the plot
    st.pyplot(fig)
    
    # insight
    st.write('''1. Loan Approval Trend:
                - Smaller to mid-sized loans (around $5,000 to $15,000) show a higher approval rate compared to larger loans.

            \n2. Larger Loan Approvals:
                - Larger loans (above $15,000) tend to have fewer approvals, indicating a potential higher risk or stricter criteria for these amounts.
                        
            \n3. Approval Proportions:
                - Mid-sized loans show a better balance between applications and approvals, while larger loans have a lower approval proportion.''')
    
    # title
    st.write('### Average Person Income by Loan Status')
    
    # Calculate the average income by loan status
    income_status = data.groupby('loan_status')['person_income'].mean().reset_index()

    # Create a bar chart to visualize the average income by loan status
    fig = plt.figure(figsize=(10, 6))
    sns.barplot(x='loan_status', y='person_income', data=income_status, palette='viridis')
    plt.xlabel('Loan Status')
    plt.ylabel('Average Person Income')
    plt.xticks(rotation=45)
    plt.grid(axis='y')
    # show the plot
    st.pyplot(fig)
    # insight
    st.write('- The bar graph illustrates that the average income for loans that were approved is lower than that for loans that were not approved.')

    # title
    st.write('### Distribution of Home Ownership')

    # Count the occurrences of each loan intent
    home_counts = data['person_home_ownership'].value_counts(normalize=True) * 100

    # Plot the bar chart
    fig = plt.figure(figsize=(8, 6))
    sns.barplot(x=home_counts.index, y=home_counts.values, palette='muted')
    plt.ylabel('Percentage (%)')
    plt.xlabel('Home Ownership')

    # Show the percentage on the bars
    for i, value in enumerate(home_counts.values):
        plt.text(i, value + 1, f'{value:.2f}%', ha='center')

    plt.xticks(rotation=45)
    plt.tight_layout()
    # show the plot
    st.pyplot(fig)

    # insight
    st.write('- The most common type of home ownership is renting, which constitutes 50.48% of the applicants. On the other hand, the least common type is categorized as "other," making up just 0.33% of the data.')

    # horizontal line
    st.write('---')

    # title
    st.write('### Conclusion')
    # insight
    st.write('''#### Applicant Demographics and Characteristics:
                    \n- Age: Most applicants are aged between 20 and 30 years, indicating a younger demographic that may lack stable financial backgrounds, such as permanent jobs or homeownership.
                    \n- Income: The average income is around $66,000, with a broad range from $4,000 to $6,000,000. Applicants with lower incomes are less likely to apply for loans, and outliers indicate high-income individuals are included.
                    \n- Employment Length: The average employment length is around 4 years, with many applicants having short employment histories, which might affect their perceived stability.
                    \n- Home Ownership: Most applicants are renters (50.48%), followed by those with mortgages (41.26%). Only 7.93% own their homes outright, suggesting a younger or less financially stable applicant pool.
                \n#### Loan Characteristics:
                    \n- Loan Amount: The average loan requested is $9,500, with amounts ranging from $500 to $35,000. Mid-sized loans (around $5,000 to $15,000) are more likely to be approved, while larger loans (above $15,000) show fewer approvals.
                    \n- Loan Interest Rates: The average interest rate is 11%, with a range from 5% to 23%. Higher interest rates correlate with a greater likelihood of loan approval.
                    \n- Loan Grade: The majority of applicants fall into loan grades A and B, indicating low risk. Only a small percentage of applicants are in the higher-risk categories (D, E, F, and G).
                    \n- Loan Purpose: Most loans are for education (19.81%), followed by medical expenses, personal reasons, and debt consolidation, which suggests a diverse pool of loan intents.
                    \n- Debt-to-Income Ratio: The average percentage of income allocated to loan repayment is around 17%. However, some applicants allocate up to 83%, indicating a risk of over-leveraging.
                \n#### Creditworthiness:
                    \n- Credit History: The average credit history length is 6 years, with a weak negative correlation to loan approval. Longer credit histories may slightly reduce the likelihood of approval.
                    \n- Default History: Most applicants have no history of default, making them low-risk borrowers. This likely contributes to the predominance of applicants with loan grades A and B
                \n#### Loan Approval Trends:
                    \n- Approval Rate: Only 21.82% of loans are approved, with the remaining 78.18% being rejected. This highly imbalanced data indicates a conservative loan approval process.
                    \n- Income with Loan Approval: A moderate negative correlation between income and loan approval suggests that higher-income applicants are less likely to be approved, potentially due to applying for riskier loans.
                    \n- Loan Amount & Interest Rate with Loan Approval: Larger loans and those with higher interest rates are more likely to be approved, potentially as a way to offset the risk of approving higher-risk applicants.
                    \n- Debt-to-Income Ratio with Loan Approval: Loans with higher debt-to-income ratios are more likely to be approved, indicating that the bank is willing to approve loans for individuals dedicating more of their income to repayment.''')
    
if __name__ == "__main__":
    run()