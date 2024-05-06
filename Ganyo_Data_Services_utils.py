''' Ganyo P1 Data Fundamentals
This module provides a reusable byline for the Ganyo Data Solutions, LLC. '''

# 2. Import Dependencies-Anything in the standard library is fair game.
import math
import statistics

# 7. Define Main Function-we can call to test our code and display all information.
def main():

#3. Define Variables of Different Types-at least one variable of each of these types
# str, int, float, bool, list of strings, list of numbers.
    
    company_name: str = "Ganyo Data Solutions, LLC"
    count_active_projects: 7
    company_founded_year: int = 2023
    has_international_presence: bool = True
    average_satisfation_score: float = 4.19
    services_offered: list = ["Data Analysis", "Machine Learning Consultation", "Education Data Solutions", "Farm & Ag Business Intelligence Solutions"]
    satisfaction_scores: list = [4.8, 4.9, 4.9, 5.0, 4.7, 4.8, 4.7, 4.9, 4.7]
    
# 4. Define Formatted Strings-create formatted strings for non-string variables.

    company_name_string: str = f'Company Name: {company_name}'
    company_year_string: str = f'Company Founded: {company_founded_year}'
    company_works_string: str = f'Accepts International Clients: {has_international_presence}'
    company_client_satisfaction: str = f'Client Satisfaction: {average_satisfation_score}'
    services_string: str = f'Services Offered: {services_offered}'
    active_projects_string: str = f'Active Projects: {count_active_projects}'

#5. Calculate Descriptive Statistics-min(), max(), len(), mean(), mode(), median(),
  # and stdev()
    smallest = min(satisfaction_scores)
    largest = max(satisfaction_scores)
    total = sum(satisfaction_scores)
    count = len(satisfaction_scores)
    mean = statistics.mean(satisfaction_scores)
    mode = statistics.mode(satisfaction_scores)
    median = statistics.median(satisfaction_scores)
    standard_deviation = statistics.stdev(satisfaction_scores)

    stats_string: str = f"""Client Satisfaction Data:
    Lowest rating: {smallest},
    Highest rating: {largest},
    Total: {total},
    Number surveyed: {count},
    Average: {mean},
    Most recurring score: {mode},
    Middle score: {median},
    Amount of Variance: {standard_deviation}
    """

#Create a multiline byline for business
    byline: str= f"""
        Company {company_name}
        Current Projects: {count_active_projects}
        International: {has_international_presence}
        Client Satisfaction: {average_client_satisfaction}
        Service: {services_offered}
        The Numbers: f"{stats_string}"
        """
    print(byline)
''' Ganyo P1 Data Fundamentals
This module provides a reusable byline for the Ganyo Data Solutions, LLC. '''

# 2. Import Dependencies-Anything in the standard library is fair game.
import math
import statistics

# 7. Define Main Function-we can call to test our code and display all information.
def main():

#3. Define Variables of Different Types-at least one variable of each of these types
# str, int, float, bool, list of strings, list of numbers.

    company_name: str = "Ganyo Data Solutions, LLC"
    count_active_projects: 7
    company_founded_year: int = 2023
    has_international_presence: bool = True
    average_satisfation_score: float = 4.19
    services_offered: list = ["Data Analysis", "Machine Learning Consultation", "Education Data Solutions", "Farm & Ag Business Intelligence Solutions"]
    satisfaction_scores: list = [4.8, 4.9, 4.9, 5.0, 4.7, 4.8, 4.7, 4.9, 4.7]
    
# 4. Define Formatted Strings-create formatted strings for non-string variables.

    company_name_string: str = f"Company Name: {company_name}"
    company_year_string: str = f"Company Founded: {company_founded_year}"
    company_works_string: str = f"Accepts International Clients: {has_international_presence}"
    company_client_satisfaction: str = f"Client Satisfaction: {average_client_score}"
    services_string: str = f"Services Offered: {services_offered}"
    active_projects_string: str = f"Active Projects: {count_active_projects}"

#5. Calculate Descriptive Statistics-min(), max(), len(), mean(), mode(), median(),
  # and stdev()
    smallest = min(satisfaction_scores)
    largest = max(satisfaction_scores)
    total = sum(satisfaction_scores)
    count = len(satisfaction_scores)
    mean = statistics.mean(satisfaction_scores)
    mode = statistics.mode(satisfaction_scores)
    median = statistics.median(satisfaction_scores)
    standard_deviation = statistics.stdev(satisfaction_scores)

    stats_string: str = f"""Client Satisfaction Scores:
    Lowest rating: {smallest},
    Highest rating: {largest},
    Total: {total},
    Number surveyed: {count},
    Average: {mean},
    Most recurring score: {mode},
    Middle score: {median},
    Amount of Variance: {standard_deviation}
    """

#Create a multiline byline for business
    byline: str = f"""
    Company: {company_name}
    Current Projects: {count_active_projects}
    International: {has_international_presence}
    Client Satisfaction: {average_client_satisfaction}
    Service: {services_offered}
    The Numbers: f"{stats_string}""
    """
    print(byline)
    
# Call the main function to execute the code
if __name__ == '__main__':
    main()
