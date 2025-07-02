# Import the functions from our other scripts
from get_data import get_pokemon_data, save_data
from clean_data import clean_pokemon_data
from feature_engineering import create_features
from create_plots import create_and_save_plots


def run_pipeline():
    """
    Executes the entire Pokémon data analysis pipeline.
    """
    print("=============================================")
    print("=== STARTING POKEMON DATA ANALYSIS PIPELINE ===")
    print("=============================================\n")

    #  Step 1: Get Data
    print(" Step 1: Fetching Data from PokéAPI ")
    raw_df = get_pokemon_data(num_pokemon=151)
    if raw_df is not None:
        save_data(raw_df, folder="data", filename="raw_pokemon_data.csv")
        print(" Step 1 Complete \n")
    else:
        print("Failed to fetch data. Aborting pipeline.")
        return

    #  Step 2: Clean Data
    print(" Step 2: Cleaning Raw Data ")
    cleaned_df = clean_pokemon_data(
        input_path="data/raw_pokemon_data.csv",
        output_path="data/cleaned_pokemon_data.csv"
    )
    if cleaned_df is not None:
        print(" Step 2 Complete \n")
    else:
        print("Failed to clean data. Aborting pipeline.")
        return

    #  Step 3: Feature Engineering
    print(" Step 3: Engineering New Features ")
    featured_df = create_features(
        input_path="data/cleaned_pokemon_data.csv",
        output_path="data/featured_pokemon_data.csv"
    )
    if featured_df is not None:
        print(" Step 3 Complete \n")
    else:
        print("Failed to engineer features. Aborting pipeline.")
        return

    #  Step 4: Create Plots
    print(" Step 4: Generating Visualizations ")
    create_and_save_plots(
        input_path="data/featured_pokemon_data.csv",
        output_folder="plots"
    )
    print(" Step 4 Complete \n")

    print("======================================")
    print("=== PIPELINE EXECUTION FINISHED! ===")
    print("======================================")
    print("Check the 'data' folder for CSV files and the 'plots' folder for HTML graphs.")  # noqa:ignore


if __name__ == "__main__":
    run_pipeline()
