credit-score-classification-app
==============================

a stremlit app on credit score classification

Problem Statement
You are working as a data scientist in a global finance company. Over the years, the company has collected basic bank details and gathered a lot of credit-related information. The management wants to build an intelligent system to segregate the people into credit score brackets to reduce the manual efforts.

| Feature | Description |
|---|----|
|`ID` | Represents a unique identification of an entry |
|`Customer_ID` | Represents a unique identification of a person |
|`Month` | Represents the month of the year |
|`Name` | Represents the name of a person |
|`Age` | Represents the age of the person |
|`SSN` | Represents the social security number of a person |
|`Occupation` | Represents the occupation of the person |
|`Annual_Income` | Represents the annual income of the person |
|`Monthly_Inhand_Salary` | Represents the monthly base salary of a person |
|`Num_Bank_Accounts` | Represents the number of bank accounts a person holds |
|`Num_Credit_Card` | Represents the number of other credit cards held by a person |
|`Interest_Rate` | Represents the interest rate on credit card |
|`Num_of_Loan` | Represents the number of loans taken from the bank |
|`Type_of_Loan` | Represents the types of loan taken by a person |
|`Delay_from_due_date` | Represents the average number of days delayed from the payment date |
|`Num_of_Delayed_Payment` | Represents the average number of payments delayed by a person |
|`Changed_Credit_Limit` | Represents the percentage change in credit card limit |
|`Num_Credit_Inquiries` | Represents the number of credit card inquiries |
|`Credit_Mix` | Represents the classification of the mix of credits |
|`Outstanding_Debt` | Represents the remaining debt to be paid (in USD) |
|`Credit_Utilization_Ratio` | Represents the utilization ratio of credit card |
|`Credit_History_Age` | Represents the age of credit history of the person |
|`Payment_of_Min_Amount` | Represents whether only the minimum amount was paid by the person |
|`Total_EMI_per_month` | Represents the monthly EMI payments (in USD) |
|`Amount_invested_monthly` | Represents the monthly amount invested by the customer (in USD) |
|`Payment_Behaviour` | Represents the payment behavior of the customer (in USD) |
|`Monthly_Balance` | Represents the monthly balance amount of the customer (in USD)
|`Credit_Score` | Represents the bracket of credit score (Poor, Standard, Good)

Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
