import pandas as pd
import geopandas as gpd



class Shapefile:

    def __init__(self, filename):
        self.filename = filename
        self.data = gpd.read_file(filename)

    def load_shapefile(self):
        return self.data
    
    def get_commune_coordinates(self):  
        """ Create a dictionary of commune coordinates from the shapefile data. """
        commune_coordinates = {}
        # Loop through the data and get unique ADM3_FR values and their coordinates
        for index, row in self.data.iterrows():
            commune = row['ADM3_FR']
            if commune not in commune_coordinates:
                commune_coordinates[commune] = (row['geometry'].centroid.y, row['geometry'].centroid.x)
        return commune_coordinates

    
    def get_department_mapping(self):
        """ Create a dictionary mapping department to their respective communes. """
        department_mapping = {}
        for index, row in self.data.iterrows():
            department = row['ADM2_FR']
            commune = row['ADM3_FR']
            if department in department_mapping:
                department_mapping[department].append(commune)
            else:
                department_mapping[department] = [commune]

    def get_agency_counts_in_commune(self):
        """ Create a dictionary of agency counts per commune where Branch==1 knowing that the commune is not unique"""
        agency_counts = {}
        for index, row in self.data.iterrows():
            commune = row['ADM3_FR']
            count=row['NUMPOINTS']
            agency_counts[commune] = count
        return agency_counts

