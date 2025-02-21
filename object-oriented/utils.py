def normalize_scores(scores):
    """Normalizes the scores to a range between 0 and 1.

    Args:
        scores (dict): A dictionary of scores with city names as keys.

    Returns:
        dict: A dictionary of normalized scores.
    """
    min_score = min(scores.values())
    max_score = max(scores.values())
    return {city: (score - min_score) / (max_score - min_score) for city, score in scores.items()}

def format_scores(scores):
    """Formats the scores to display them in a user-friendly way.

    Args:
        scores (dict): A dictionary of scores with city names as keys.

    Returns:
        dict: A dictionary with city names as keys and formatted scores as values.
    """
    return {city: round(score, 2) for city, score in scores.items()}  # Format scores to two decimal places

def round_scores(scores):
    """Rounds the scores to the nearest integer.

    Args:
        scores (dict): A dictionary of scores with city names as keys.

    Returns:
        dict: A dictionary with city names as keys and rounded scores as values.
    """
    return {city: round(score) for city, score in scores.items()}  # Round scores to the nearest integer


def reverse_dictionary(original_dict):
    """Reverses the keys and values of a given dictionary.

    Args:
        original_dict (dict): The original dictionary to reverse.

    Returns:
        dict: A new dictionary with keys and values swapped.
    """
    return {v: k for k, v in original_dict.items()}

def mean_scores(scores, department_mapping):
    # Calculate the mean ISIBF for each district
    district_isibf_mean = {}

    for district, departments in department_mapping.items():
        # Calculate the mean ISIBF for the district
        total_isibf = sum(scores.get(department, 0) for department in departments)  # Sum ISIBF values of the departments
        mean_isibf = total_isibf / len(departments) if departments else 0  # Compute mean (avoid division by zero)
        district_isibf_mean[district] = mean_isibf

    # Return the mean ISIBF for each district
    return district_isibf_mean

def mean(scores):
    # calculate the mean of all scores of the dictionnary 
    mean = sum(scores.values()) / len(scores) if scores else 0
    # .2f to keep only 2 decimal
    return round(mean, 2)

def alpha_values(scores, min_alpha, max_alpha):
    # calculate the alpha for each country based on scores of integration to infrastructures 
    scores=normalize_scores(scores) # have reverse normalized scores of integration to infrastructures
    scores_normalized = {city: 1-score for city, score in scores.items()}
    # Trouver le min et max des scores normalisés
    min_score = min(scores_normalized.values())
    max_score = max(scores_normalized.values())
    # Dictionary to store the alpha values
    alpha_values = {}
    for city, score in scores_normalized.items():
        # set the minimum of scores_normalized to min_alpha and the maximum to max_alpha
        alpha = min_alpha + score * (max_alpha - min_alpha) 
        alpha_values[city] = alpha

    return alpha_values


    
import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the page to scrape

def get_population_data(country):
    url = f"https://www.citypopulation.de/en/{country}/admin/"

    # Send an HTTP request to get the content of the page
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the table containing the population and area data
    table = soup.find('table', {'class': 'data'})

    # Initialize lists to store data
    regions = []
    populations = []
    areas = []

    # Loop through the table rows (skip header row)
    for row in table.find_all('tr')[1:]:
        cells = row.find_all('td')
        if len(cells) >= 3:
            region_name = cells[0].get_text(strip=True)
            population = cells[1].get_text(strip=True).replace(',', '')  # Remove commas for numerical values
            area = cells[2].get_text(strip=True).replace(',', '')  # Remove commas for numerical values
            
            # Append data to respective lists
            regions.append(region_name)
            populations.append(population)
            areas.append(area)

    # Display the extracted data
    for region, pop, area in zip(regions, populations, areas):
        print(f"Region: {region}, Population: {pop}, Area: {area} km²")


    df = pd.DataFrame({'Region': regions, 'Population': populations, 'Area': areas})

    df.to_csv(f'/Users/haouabenaliabbo/Desktop/M2 IREN/ALTERNANCE/GitHub/Dashboard-West-Africa/object-oriented/data/{country}_population.csv', index=False)


import numpy as np
def log_transform(scores):
    """Applies a log transformation to the scores.

    Args:
        scores (dict): A dictionary of scores with city names as keys.

    Returns:
        dict: A dictionary with city names as keys and log-transformed scores as values.
    """
    return {city: np.log2(score+1e-5) for city, score in scores.items()}