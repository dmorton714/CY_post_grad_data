import logging
from src import config, data_loader, feature_engineering, analysis, visualization

logging.basicConfig(level=logging.INFO)

def main() -> None:
    df = data_loader.load_data(config.DATA_PATH)
    df = feature_engineering.add_trip_duration(df)
    stats = analysis.compute_summary_stats(df)
    print(stats)
    visualization.plot_trip_duration_histogram(df)

if __name__ == "__main__":
    main()