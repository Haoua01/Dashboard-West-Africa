class BankAgencies:
    """
    Class to represent bank agencies data.

    Attributes:
        agency_counts (dict): A dictionary containing the number of agencies per region.
        department_mapping (dict): A dictionary mapping agencies to their respective departments.
        coordinates (dict): A dictionary containing the geographical coordinates of cities.

    Methods:
        get_agency_counts(): Returns a dictionary of agency counts.
        get_department_mapping(): Returns a dictionary of department mappings.
        get_coordinates(): Returns a dictionary of city coordinates.
    """

    def __init__(self, agency_counts, department_mapping, coordinates):
        self.agency_counts = agency_counts
        self.department_mapping = department_mapping
        self.coordinates = coordinates

    def get_agency_counts(self):
        """Returns a dictionary containing the number of agencies per region."""
        return self.agency_counts

    def get_department_mapping(self):
        """Returns the department mapping for regions."""
        return self.department_mapping

    def get_coordinates(self):
        """Returns the geographical coordinates for cities."""
        return self.coordinates
