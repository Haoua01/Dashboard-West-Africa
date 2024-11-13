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

