import pandas as pd
import random
import string


def _generate_mixed_numeric(size):
    """Generates a list of mostly integers with some random strings."""
    data = []
    for _ in range(size):
        if random.random() < 0.999:
            data.append(random.randint(0, 10000))
        else:
            data.append(''.join(random.choices(string.ascii_lowercase, k=5)))
    return data


def _generate_boolean_like(size):
    """Generates a list of boolean-like strings and other noise."""
    options = ['True', 'False', 'true', 'false',
               '1', '0', 'yes', 'no', 'N/A', '']
    return [random.choice(options) for _ in range(size)]


def _generate_date_like(size):
    """Generates a list of dates in different formats,
       plus some non-date strings."""
    data = []
    for _ in range(size):
        if random.random() < 0.99:
            year = random.randint(2020, 2024)
            month = random.randint(1, 12)
            day = random.randint(1, 28)
            rand_format = random.choice(['iso', 'us', 'text'])

            if rand_format == 'iso':
                data.append(f"{year}-{month:02d}-{day:02d}")
            elif rand_format == 'us':
                data.append(f"{month:02d}/{day:02d}/{year}")
            else:
                month_abbr = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                              'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'][month-1] # noqa
                data.append(f"{month_abbr} {day}, {year}")
        else:
            data.append("Not a date")
    return data


def _generate_categorical_with_noise(size):
    """Generates categorical data with some random, unique values."""
    categories = ['alpha', 'beta', 'gamma', 'delta', 'epsilon'] * (size // 5)
    for i in range(int(size * 0.01)):
        noise_index = random.randint(0, size - 1)
        categories[noise_index] = f"noise_{i}"
    random.shuffle(categories)
    return categories[:size]


def _generate_mostly_empty(size):
    """Generates a list with a high percentage of missing values."""
    data = []
    for _ in range(size):
        if random.random() < 0.05:
            data.append(random.random() * 100)
        else:
            data.append(None)
    return data

# --- Main Function ---


def create_tricky_csv(num_rows, output_filename='tricky_data.csv'):
    """
    Generates a large CSV file with mixed data types to challenge pandas'
    type inference.

    Args:
        num_rows (int): The number of rows to generate in the CSV file.
        output_filename (str): The name of the file to save the data to.

    Returns:
        pd.DataFrame: The generated DataFrame.
    """
    print(f"Generating a dataset with {num_rows} rows...")

    data = {
        'id': range(num_rows),
        'mixed_numeric': _generate_mixed_numeric(num_rows),
        'boolean_like': _generate_boolean_like(num_rows),
        'date_like': _generate_date_like(num_rows),
        'categorical_noise': _generate_categorical_with_noise(num_rows),
        'mostly_empty': _generate_mostly_empty(num_rows)
    }

    df = pd.DataFrame(data)

    print(f"DataFrame created. Now saving to '{output_filename}'...")
    df.to_csv(output_filename, index=False)
    print("Save complete.")

    return df


if __name__ == '__main__':
    rows_to_generate = 1_000_000
    generated_filename = 'tricky_data_generated.csv'

    print("--- Running script in standalone mode ---")
    generated_df = create_tricky_csv(rows_to_generate, generated_filename)

    print("\n--- Column Preview & Inferred dtypes ---")
    print(generated_df.info())
