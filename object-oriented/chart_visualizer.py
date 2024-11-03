import pandas as pd
import plotly.express as px
from utils import reverse_dictionary

class ChartVisualizer:
    """
    Class for visualizing demographic indicators with bar charts.

    Attributes:
        scores (dict): A dictionary containing scores from an indicator.
        title (str): Title of the chart.
        label (str): Label for the Y-axis.
        department_mapping (dict): A mapping of regions to their respective departments.

    Methods:
        create_bar_chart(): Generates a bar chart for the demographic indicators.
    """

    def __init__(self, scores, title, label, country):
        self.scores = scores  # Expecting a dictionary for the demographic data
        self.title = title  # Title for the chart
        self.label = label  # Label for the Y-axis
        self.country = country

    def create_bar_chart(self):
        """Generates a bar chart for the indicator."""
        # Prepare the DataFrame
        df = pd.DataFrame({
            'Ville': list(self.scores.keys()),
            self.label: list(self.scores.values()),  # Use the label attribute
        })

        # Create the bar chart
        fig = px.bar(
            df,
            x='Ville',
            y=self.label,  # Use the label attribute for the Y-axis
            labels={'Ville': 'Ville', self.label: "Nombre d'agences"},  # Adjust based on the label
            title=self.title,
            hover_data={'Ville': True},  # Show department on hover
            color_discrete_sequence=["#4C78A8"]  # Unique color for all bars (blue)
        )

        # Update layout
        fig.update_layout(
            xaxis_title="Ville",
            yaxis_title="Nombre d'agences" # Use the label for the Y-axis title
        )

        # Save as HTML
        html_file_path = f'/Users/haouabenaliabbo/Desktop/M2 IREN/ALTERNANCE/GitHub/Dashboard/{self.label}_{self.country}.html'

        # Save the map as HTML
        fig.write_html(html_file_path)

        print(f"Chart generated and saved")
