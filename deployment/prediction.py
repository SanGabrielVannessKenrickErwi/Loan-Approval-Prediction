# import libraries
import pandas as pd
import streamlit as st

# pickle
import pickle

# load model
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)
# load encoder
with open('encoder.pkl', 'rb') as file_1:
    encoder = pickle.load(file_1)

def run():
    # title
    st.title('Loan Approval Prediction')

    # horizontal line
    st.write("---")

    # input banner
    st.image('loan_approval_prediction_image.png')

    # description
    st.write('''This page will allows user to predict loan approval status''')

    # form
    with st.form(key='form parameter'):
        age = st.number_input('Age :', min_value=20, max_value=94, step=1)
        income = st.number_input('Income :', min_value=4000, max_value=200100, step=100)
        home_owner = st.selectbox('Home Ownership :', {'OWN', 'MORTGAGE', 'RENT', 'OTHER'})
        work_length = st.number_input('Work Length :', min_value=0, max_value=22, step=1)
        loan_intent = st.selectbox('Loan Intent :', {'HOMEIMPROVEMENT', 'DEBTCONSOLIDATION', 'MEDICAL', 'PERSONAL',
       'VENTURE', 'EDUCATION'})
        loan_grade = st.radio('Loan Grade :', {'A', 'B', 'C', 'D', 'E', 'F', 'G'})
        loan_amount = st.number_input('Loan Amount :',  min_value=500, max_value=34000, step=100)
        loan_int_rate = st.number_input('Loan Interest Rate :', min_value=5.42, max_value=20.62, step=0.01)
        loan_percent_income = st.slider('Percentage Loan of Income :', 1, 65, 10)
        default = st.radio('Default On Credit :', {'Y', 'N'})
        cred_hist_length = st.number_input('Credit History Length :', 2, 23, 5)

        submit = st.form_submit_button('Predict')

    # data inference
    data = pd.DataFrame([{
        'person_age' : age,
        'person_income' : income,
        'person_home_ownership' : home_owner,
        'person_emp_length' : work_length,
        'loan_intent' : loan_intent,
        'loan_grade' : loan_grade,
        'loan_amnt' : loan_amount,
        'loan_int_rate' : loan_int_rate,
        'loan_percent_income' : loan_percent_income/100,
        'cb_person_default_on_file' : default,
        'cb_person_cred_hist_length' : cred_hist_length}])

    # Show Data
    st.dataframe(data)


    # predict
    if submit:
        data['cb_person_default_on_file'] = encoder.transform(data['cb_person_default_on_file'])
        pred = model.predict(data)
        if pred == 0:
            st.write(f'#### Loan Approval Status : Not Approved')
        else:
            st.write(f'#### Loan Approval Status : Approved')


if __name__ == "__main__":
    run()