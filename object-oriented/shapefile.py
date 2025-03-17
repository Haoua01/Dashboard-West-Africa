import pandas as pd
import geopandas as gpd



class Shapefile:

    def __init__(self, filename):
        self.filename = filename
        self.data = gpd.read_file(filename)

    def load_shapefile(self):
        return self.data
    
    def get_commune_coordinates2(self):  
        """ Create a dictionary of commune coordinates from the shapefile data. """
        countries=self.data['Country'].unique()
        commune_coordinates = {}
        for country in countries:
            commune_coordinates[country] = {}
            commune_countries = self.data[self.data['Country'] == country]
            for index, row in commune_countries.iterrows():
                commune = row['ADM3_FR']
                latitude = row['Latitude']
                longitude = row['Longitude']
                commune_coordinates[country][commune] = (latitude, longitude)
        return commune_coordinates
    
    def get_commune_coordinates(self):  
        """ Create a dictionary of commune coordinates from the shapefile data. """
        commune_coordinates = {}
        for index, row in self.data.iterrows():
            commune = row['ADM3_FR']
            latitude = row['Latitude']
            longitude = row['Longitude']
            commune_coordinates[commune] = (latitude, longitude)
        return commune_coordinates
    
    
    def get_population(self):
        """ Create a dictionary of commune populations from the shapefile data. """
        commune_population = {}
        for index, row in self.data.iterrows():
            commune = row['ADM3_FR']
            population = row['Population']
            commune_population[commune] = population
        return commune_population

    
    def get_department_mapping(self):
        """ Create a dictionary mapping department to their respective communes. """
        department_mapping = {}
        for index, row in self.data.iterrows():
            department = row['Country']
            commune = row['ADM3_FR']
            if department in department_mapping:
                department_mapping[department].append(commune)
            else:
                department_mapping[department] = [commune]

    def get_country_mapping(self):
        """ Create a dictionary mapping country to their respective communes. """
        country_mapping = {}
        
        for index, row in self.data.iterrows():
            country = row['Country']
            commune = row['ADM3_FR']
            
            # Initialize the list if the country key doesn't exist
            if country not in country_mapping:
                country_mapping[country] = []
            
            # Append the commune to the list for the given country
            country_mapping[country].append(commune)
        
        return country_mapping


    def get_agency_counts_in_commune(self, service_type):
        """ Create a dictionary of agency counts per commune where Branch==1 knowing that the commune is not unique"""
        agency_counts = {}
        for index, row in self.data.iterrows():
            commune = row['ADM3_FR']
            if service_type == 'Branch':
                count=row['Total_bran']
            elif service_type == 'ATM':
                count=row['Total_ATMs']
            agency_counts[commune] = count
        return agency_counts

