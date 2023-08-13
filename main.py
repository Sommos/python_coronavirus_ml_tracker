import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import random, math, time, datetime, operator
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error, mean_absolute_error

if __name__ == "__main__":
    confirmed_cases = pd.read_csv('datasets/01-01-2021.csv')
    confirmed_deaths = confirmed_cases.loc[:, ['Country_Region', 'Confirmed', 'Deaths']]
    print(confirmed_deaths.head())