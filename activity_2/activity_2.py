from scipy.stats import t
from math import sqrt
from random import randint

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
        ((std_dev_sample_a ** 2) / mean_sample_a) + ((std_dev_sample_b ** 2) / mean_sample_b)
    )

    numerator_df = (
        ((std_dev_sample_a ** 2) / len(sample_values_a)) + ((std_dev_sample_b ** 2) / len(sample_values_b))
    ) ** 2
    denominator_df_sample_a = (1 / (len(sample_values_a) - 1)) * (
        ((std_dev_sample_a ** 2) / len(sample_values_a)) ** 2
    )
    denominator_df_sample_b = (1 / (len(sample_values_b) - 1)) * (
        ((std_dev_sample_b ** 2) / len(sample_values_b)) ** 2
    )
    denominator_df = denominator_df_sample_a + denominator_df_sample_b
    degrees_freedom = round((numerator_df / denominator_df) - 2)
    print(degrees_freedom)

    z_value = t.ppf(confidence_level, degrees_freedom)
    print(z_value)
    min_value = diff_mean_samples - (diff_mean_std_dev * z_value)
    max_value = diff_mean_samples + (diff_mean_std_dev * z_value)

    return (min_value, max_value)


def size_of_sample(mean, std_dev_value, z_value, precision):
    numerator = 100 * std_dev_value * z_value
    denominator = precision * mean

    return (numerator / denominator) ** 2


if __name__ == "__main__":
    sample_a = [randint(0, 100) for _ in range(20)]
    sample_b = [randint(0, 1000) for _ in range(100)]

    ci_samples_a = confidence_interval(sample_a, 0.9)
    ci_samples_b = confidence_interval(sample_b, 0.95)

    print("Confidence interval:")
    print(f"Sample A: {ci_samples_a}")
    print(f"Sample B: {ci_samples_b}")

    zero_test_sample_a = mean_zero_test(ci_samples_a)
    zero_test_sample_b = mean_zero_test(ci_samples_b)

    print("\nMean zero test:")
    print(f"Sample A: {zero_test_sample_a}")
    print(f"Sample B: {zero_test_sample_b}")

    ci_samples_a_and_b = confidence_interval_unpaired_samples(sample_a, sample_b, 0.9)

    print("\nConfidence interval unpaired samples")
    print(f"{ci_samples_a_and_b}")

    mean_sample_a = arithmetic_average(sample_a)
    std_dev_sample_a = std_dev(sample_a)
    z_value_sample_a = Z_VALUE[0.9]
    precision_sample_a = 0.5

    mean_sample_b = arithmetic_average(sample_b)
    std_dev_sample_b = std_dev(sample_b)
    z_value_sample_b = Z_VALUE[0.9]
    precision_sample_b = 0.6

    size_sample_a = size_of_sample(
        mean_sample_a, std_dev_sample_a, z_value_sample_a, precision_sample_a
    )
    size_sample_b = size_of_sample(
        mean_sample_b, std_dev_sample_b, z_value_sample_b, precision_sample_b
    )
    print("\nSimple of samples:")
    print(f"Sample A: {size_sample_a}")
    print(f"Sample B: {size_sample_b}")
