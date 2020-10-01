from functools import reduce
from scipy.stats import t
from math import sqrt

from activity_1.activity_1 import arithmetic_average, std_dev

Z_VALUE = {
    0.90: 1.645,
    0.95: 1.960,
    0.99: 2.576
}

def confidence_interval(sample_values, confidence_level):
    mean = arithmetic_average(sample_values)
    std_dev_val = std_dev(sample_values)
    
    if len(sample_values) > 30:
        z_value = Z_VALUE[confidence_level]
        min_value = mean - ((std_dev_val * z_value) / sqrt(len(sample_values)))
        max_value = mean + ((std_dev_val * z_value) / sqrt(len(sample_values)))
        
        return (min_value, max_value)
    else:
        degrees_freedom = len(sample_values) - 1
        z_value = t.ppf(confidence_level, degrees_freedom)
        min_value = mean - ((std_dev_val * z_value) / sqrt(len(sample_values)))
        max_value = mean + ((std_dev_val * z_value) / sqrt(len(sample_values)))
        
        return (min_value, max_value)

if __name__ == '__main__':
    values = [-0.04,-0.19, 0.14, -0.09, -0.14, 0.19, 0.04, 0.09]
    print(confidence_interval(values, 0.95))