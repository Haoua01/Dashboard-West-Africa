from financial_service import FinancialService

class MobileMoneyAgencies(FinancialService):

    """
    Class representing mobile money agencies, inheriting from FinancialService.

    Methods:
        get_service_type(): Returns "Mobile Money" indicating the type of service.
    """
    
    def __init__(self, agency_counts, department_mapping, coordinates):
        super().__init__(agency_counts, department_mapping, coordinates)

    def get_service_type(self):
        return "Mobile Money"
