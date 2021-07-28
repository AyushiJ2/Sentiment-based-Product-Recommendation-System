
# -*- coding: utf-8 -*-
"""Sentiment Based Recommendation System-Capstone Project.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OoZFOyhrgj2yYC_YJosVOqgfYaa6KiIn
"""
#importing the python libraries
import numpy as np
import pandas as pd
from google.colab import drive
drive.mount('/drive')
#importing needed python libraries
import matplotlib.pyplot as plt
import seaborn as sns
import copy
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.stem import SnowballStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import metrics
from sklearn.naive_bayes import MultinomialNB, BernoulliNB
from sklearn.linear_model import LogisticRegression
from sklearn.dummy import DummyClassifier
from sklearn.metrics import classification_report
from sklearn.metrics import roc_auc_score
from sklearn.metrics import roc_curve
from imblearn.over_sampling import SMOTE
import xgboost as xgb
from xgboost import XGBClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import KFold
from sklearn.model_selection import GridSearchCV
import re
from textblob import TextBlob
sns.set_style('white')
%matplotlib inline
from sklearn.model_selection import train_test_split

#loading the data
review_df=pd.read_csv('/drive/MyDrive/Sentiment Analysis/sample30.csv')