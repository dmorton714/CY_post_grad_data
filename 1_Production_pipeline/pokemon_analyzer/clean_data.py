import pandas as pd
import os


def clean_pokemon_data(input_path="data/raw_pokemon_data.csv",
                       output_path="data/cleaned_pokemon_data.csv"):
    """
    Cleans the raw Pokémon data.
    - Fills missing 'type2' values.
    - Converts weight from hectograms to kilograms.
    - Converts height from decimetres to meters.

    Args:
        input_path (str): The path to the raw data CSV file.
        output_path (str): The path to save the cleaned data CSV file.

    Returns:
        pandas.DataFrame: The cleaned DataFrame.
    """
    print("Starting data cleaning process...")
    try:
        df = pd.read_csv(input_path)
        print("Raw data loaded successfully.")
    except FileNotFoundError:
        print(f"Error: The file {input_path} was not found.")
        return None

    # Data Cleaning Steps

    # 1. Handle missing data
    # The 'type2' column has missing values for Pokémon with only one type.
    # We assign the result back to the column to avoid the FutureWarning.
    df['type2'] = df['type2'].fillna('None')
    print("Filled missing 'type2' values.")

    # 2. Convert units for clarity
    # The API provides weight in hectograms and height in decimetres.
    # Let's convert them to more standard units (kg and meters).
    df['weight_kg'] = df['weight'] / 10.0
    df['height_m'] = df['height'] / 10.0
    print("Converted weight to kg and height to meters.")

    # Drop the original columns if desired
    df.drop(['weight', 'height'], axis=1, inplace=True)

    #  Save Cleaned Data
    # It's good practice to save intermediate results
    output_folder = os.path.dirname(output_path)
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    df.to_csv(output_path, index=False)
    print(f"Cleaned data saved successfully to {output_path}")

    return df


if __name__ == "__main__":
    # This allows standalone execution for testing
    print("Running clean_data.py as a standalone script.")
    cleaned_df = clean_pokemon_data()
    if cleaned_df is not None:
        print("\nCleaned Data Head:")
        print(cleaned_df.head())
