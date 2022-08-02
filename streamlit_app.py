import streamlit as st
import pickle

st.set_page_config(page_title='Credit Score - Bankio', page_icon='💰', layout='wide',
                   initial_sidebar_state='auto', menu_items={
                        'Get Help': None,
                        'Report a bug': 'https://github.com/devmedeiros/credit-score-classification-app/issues',
                        'About': '''
                        This app was made by **Jaqueline Medeiros** and its purpose is to showcase how a Credit Score Evaluation work in the fictional bank _Bankio_. 
                        
                        This evaluation is using a Machine Learning model, and you can learn more about how the model work and how I got here by going to the GitHub [repository](https://github.com/devmedeiros/credit-score-classification-app).

                        If you are interested in Data Science you can see follow my work through my blog [devmedeiros.com](https://devmedeiros.com) or on LinkedIn [medeiros-jaqueline](https://www.linkedin.com/in/medeiros-jaqueline/).
                        '''
     })

#model = pickle.load(open('models/model.obj', 'rb'))

st.image('https://user-images.githubusercontent.com/33239902/182270472-10d2bf4b-0b81-47f5-80cb-6ad3c53abc92.png')

st.title('Credit Score Analysis')

st.markdown('So you want to apply for a loan at _Bankio_? Just enter your details so we can see your credit score!')

col1, col2 = st.columns([2, 4])

with col1:
    st.header('Credit Score Form')
    age = st.slider('What is your age?', min_value=18, max_value=100, step=1)
    annual_income = st.number_input('What is your Annual Income?', min_value=0.00, max_value=300000.00)
    accounts = st.slider('How many bank accounts do you have?', min_value=0, max_value=20, step=1)
    credit_cards = st.slider('How many credit cards do you have?', min_value=0, max_value=12, step=1)
    delayed_payments = st.slider('How many delayed payments do you have?', min_value=0, max_value=20, step=1)
    credit_card_ratio = st.slider('What is your credit card utilization ratio?', min_value=0.00, max_value=100.00)
    emi_monthly = st.number_input('How much EMI do you pay monthly?', min_value=0.00, max_value=100.00)
    credit_history = st.number_input('How many months old is your credit history?', min_value=0, max_value=500, step=1)
    loans = st.multiselect('Which loans do you have?', ['Auto Loan', 'Credit-Builder Loan', 'Personal Loan',
                                                'Home Equity Loan', 'Mortgage Loan', 'Student Loan',
                                                'Debt Consolidation Loan', 'Payday Loan'])
    missed_payment = st.radio('Have you missed any payment in the last 12 months?', ['Yes', 'No'])
    minimum_payment = st.radio('Have you payed the minimum amount in at lest one of your credit cards?', ['Yes', 'No'])

    button = st.button( 'Run the numbers!')
    credit_score = 1

with col2:
    st.header('Credit Score Results')

    placeholder = st.empty()

    if button:
        if credit_score == 1:
            st.balloons()
            placeholder.markdown('Your credit score is **GOOD**! Congratulations!')
        elif credit_score == 0:
            placeholder.markdown('Your credit score is **REGULAR**.')
        elif credit_score == -1:
            placeholder.markdown('Your credit score is **POOR**. You need to work on your finances to improve your credit score.')