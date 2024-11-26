import pandas as pd
import plotly.express as px


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

    def __init__(self, scores, label, title):
        self.scores = scores  # Expecting a dictionary for the demographic data
        self.label = label  # Label for the Y-axis
        self.title = title  

    def create_bar_chart(self):
        """Generates a bar chart for the indicator."""
        # Prepare the DataFrame
        df = pd.DataFrame({
            "Pays": list(self.scores.keys()),
            self.label: list(self.scores.values()),  # Use the label attribute
        })

        # Create the bar chart
        fig = px.bar(
            df,
            x="Pays",  # Use the title attribute for the X-axis',
            y=self.label,  # Use the label attribute for the Y-axis
            labels={"Pays": "pays", self.label: "agences"},  # Adjust based on the label
            title=f"Nombre d'agences pour {self.title} par pays",
            hover_data={"Pays": True},  # Show department on hover
            color_discrete_sequence=["#4C78A8"]  # Unique color for all bars (blue)
        )

        # Update the hoverlabel style to change the background color
        fig.update_traces(
            marker_line_color='rgb(0,0,0)', 
            marker_line_width=1.5, 
            opacity=0.8,
            hoverlabel=dict(
                bgcolor="rgba(255, 255, 255, 0.7)",  # Set the hover label background color (light white with transparency)
                font_size=14,  # Font size
                font_family="Arial",  # Font family
                font_color="black",  # Font color
                bordercolor="black",  # Border color for the tooltip
            )
        )
        # Update layout
        fig.update_layout(
            # Use the title attribute for the X-axis and set the first letter to uppercase
            xaxis_title="Pays",
            yaxis_title=f"Nombre d'agences pour {self.title}", # Use the label for the Y-axis title
            dragmode=False,  # Disable all drag interactions (no pan)
            modebar=dict(remove=['zoom', 'pan', 'resetScale', 'lasso2d', 'select2d', 'zoomIn', 'zoomOut', 'autoScale2d', 'resetGeo', 'hoverClosestCartesian']),  # You can specify which tools to remove
            )

        # Save as HTML
        html_file_path = f'/Users/haouabenaliabbo/Desktop/M2 IREN/ALTERNANCE/GitHub/Dashboard-West-Africa/docs/results/{self.label}_pays.html'

        # Save the map as HTML
        fig.write_html(html_file_path)

        print(f"Chart generated and saved")
