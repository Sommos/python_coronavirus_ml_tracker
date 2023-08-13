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
    coronavirus_data = pd.read_csv('datasets/01-01-2021.csv')
    confirmed_cases = pd.read_csv('datasets/time_series_2019-ncov-Confirmed.csv')
    confirmed_deaths = pd.read_csv('datasets/time_series_2019-ncov-Deaths.csv')
    confirmed_recoveries = pd.read_csv('datasets/time_series_2019-ncov-Recovered.csv')

    print(confirmed_cases.head())
    print(confirmed_deaths.head())
    print(confirmed_recoveries.head())
    print(coronavirus_data.head())

    columns = confirmed_cases.keys()
    print(columns)

    confirmed = confirmed_cases.loc[:, columns[4]:columns[-1]]
    deaths = confirmed_deaths.loc[:, columns[4]:columns[-1]]
    recoveries = confirmed_recoveries.loc[:, columns[4]:columns[-1]]

    dates = confirmed.keys()
    world_cases = []
    total_deaths = []
    mortality_rate = []
    recovery_rate = []
    total_recovered = []
    total_active = []

    china_cases = []
    italy_cases = []
    us_cases = []
    spain_cases = []
    france_cases = []
    germany_cases = []
    uk_cases = []
    russia_cases = []
    brazil_cases = []
    india_cases = []

    china_deaths = []
    italy_deaths = []
    us_deaths = []
    spain_deaths = []
    france_deaths = []
    germany_deaths = []
    uk_deaths = []
    russia_deaths = []
    brazil_deaths = []
    india_deaths = []

    china_recoveries = []
    italy_recoveries = []
    us_recoveries = []
    spain_recoveries = []
    france_recoveries = []
    germany_recoveries = []
    uk_recoveries = []
    russia_recoveries = []
    brazil_recoveries = []
    india_recoveries = []

    for i in dates:
        confirmed_sum = confirmed[i].sum()
        death_sum = deaths[i].sum()
        recovered_sum = recoveries[i].sum()

        world_cases.append(confirmed_sum)
        total_deaths.append(death_sum)
        total_recovered.append(recovered_sum)
        total_active.append(confirmed_sum-death_sum-recovered_sum)

        mortality_rate.append(death_sum/confirmed_sum)
        recovery_rate.append(recovered_sum/confirmed_sum)

        china_cases.append(confirmed_cases[confirmed_cases['Country/Region']=='China'][i].sum())
        italy_cases.append(confirmed_cases[confirmed_cases['Country/Region']=='Italy'][i].sum())
        us_cases.append(confirmed_cases[confirmed_cases['Country/Region']=='US'][i].sum())
        spain_cases.append(confirmed_cases[confirmed_cases['Country/Region']=='Spain'][i].sum())
        france_cases.append(confirmed_cases[confirmed_cases['Country/Region']=='France'][i].sum())
        germany_cases.append(confirmed_cases[confirmed_cases['Country/Region']=='Germany'][i].sum())
        uk_cases.append(confirmed_cases[confirmed_cases['Country/Region']=='United Kingdom'][i].sum())
        russia_cases.append(confirmed_cases[confirmed_cases['Country/Region']=='Russia'][i].sum())
        brazil_cases.append(confirmed_cases[confirmed_cases['Country/Region']=='Brazil'][i].sum())
        india_cases.append(confirmed_cases[confirmed_cases['Country/Region']=='India'][i].sum())

        china_deaths.append(confirmed_deaths[confirmed_deaths['Country/Region']=='China'][i].sum())
        italy_deaths.append(confirmed_deaths[confirmed_deaths['Country/Region']=='Italy'][i].sum())
        us_deaths.append(confirmed_deaths[confirmed_deaths['Country/Region']=='US'][i].sum())
        spain_deaths.append(confirmed_deaths[confirmed_deaths['Country/Region']=='Spain'][i].sum())
        france_deaths.append(confirmed_deaths[confirmed_deaths['Country/Region']=='France'][i].sum())
        germany_deaths.append(confirmed_deaths[confirmed_deaths['Country/Region']=='Germany'][i].sum())
        uk_deaths.append(confirmed_deaths[confirmed_deaths['Country/Region']=='United Kingdom'][i].sum())
        russia_deaths.append(confirmed_deaths[confirmed_deaths['Country/Region']=='Russia'][i].sum())
        brazil_deaths.append(confirmed_deaths[confirmed_deaths['Country/Region']=='Brazil'][i].sum())
        india_deaths.append(confirmed_deaths[confirmed_deaths['Country/Region']=='India'][i].sum())

        china_recoveries.append(confirmed_recoveries[confirmed_recoveries['Country/Region']=='China'][i].sum())
        italy_recoveries.append(confirmed_recoveries[confirmed_recoveries['Country/Region']=='Italy'][i].sum())
        us_recoveries.append(confirmed_recoveries[confirmed_recoveries['Country/Region']=='US'][i].sum())
        spain_recoveries.append(confirmed_recoveries[confirmed_recoveries['Country/Region']=='Spain'][i].sum())
        france_recoveries.append(confirmed_recoveries[confirmed_recoveries['Country/Region']=='France'][i].sum())
        germany_recoveries.append(confirmed_recoveries[confirmed_recoveries['Country/Region']=='Germany'][i].sum())
        uk_recoveries.append(confirmed_recoveries[confirmed_recoveries['Country/Region']=='United Kingdom'][i].sum())
        russia_recoveries.append(confirmed_recoveries[confirmed_recoveries['Country/Region']=='Russia'][i].sum())
        brazil_recoveries.append(confirmed_recoveries[confirmed_recoveries['Country/Region']=='Brazil'][i].sum())
        india_recoveries.append(confirmed_recoveries[confirmed_recoveries['Country/Region']=='India'][i].sum())

    def daily_increase(data):
        d = []
        for i in range(len(data)):
            if i == 0:
                d.append(data[0])
            else:
                d.append(data[i]-data[i-1])
        return d

    world_daily_increase = daily_increase(world_cases)
    china_daily_increase = daily_increase(china_cases)
    italy_daily_increase = daily_increase(italy_cases)
    us_daily_increase = daily_increase(us_cases)
    spain_daily_increase = daily_increase(spain_cases)
    france_daily_increase = daily_increase(france_cases)
    germany_daily_increase = daily_increase(germany_cases)
    uk_daily_increase = daily_increase(uk_cases)
    russia_daily_increase = daily_increase(russia_cases)
    brazil_daily_increase = daily_increase(brazil_cases)
    india_daily_increase = daily_increase(india_cases)

    world_daily_death = daily_increase(total_deaths)
    china_daily_death = daily_increase(china_deaths)
    italy_daily_death = daily_increase(italy_deaths)
    us_daily_death = daily_increase(us_deaths)
    spain_daily_death = daily_increase(spain_deaths)
    france_daily_death = daily_increase(france_deaths)
    germany_daily_death = daily_increase(germany_deaths)
    uk_daily_death = daily_increase(uk_deaths)
    russia_daily_death = daily_increase(russia_deaths)
    brazil_daily_death = daily_increase(brazil_deaths)
    india_daily_death = daily_increase(india_deaths)

    world_daily_recovery = daily_increase(total_recovered)
    china_daily_recovery = daily_increase(china_recoveries)
    italy_daily_recovery = daily_increase(italy_recoveries)
    us_daily_recovery = daily_increase(us_recoveries)
    spain_daily_recovery = daily_increase(spain_recoveries)
    france_daily_recovery = daily_increase(france_recoveries)
    germany_daily_recovery = daily_increase(germany_recoveries)
    uk_daily_recovery = daily_increase(uk_recoveries)
    russia_daily_recovery = daily_increase(russia_recoveries)
    brazil_daily_recovery = daily_increase(brazil_recoveries)
    india_daily_recovery = daily_increase(india_recoveries)

    unique_countries = list(coronavirus_data['Country_Region'].unique())

    country_confirmed_cases = []
    country_death_cases = []
    country_active_cases = []
    country_recovery_cases = []
    country_mortality_rate = []
    no_cases = []

    for i in unique_countries:
        cases = coronavirus_data[coronavirus_data['Country_Region']==i]['Confirmed'].sum()
        if cases > 0:
            country_confirmed_cases.append(cases)
        else:
            no_cases.append(i)

    for i in no_cases:
        unique_countries.remove(i)

    unique_countries = [k for k, v in sorted(zip(unique_countries, country_confirmed_cases), key=operator.itemgetter(1), reverse=True)]
    for i in range(len(unique_countries)):
        country_confirmed_cases[i] = coronavirus_data[coronavirus_data['Country_Region']==unique_countries[i]]['Confirmed'].sum()
        country_death_cases.append(coronavirus_data[coronavirus_data['Country_Region']==unique_countries[i]]['Deaths'].sum())
        country_recovery_cases.append(coronavirus_data[coronavirus_data['Country_Region']==unique_countries[i]]['Recovered'].sum())
        country_active_cases.append(coronavirus_data[coronavirus_data['Country_Region']==unique_countries[i]]['Active'].sum())
        country_mortality_rate.append(country_death_cases[i]/country_confirmed_cases[i])

    country_df = pd.DataFrame({'Country Name': unique_countries, 'Number of Confirmed Cases': country_confirmed_cases,
                               'Number of Deaths': country_death_cases, 'Number of Recoveries': country_recovery_cases,
                               'Number of Active Cases': country_active_cases, 'Mortality Rate': country_mortality_rate})

    country_df.style.background_gradient(cmap='Blues')

    unique_provinces = list(coronavirus_data['Province_State'].unique())