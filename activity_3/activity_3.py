from random import randint
from math import ceil, pow
import pandas as pd
from collections import namedtuple
from activity_1.activity_1 import arithmetic_average

def get_shapiro_wilk_tables():
    file_coefficients = 'activity_3/coefficients.csv'
    file_critical_values = 'activity_3/critical_values.csv'
    
    pd_coefficients = pd.read_csv(file_coefficients)
    pd_critical_values = pd.read_csv(file_critical_values)

    pd_coefficients.set_index('i\\n', inplace=True)
    pd_critical_values.set_index('N', inplace=True)

    pd_coefficients = pd_coefficients.apply(lambda x: x.str.replace(',', '.').astype(float), axis=1)
    pd_critical_values = pd_critical_values.apply(lambda x: x.str.replace(',', '.').astype(float), axis=1)

    return (pd_coefficients, pd_critical_values)


def get_b_shapiro_wilk(values, pd_coefficients):
    result = 0
    len_sample = len(values)

    for i in range(ceil(len_sample / 2)):
        result += (values[len_sample-i-1] - values[i]) * float(pd_coefficients.loc[i+1, str(len_sample)])
    
    return result

def get_s_shapiro_wilk(values):
    mean = arithmetic_average(values)
    
    return sum([(value - mean) ** 2 for value in values])

def get_shapiro_result(pd_critical_values, W_calculated, confidence_level):
    significance_level = str(round(1-confidence_level,2))

    W = float(pd_critical_values.loc[len(sample_sorted), significance_level])

    return ('Rejected' if W_calculated > W else 'Acepted', significance_level)
    

if __name__ == '__main__':
    sample = [1.90642, 2.22488, 2.10288, 1.69742, 1.52229, 
    3.15435, 2.61826, 1.98492, 1.42738, 1.99568]
    confidence_level = 0.95

    pd_coefficients, pd_critical_values = get_shapiro_wilk_tables()
    sample_sorted = sorted(sample)

    s = get_s_shapiro_wilk(sample_sorted)
    b = get_b_shapiro_wilk(sample_sorted, pd_coefficients)
    W_calculated = pow(b,2) / s

    hypothesis_null, significance_level = get_shapiro_result(pd_critical_values, W_calculated, 0.95)

    ShapiroResult = namedtuple('ShapiroResult', ('hypothesis_null','significance_level'))

    print(ShapiroResult(hypothesis_null, significance_level))