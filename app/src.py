def transform_resp(resp):
    def yes_no(column):
        if resp[column] == 'Yes':
            return 1
        else:
            return 0
    
    loans = {
        'Auto Loan': 0,
        'Credit-Builder Loan': 0,
        'Personal Loan': 0,
        'Home Equity Loan': 0,
        'Mortgage Loan': 0,
        'Student Loan': 0,
        'Debt Consolidation Loan': 0,
        'Payday Loan': 0
    }

    if resp['loans'] == None:
        loans['Auto Loan'] = 0
        loans['Credit-Builder Loan'] = 0
        loans['Personal Loan'] = 0
        loans['Home Equity Loan'] = 0
        loans['Mortgage Loan'] = 0
        loans['Student Loan'] = 0
        loans['Debt Consolidation Loan'] = 0
        loans['Payday Loan'] = 0
    else:
        for key_ans in loans.keys():
            if key_ans in resp['loans']:
                loans[key_ans] = 1

    output = {
        'Age': resp['age'],
        'Annual_Income': resp['annual_income'],
        'Num_Bank_Accounts': resp['accounts'],
        'Num_Credit_Card': resp['credit_cards'],
        'Num_of_Delayed_Payment': resp['delayed_payments'],
        'Credit_Utilization_Ratio': resp['credit_card_ratio'],
        'Total_EMI_per_month': resp['emi_monthly'],
        'Credit_History_Age_Formated': resp['credit_history'],
        'Auto_Loan': loans['Auto Loan'],
        'Credit-Builder_Loan': loans['Credit-Builder Loan'],
        'Personal_Loan': loans['Personal Loan'],
        'Home_Equity_Loan': loans['Home Equity Loan'],
        'Mortgage_Loan': loans['Mortgage Loan'],
        'Student_Loan': loans['Student Loan'],
        'Debt_Consolidation_Loan': loans['Debt Consolidation Loan'],
        'Payday_Loan': loans['Payday Loan'],
        'Missed_Payment_Day': yes_no('missed_payment'),
        'Payment_of_Min_Amount_Yes': yes_no('minimum_payment')
    }

    return output