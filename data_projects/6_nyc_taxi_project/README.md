# NYC Taxi Trip Duration Analysis

A small, structured Python data project that demonstrates how to:
- Load and clean raw data
- Perform simple feature engineering
- Generate summary statistics
- Visualize results
- Organize production-ready code, configs, and tests

---

## Project Structure

```bash
nyc_taxi_project/
├── data/
│   └── nyc_taxi_sample.csv          # Sample dataset (3 example taxi trips)
├── notebooks/
│   └── exploratory_analysis.ipynb   # Notebook for ad hoc exploration
├── src/
│   ├── __init__.py
│   ├── config.py                    # Central config (paths, constants)
│   ├── data_loader.py               # Data loading logic
│   ├── feature_engineering.py       # Feature engineering logic
│   ├── analysis.py                  # Summary stats
│   └── visualization.py             # Plotting logic
├── tests/
│   └── test_data_loader.py          # Example test
├── main.py                          # Entry point to run the analysis
├── requirements.txt                 # Python dependencies
└── README.md                        # Project overview (this file)
```