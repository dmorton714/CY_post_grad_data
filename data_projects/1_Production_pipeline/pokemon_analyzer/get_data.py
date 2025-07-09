import requests
import pandas as pd
import os
import logging
from tqdm import tqdm


def setup_logging():
    """
    Configures a robust logger to write to a file and the console.
    This function is safe to call multiple times.
    """
    # Create a 'logs' directory if it doesn't exist
    if not os.path.exists('logs'):
        os.makedirs('logs')

    log = logging.getLogger()  # Get the root logger
    log.setLevel(logging.INFO)  # Set the lowest level to capture all messages

    # If handlers are already present, remove them.
    # This ensures we don't add duplicate handlers on subsequent calls.
    if log.hasHandlers():
        log.handlers.clear()

    # Create file handler which logs detailed INFO messages
    fh = logging.FileHandler('logs/data_fetch.log', mode='w')
    fh.setLevel(logging.INFO)
    fh_formatter = logging.Formatter(
        '%(asctime)s - %(levelname)s - %(message)s')
    fh.setFormatter(fh_formatter)
    log.addHandler(fh)

    # Create console handler with a higher log level (WARNING)
    # This keeps the console clean for the progress bar.
    ch = logging.StreamHandler()
    ch.setLevel(logging.WARNING)
    ch_formatter = logging.Formatter('%(levelname)s: %(message)s')
    ch.setFormatter(ch_formatter)
    log.addHandler(ch)


def get_pokemon_data(num_pokemon=151):
    """
    Fetches data for a specified number of Pokémon from the PokéAPI, showing a progress bar.    # noqa:ignore

    Args:
        num_pokemon (int): The number of Pokémon to fetch (defaults to 151).

    Returns:
        pandas.DataFrame: A DataFrame containing the fetched Pokémon data.
                          Returns None if the request fails.
    """
    # Set up logging for this run
    setup_logging()
    logging.info(f"Starting API fetch for {num_pokemon} Pokémon.")

    print("Fetching data... (See 'logs/data_fetch.log' for detailed logs)")  # noqa:ignore
    base_url = "https://pokeapi.co/api/v2/pokemon"
    pokemon_data = []

    # Wrap the range iterator with tqdm to create a progress bar
    for i in tqdm(range(1, num_pokemon + 1), desc="Fetching Pokémon"):
        try:
            response = requests.get(f"{base_url}/{i}")
            response.raise_for_status()
            data = response.json()

            # Extracting relevant information
            pokemon_info = {
                'id': data['id'],
                'name': data['name'],
                'height': data['height'],
                'weight': data['weight'],
                'base_experience': data['base_experience'],
                'type1': data['types'][0]['type']['name'],
                'type2': data['types'][1]['type']['name'] if len(data['types']) > 1 else None,  # noqa:ignore
                'hp': data['stats'][0]['base_stat'],
                'attack': data['stats'][1]['base_stat'],
                'defense': data['stats'][2]['base_stat'],
                'special-attack': data['stats'][3]['base_stat'],
                'special-defense': data['stats'][4]['base_stat'],
                'speed': data['stats'][5]['base_stat'],
                'sprite_url': data['sprites']['front_default']
            }
            pokemon_data.append(pokemon_info)
            logging.info(
                f"Successfully fetched data for #{data['id']} - {data['name']}.")  # noqa:ignore

        except requests.exceptions.RequestException as e:
            logging.error(f"Error fetching data for Pokémon ID {i}: {e}")
            continue

    if not pokemon_data:
        logging.warning("No data was fetched. The final DataFrame is empty.")
        return None

    logging.info(f"Successfully fetched data for {len(pokemon_data)} Pokémon.")
    return pd.DataFrame(pokemon_data)


def save_data(df, folder="data", filename="raw_pokemon_data.csv"):
    """
    Saves a DataFrame to a CSV file.

    Args:
        df (pandas.DataFrame): The DataFrame to save.
        folder (str): The directory to save the file in.
        filename (str): The name of the file.
    """
    if df is None:
        logging.warning("DataFrame is None, skipping save.")
        return

    if not os.path.exists(folder):
        os.makedirs(folder)

    filepath = os.path.join(folder, filename)
    df.to_csv(filepath, index=False)
    print(f"\nData saved successfully to {filepath}")
    logging.info(f"DataFrame saved to {filepath}")


if __name__ == "__main__":
    print("Running get_data.py as a standalone script.")
    raw_data = get_pokemon_data(151)
    if raw_data is not None:
        save_data(raw_data)
