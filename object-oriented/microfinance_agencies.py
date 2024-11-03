from financial_service import FinancialService

class MicrofinanceAgencies(FinancialService):

    """
    Class representing microfinance agencies, inheriting from FinancialService.

    Methods:
        get_service_type(): Returns "Microfinance" indicating the type of service.
    """
    
    def __init__(self, agency_counts, department_mapping, coordinates):
        super().__init__(agency_counts, department_mapping, coordinates)

    def get_service_type(self):
        return "Microfinance"
