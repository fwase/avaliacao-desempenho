from functools import reduce
from scipy.stats import t
from math import sqrt

from activity_1.activity_1 import arithmetic_average, std_dev

Z_VALUE = {0.90: 1.645, 0.95: 1.960, 0.99: 2.576}


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


def mean_zero_test(conf_interval):
    min_value, max_value = conf_interval
    if min_value <= 0 <= max_value:
        return True

    return False


def confidence_interval_unpaired_samples(
    sample_values_a, sample_values_b, confidence_level
):
    mean_sample_a = arithmetic_average(sample_values_a)
    mean_sample_b = arithmetic_average(sample_values_b)
    diff_mean_samples = mean_sample_a - mean_sample_b

    std_dev_sample_a = std_dev(sample_values_a)
    std_dev_sample_b = std_dev(sample_values_b)
    diff_mean_std_dev = sqrt(
        (std_dev_sample_a / mean_sample_a) + (std_dev_sample_b / mean_sample_b)
    )

    numerator_df = (
        (std_dev_sample_a / mean_sample_a) + (std_dev_sample_b / mean_sample_b)
    ) ** 2
    denominator_df_sample_a = (1 / (mean_sample_a - 1)) * (
        (std_dev_sample_a / mean_sample_a) ** 2
    )
    denominator_df_sample_b = (1 / (mean_sample_b - 1)) * (
        (std_dev_sample_b / mean_sample_b) ** 2
    )
    denominator_df = denominator_df_sample_a + denominator_df_sample_b
    degrees_freedom = round((numerator_df / denominator_df) - 2)

    z_value = t.ppf(confidence_level, degrees_freedom)
    min_value = diff_mean_samples - (diff_mean_std_dev * z_value)
    min_value = diff_mean_samples + (diff_mean_std_dev * z_value)

    return (min_value, min_value)


def size_of_sample(mean, std_dev_value, z_value, precision):
    numerator = 100 * std_dev_value * z_value
    denominator = precision * mean

    return (numerator / denominator) ** 2


if __name__ == "__main__":
    values = [-0.04, -0.19, 0.14, -0.09, -0.14, 0.19, 0.04, 0.09]
    print(confidence_interval(values, 0.95))
