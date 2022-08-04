import streamlit as st
import pickle
import pandas as pd
from zipfile import ZipFile
import os
from src import transform_resp
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title='Credit Score App', page_icon='💰', layout='wide',
                   initial_sidebar_state='auto', menu_items={
                        'Get Help': None,
                        'Report a bug': 'https://github.com/devmedeiros/credit-score-classification-app/issues',
                        'About': '''
                        This app was made by **Jaqueline Medeiros** and its purpose is to showcase how a Credit Score Evaluation work in the fictional bank _Bankio_. 
                        
                        This evaluation is using a Machine Learning model, and you can learn more about how the model work and how I got here by going to the GitHub [repository](https://github.com/devmedeiros/credit-score-classification-app).

                        If you are interested in Data Science you can see follow my work through my blog [devmedeiros.com](https://devmedeiros.com) or on LinkedIn [medeiros-jaqueline](https://www.linkedin.com/in/medeiros-jaqueline/).
                        '''
     })

path = os.path.dirname(__file__)
folder_path = os.path.join(path,'../models')

@st.cache(allow_output_mutation=True)
def unzip_load(name):
    path_zip = os.path.join(path,'../models/'+name+'.zip')
    ZipFile(path_zip).extractall(folder_path)
    path_obj = os.path.join(path,'../models/'+name+'.obj')
    return  pickle.load(open(path_obj, 'rb'))

scaler = unzip_load('scaler')
model = unzip_load('model')

st.title('Credit Score Analysis')
st.caption('Made by Jaqueline Medeiros')

st.markdown('''
            This is a mock-up intended for information only, if you wish to learn more about the model behind this please go to the GitHub [repository](https://github.com/devmedeiros/credit-score-classification-app).

            On the left, there's a sidebar (click `>` if you don't see it). Where you can fill out a form - _this data is not saved_ - to see how each piece of information you provided impacts your credit score.
''')

st.info('This still is a work in progress, so features and information on this page may change between visits.')

with st.sidebar:
    st.header('Credit Score Form')
    age = st.slider('What is your age?', min_value=18, max_value=100, step=1)
    annual_income = st.number_input('What is your Annual Income?', min_value=0.00, max_value=300000.00)
    accounts = st.number_input('How many bank accounts do you have?', min_value=0, max_value=20, step=1)
    credit_cards = st.number_input('How many credit cards do you have?', min_value=0, max_value=12, step=1)
    delayed_payments = st.number_input('How many delayed payments do you have?', min_value=0, max_value=20, step=1)
    credit_card_ratio = st.slider('What is your credit card utilization ratio?', min_value=0.00, max_value=100.00)
    emi_monthly = st.number_input('How much EMI do you pay monthly?', min_value=0.00, max_value=5000.00)
    credit_history = st.number_input('How many months old is your credit history?', min_value=0, max_value=500, step=1)
    loans = st.multiselect('Which loans do you have?', ['Auto Loan', 'Credit-Builder Loan', 'Personal Loan',
                                                'Home Equity Loan', 'Mortgage Loan', 'Student Loan',
                                                'Debt Consolidation Loan', 'Payday Loan'])
    missed_payment = st.radio('Have you missed any payments in the last 12 months?', ['Yes', 'No'])
    minimum_payment = st.radio('Have you paid the minimum amount on at least one of your credit cards?', ['Yes', 'No'])

    button = st.button( 'Run the numbers!')

st.header('Credit Score Results')

col1, col2 = st.columns([3, 2])

with col2:
    x1 = [0, 6, 0]
    x2 = [0, 4, 0]
    x3 = [0, 2, 0]
    y = ['0', '1', '2']

    f, ax = plt.subplots(figsize=(5,2))

    p1 = sns.barplot(x=x1, y=y, color='#3EC300')
    p1.set(xticklabels=[], yticklabels=[])
    p1.tick_params(bottom=False, left=False)
    p2 = sns.barplot(x=x2, y=y, color='#FAA300')
    p2.set(xticklabels=[], yticklabels=[])
    p2.tick_params(bottom=False, left=False)
    p3 = sns.barplot(x=x3, y=y, color='#FF331F')
    p3.set(xticklabels=[], yticklabels=[])
    p3.tick_params(bottom=False, left=False)

    plt.text(0.7, 1.05, "POOR", horizontalalignment='left', size='medium', color='white', weight='semibold')
    plt.text(2.5, 1.05, "REGULAR", horizontalalignment='left', size='medium', color='white', weight='semibold')
    plt.text(4.7, 1.05, "GOOD", horizontalalignment='left', size='medium', color='white', weight='semibold')

    ax.set(xlim=(0, 6))
    sns.despine(left=True, bottom=True)

    figure = st.pyplot(f, width=5)

with col1:

    placeholder = st.empty()

    if button:
        resp = {
            'age': age,
            'annual_income': annual_income,
            'accounts': accounts,
            'credit_cards': credit_cards,
            'delayed_payments': delayed_payments,
            'credit_card_ratio': credit_card_ratio,
            'emi_monthly': emi_monthly,
            'credit_history': credit_history,
            'loans': loans,
            'missed_payment': missed_payment,
            'minimum_payment': minimum_payment
        }
        output = transform_resp(resp)
        output = pd.DataFrame(output, index=[0])
        output.loc[:,:] = scaler.transform(output)

        credit_score = model.predict(output)[0]

        if credit_score == 1:
            st.balloons()
            t1 = plt.Polygon([[5, 0.5], [5.5, 0], [4.5, 0]], color='black')
            placeholder.markdown('Your credit score is **GOOD**! Congratulations!')
            st.markdown('This credit score indicates that this person is likely to repay a loan, so the risk of giving them credit is low.')
        elif credit_score == 0:
            t1 = plt.Polygon([[3, 0.5], [3.5, 0], [2.5, 0]], color='black')
            placeholder.markdown('Your credit score is **REGULAR**.')
            st.markdown('This credit score indicates that this person is likely to repay a loan, but can occasionally miss some payments. Meaning that the risk of giving them credit is medium.')
        elif credit_score == -1:
            t1 = plt.Polygon([[1, 0.5], [1.5, 0], [0.5, 0]], color='black')
            placeholder.markdown('Your credit score is **POOR**.')
            st.markdown('This credit score indicates that this person is unlikely to repay a loan, so the risk of lending them credit is high.')
        plt.gca().add_patch(t1)
        figure.pyplot(f)