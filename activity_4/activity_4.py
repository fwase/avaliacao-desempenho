from random import randint
from math import floor, sqrt

def truncated_mean(values, d_value):
    len_values = len(values)
    summation = sum([value for value in values[d_value:]])

    return (1 / (len_values - d_value)) * summation

def truncated_variance(values, d_value):
    mean = truncated_mean(values, d_value)
    numerator = sum([(value - mean) ** 2 for value in values[d_value:]])
    
    return numerator / (len(values) - 1)

def get_mser_5y_values(values):
    d_values = []
    len_values = len(values)


    for d_value in range(floor(len_values/2)-1):
        variance = truncated_variance(values, d_value)
        denominator = sqrt(len_values - d_value)
        d_values.append((d_value, variance/denominator))

    return d_values


if __name__ == '__main__':
    sample = [47, 26, 86, 70, 84, 100, 72, 15, 78, 31]    

    d_values = get_mser_5y_values(sample)
    d_value_min = sorted(d_values, key=lambda x: x[1])[0]

    print(f'value of d: {d_value_min[0]}')