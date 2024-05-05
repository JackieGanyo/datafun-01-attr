''' This module provides a reusable byline for the Ganyo Data Solutions. '''

import math
import statistics

company_name: str = "Ganyo Data Solutions, LLC"
count_active_projects: int = 2
has_international_presence: bool = False
average_client_satisfaction: float = 4.7
services_offered: list = ["Data Analysis", "Machine Learning Consulting", "Business Intelligence Solutions"]
satisfaction_scores: list = [4.8, 4.6, 4.9, 5.0, 4.7]


smallest= min(satisfaction_scores)
largest= max(satisfaction_scores)
total= sum(satisfaction_scores)
count= len(satisfaction_scores)
mean= statistics.mean(satisfaction_scores)
mode= statistics.mode(satisfaction_scores)
median= statistics.median(satisfaction_scores)
standard_deviation=statistics.stdev(satisfaction_scores)

stats_string: str = f"""
Descriptive Statistics for Our Satisfaction Scores:
Smallest: {smallest},
Largest: {largest},
Total: {total},
Count: {count},
Mean: {mean},
Mode: {mode},
Median: {median},
Standard Deviation: {standard_deviation}
"""

#Create a multiline byline for business
byline: str = f"""
Company: {company_name}
Current Projects: {count_active_projects}
International: {has_international_presence}
Client Satisfaction: {average_client_satisfaction}
Service: {services_offered}
The Numbers: f"{stats_string=}""
"""
def main():
    ''' Display all output'''
    print(company_name)
    print(count_active_projects)
    print(has_international_presence)
    print(average_client_satisfaction)
    print(services_offered)
    print(stats_string)

    # If all of the above works, then the byline should work too:
    print(byline)
    
    """execute the main() function when this script run directly, but NOT if 
    we import it as a module.  use boilerplate code"""

    if __name__ == '__main__':
        main()