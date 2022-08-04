# Credit Score Classification App

<div align="center">

  <a href="">[![Status - Under Development](https://img.shields.io/badge/Status-Under_Development-2ea44f)](https://)</a>
  <a href="">[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://devmedeiros-credit-score-classification-appstreamlit-app-fcakrl.streamlitapp.com/)</a>
    <a href="">[![License](https://img.shields.io/badge/License-MIT-blue)](#license)</a>

</div>

![a gif showing how the streamlit credit score app works](https://user-images.githubusercontent.com/33239902/182934370-a15267ad-f789-424b-8a44-5f512f7f3b06.gif)

This streamlit app demonstrate how a company may evaluate a person credit score, you can see the app live [here](https://bit.ly/3boP7Xd).

## Running Locally

If you want to run the app locally you can clone the project

```bash
  git clone https://github.com/devmedeiros/credit-score-classification-app
```

Install the requirements

```bash
  pip install -r requirements.txt
```

Enter the project directory

```bash
  cd credit-score-classification-app
```

Run the Streamlit App

```bash
  streamlit run app/streamlit_app.py
```

## Project Organization

```txt
├── LICENSE
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   └── processed      <- The final, canonical data sets for modeling.
│
├── app                <- Streamlit App.
│
├── models             <- Trained and serialized models.
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering)
│                         and a short `-` delimited description, e.g.
│                         `1.0-initial-data-exploration`.
│
├── references         <- Data dictionary.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
└── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
                          generated with `pip freeze > requirements.txt`
```

## Roadmap
 - improve machine learning model
 - add 3 default profiles on Streamlit

--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>.</small></p>
