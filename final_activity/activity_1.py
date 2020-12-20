from random import randint
import math
import pandas as pd
import matplotlib.pyplot as plt
from functools import reduce

def arithmetic_average(values):
    return sum(values) / len(values)

def weighted_average(values, weights):
    numerator = sum([value * weight for value, weight  in zip(values, weights)])
    
    return numerator / sum(weights)

def geometric_mean(values):
    mult = reduce(lambda x,y: x * y, values)
    return mult ** (1 / len(values))

def harmonic_mean(values):
    denominator = sum([1 / value for value in values])
    
    return len(values) / denominator

def variance(values):
    mean = arithmetic_average(values)
    numerator = sum([(value - mean) ** 2 for value in values])
    
    return numerator / (len(values) - 1)

def std_dev(values):
    variance_values = variance(values)
    
    return variance_values ** (1/2)

def coefficient_variation(values):
    std_dev_values = std_dev(values)
    mean = arithmetic_average(values)
    
    return (std_dev_values / mean) * 100

def bloxplot(values):
    pd_values = pd.DataFrame(values, columns=['values'])
    
    plt.boxplot(pd_values.values, patch_artist=True)
    plt.title('Boxplot of values')
    plt.xlabel('Values')
    plt.figure(figsize=(12,12))

    plt.show()

if __name__ == "__main__":
    qtd_numbers = 20
    values = [randint(0,1000) for i in range(qtd_numbers)]
    weights = [randint(1,10) for i in range(qtd_numbers)]

    print(arithmetic_average(values))
    print(weighted_average(values, weights))
    print(geometric_mean(values))
    print(harmonic_mean(values))
    print(variance(values))
    print(std_dev(values))
    print(coefficient_variation(values))
    bloxplot(values)