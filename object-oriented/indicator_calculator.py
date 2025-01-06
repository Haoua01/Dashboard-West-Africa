import numpy as np

class IndicatorCalculator:
    """
    Class to calculate various indicators, including ISIBF and demographic indicators.

    Attributes:
        agency_counts (dict): A dictionary containing the number of agencies per region.
        neighbors (dict): A dictionary containing distances to neighboring regions.
        population (dict): A dictionary containing the population of each region.
        alpha (float): Parameter for the ISIBF calculation.
        threshold (float): Distance threshold for consideration in calculations.
        department_mapping (dict): A dictionary mapping cities to their respective departments.

    Methods:
        calculate_isibf(): Calculates the ISIBF based on the agency data and distances.
        demographic_indicator(): Calculates the demographic indicator (number of agencies per 10,000 inhabitants).
    """
    
    def __init__(self, agency_counts, neighbors, population, area, department_mapping, alpha=1.01, threshold=200):
        self.agency_counts = agency_counts  # Dictionary containing the number of agencies
        self.neighbors = neighbors  # Dictionary containing distances to neighboring regions
        self.population = population  # Dictionary containing the population of each region
        self.department_mapping = department_mapping  # Mapping from city to department
        self.alpha = alpha  # Parameter for the ISIBF calculation
        self.threshold = threshold  # Distance threshold for the calculation
        self.area = area  # Area of the region

    def calculate_isibf(self):
        """Calculates the ISIBF based on agency counts and neighboring distances."""
        neighbors_contributions = {}
        own_contribution = {}
        isibf_values = {}

        for city in self.agency_counts:
            total = 0
            
            # Calculate contribution from neighbors
            for neighbor, distance in self.neighbors.get(city, {}).items():
                if distance > 0:
                    total += np.log2(self.agency_counts[neighbor] + 1) / self.alpha ** distance
            
            # Calculate own contribution
            own_contribution[city] = np.log2(self.agency_counts[city] + 1)
            neighbors_contributions[city] = total
            
            # Calculate total ISIBF value for the city
            isibf_values[city] = total + own_contribution[city]

        # Map ISIBF values to departments
        isibf_dep = {}
        for city, value in isibf_values.items():
            department = self.department_mapping.get(city)
            if department:  # Check if the department exists
                if department not in isibf_dep:
                    isibf_dep[department] = 0
                isibf_dep[department] += value  # Accumulate values for each department

        return isibf_dep  # Return the department-level ISIBF values
    
    def calculate_isibf2(self):
        """Calculates the ISIBF based on agency counts and neighboring distances."""
        neighbors_contributions = {}
        own_contribution = {}
        isibf_values = {}

        for city in self.agency_counts:
            total = 0
            
            # Calculate contribution from neighbors
            for neighbor, distance in self.neighbors.get(city, {}).items():
                if city=='Soum':
                    print(neighbor, distance)
                if distance > 0:
                    total += np.log2(self.agency_counts[neighbor] + 1) / self.alpha ** distance
            
            # Calculate own contribution
            own_contribution[city] = np.log2(self.agency_counts[city] + 1)
            neighbors_contributions[city] = total
            
            # Calculate total ISIBF value for the city
            isibf_values[city] = total + own_contribution[city]
            if city=='Soum':
                print(own_contribution[city], neighbors_contributions[city], isibf_values[city])
            #print(own_contribution[city], neighbors_contributions[city], isibf_values[city])
            
        return isibf_values  # Return the city-level ISIBF values
    
    def calculate_isibf3(self):
        """Calculates the ISIBF based on agency counts and neighboring distances."""
        neighbors_contributions = {}
        own_contribution = {}
        isibf_values = {}

        for city in self.agency_counts:
            total = 0
            
            # Calculate contribution from neighbors
            for neighbor, distance in self.neighbors.get(city, {}).items():
                if distance > 0:
                    total += np.log2(self.agency_counts[neighbor] + 1) / (self.alpha[neighbor] ** distance)
            
            # Calculate own contribution
            own_contribution[city] = np.log2(self.agency_counts[city] + 1)
            neighbors_contributions[city] = total
            
            # Calculate total ISIBF value for the city
            isibf_values[city] = total + own_contribution[city]
            #print(own_contribution[city], neighbors_contributions[city], isibf_values[city])
            
        return isibf_values


    """
    def demographic_indicator(self,nb_inhabitants):
        Calculates the demographic indicator (number of agencies per 10,000 inhabitants).

        Returns:
            dict: A dictionary with regions as keys and the demographic indicator as values.
        
        demo_indicator = {}
        for city, count in self.agency_counts.items():
            if city in self.population:
                if self.population[city] > 0:  # Avoid division by zero
                    demo_indicator[city] = (count / self.population[city]) * nb_inhabitants  # Agencies per 10,000 inhabitants
                else:
                    demo_indicator[city] = None  # Or handle as you prefer
            else:
                demo_indicator[city] = None  # Or handle as you prefer
        return demo_indicator
    """


    def demographic_indicator_country(self):
        """Calculates the demographic indicator for each country and returns the result per 100,000 inhabitants."""

        total_agencies = sum(self.agency_counts.values())
        return (total_agencies/self.population)*100000






    def geographic_indicator(self):
        """Calculates the geographic indicator (number of agencies per 10,000 km²)."""
        total_agencies = sum(self.agency_counts.values())
        return (total_agencies/self.area)*10000
