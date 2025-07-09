import pandas as pd
import numpy as np
import os


def create_features(input_path="data/cleaned_pokemon_data.csv",
                    output_path="data/featured_pokemon_data.csv"):
    """
    Engineers new features from the cleaned Pokémon data.
    - Calculates a 'combat_total' stat.
    - Calculates BMI (Body Mass Index).
    - Categorizes Pokémon by speed.

    Args:
        input_path (str): Path to the cleaned data CSV.
        output_path (str): Path to save the featured data CSV.

    Returns:
        pandas.DataFrame: DataFrame with new features.
    """
    print("Starting feature engineering process...")
    try:
        df = pd.read_csv(input_path)
        print("Cleaned data loaded successfully.")
    except FileNotFoundError:
        print(f"Error: The file {input_path} was not found.")
        return None

    #  Feature Engineering Steps

    # 1. Create a 'combat_total' stat
    # This gives a general idea of a Pokémon's overall strength in battle.
    stat_columns = ['hp', 'attack', 'defense',
                    'special-attack', 'special-defense', 'speed']
    df['combat_total'] = df[stat_columns].sum(axis=1)
    print("Created 'combat_total' feature.")

    # 2. Calculate Body Mass Index (BMI)
    # BMI = weight (kg) / (height (m))^2
    # This could be a fun, novel metric. Let's avoid division by zero.
    df['bmi'] = df.apply(
        lambda row: row['weight_kg'] /
        (row['height_m'] ** 2) if row['height_m'] > 0 else 0,
        axis=1
    )
    print("Created 'bmi' feature.")

    # 3. Categorize Pokémon by Speed
    # Create descriptive categories for speed stat.
    speed_bins = [0, 50, 80, 100, np.inf]
    speed_labels = ['Slow', 'Average', 'Fast', 'Very Fast']
    df['speed_category'] = pd.cut(
        df['speed'], bins=speed_bins, labels=speed_labels, right=False)
    print("Created 'speed_category' feature.")

    #  Save Featured Data
    output_folder = os.path.dirname(output_path)
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    df.to_csv(output_path, index=False)
    print(f"Featured data saved successfully to {output_path}")

    return df


if __name__ == "__main__":
    print("Running feature_engineering.py as a standalone script.")
    featured_df = create_features()
    if featured_df is not None:
        print("\nFeatured Data Head (with new columns):")
        print(featured_df[['name', 'combat_total',
              'bmi', 'speed_category']].head())
