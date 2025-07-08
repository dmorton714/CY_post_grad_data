import pandas as pd
import plotly.express as px
import plotly.io as pio
import os


def create_and_save_plots(input_path="data/featured_pokemon_data.csv",
                          output_folder="plots",
                          save_files=True,
                          display_in_notebook=False):
    """
    Creates various plots from the featured Pokémon data.
    - Saves them as HTML files if save_files is True.
    - Displays them inline in a notebook if display_in_notebook is True.

    Args:
        input_path (str): Path to the featured data CSV.
        output_folder (str): Directory to save the plot HTML files.
        save_files (bool): If True, saves plots as HTML files.
        display_in_notebook (bool): If True, displays plots directly using fig.show().        # noqa:ignore
    """
    print("Starting plot generation...")
    try:
        df = pd.read_csv(input_path)
        print("Featured data loaded successfully.")
    except FileNotFoundError:
        print(f"Error: The file {input_path} was not found.")
        return

    #  Plot 1: Attack vs. Defense Scatter Plot
    fig1 = px.scatter(
        df,
        x='attack',
        y='defense',
        color='type1',
        hover_data=['name', 'combat_total'],
        title='Attack vs. Defense of Generation 1 Pokémon',
        labels={'attack': 'Attack Stat',
                'defense': 'Defense Stat', 'type1': 'Primary Type'}
    )

    #  Plot 2: Distribution of Primary Types
    type_counts = df['type1'].value_counts()
    fig2 = px.bar(
        x=type_counts.index,
        y=type_counts.values,
        title='Distribution of Primary Pokémon Types',
        labels={'x': 'Pokémon Type', 'y': 'Count'}
    )

    #  Plot 3: Combat Total by Speed Category
    fig3 = px.box(
        df,
        x='speed_category',
        y='combat_total',
        color='speed_category',
        title='Combat Power by Speed Category',
        labels={'speed_category': 'Speed Category',
                'combat_total': 'Total Combat Stats'},
        category_orders={"speed_category": [
            "Slow", "Average", "Fast", "Very Fast"]}
    )

    #  Display or Save the plots
    if display_in_notebook:
        print("Displaying plots in notebook...")
        fig1.show()
        fig2.show()
        fig3.show()

    if save_files:
        # Create the output directory if it doesn't exist
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
        print(f"Saving plot files in '{output_folder}/'")

        plot1_path = os.path.join(output_folder, "attack_vs_defense.html")
        pio.write_html(fig1, file=plot1_path, auto_open=False)
        print(f"- Saved: {plot1_path}")

        plot2_path = os.path.join(output_folder, "type_distribution.html")
        pio.write_html(fig2, file=plot2_path, auto_open=False)
        print(f"- Saved: {plot2_path}")

        plot3_path = os.path.join(output_folder, "combat_total_by_speed.html")
        pio.write_html(fig3, file=plot3_path, auto_open=False)
        print(f"- Saved: {plot3_path}")

    print("\nPlot generation complete.")


if __name__ == "__main__":
    print("Running create_plots.py as a standalone script (saving files).")
    create_and_save_plots(display_in_notebook=False, save_files=True)
