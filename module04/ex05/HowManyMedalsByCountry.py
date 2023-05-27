from pandas import DataFrame
import pandas as pd
import unittest


def how_many_medals_by_country(dataframe: DataFrame, country: str):
    """
    Function that returns a dictionary of dictionaries giving the number
    and type of medal for each competition where the country
    delegation earned medals.

    The keys of the main dictionary are the Olympic games years.
    In each year's dictionary, the keys are 'G', 'S', 'B' corresponding to
    the type of medals won (gold, silver, bronze).
    The innermost values correspond to the number of medals of a given type won
    for a given year.
    """

    if not isinstance(dataframe, DataFrame):
        raise Exception("Error, dataframe is not a pandas.DataFrame")
    elif not isinstance(country, str):
        raise Exception("Error, invalid country, must be a str")

    # List of team sports
    team_sports = ['Basketball', 'Football',  'Tug-Of-War', 'Badminton',
                   'Sailing', 'Handball', 'Water Polo', 'Hockey', 'Rowing',
                   'Bobsleigh', 'Softball', 'Volleyball',
                   'Synchronized Swimming', 'Baseball', 'Rugby Sevens',
                   'Rugby', 'Lacrosse', 'Polo']

    # Drop rows with NaN values in 'Medal' column
    dataframe = dataframe.dropna(subset=['Medal'])

    # Filter dataframe by country
    filtered_by_country = dataframe[dataframe['Team'] == country]

    # Filter dataframe by team sports
    filtered_by_team = filtered_by_country[
        filtered_by_country['Sport'].isin(team_sports)]

    # Remove duplicates from filtered_by_team dataframe
    # (keep only one medal per team)
    filtered_by_team = filtered_by_team.drop_duplicates(
        subset=['Year', 'Event', 'Medal'])

    # List of individual sports
    individual_sports = dataframe[
        ~dataframe['Sport'].isin(team_sports)]['Sport'].unique()

    # Filter dataframe by individual sports
    filtered_by_individual = filtered_by_country[
        filtered_by_country['Sport'].isin(individual_sports)]

    # Concatenate filtered_by_individual and filtered_by_team dataframes
    medals = pd.concat([filtered_by_individual, filtered_by_team])

    # Replace values in 'Medal' column by 'G', 'S' or 'B'
    medals['Medal'] = medals['Medal'].replace(
        {'Gold': 'G', 'Silver': 'S', 'Bronze': 'B'})

    # Group medals by year and medal type
    grouped_medals = medals.groupby(
        ['Year', 'Medal']).size().reset_index(name='Count')

    # Create dictionary of dictionaries with number of medals by year
    medal_dict = {}
    for index, row in grouped_medals.iterrows():
        year = row['Year']
        medal_type = row['Medal']
        count = row['Count']
        if year not in medal_dict:
            medal_dict[year] = {'G': 0, 'S': 0, 'B': 0}
        medal_dict[year][medal_type] += count
    return medal_dict


class TestHowManyMedalsByCountry(unittest.TestCase):

    def test_how_many_medals_by_country(self):
        # Create a test dataframe
        data = {'Year': [2000, 2000, 2004, 2004, 2008, 2008],
                'Sport': ['Basketball', 'Basketball', 'Basketball',
                          'Football', 'Football', 'Football'],
                'Event': ['Men\'s Basketball', 'Women\'s Basketball',
                          'Men\'s Basketball', 'Women\'s Football',
                          'Men\'s Football', 'Women\'s Football'],
                'Team': ['France', 'France', 'France', 'France', 'France',
                         'France'],
                'Medal': ['Gold', 'Silver', 'Gold', 'Bronze', 'Silver',
                          'Silver']
                }
        test_dataframe = DataFrame(data)

        # Test the function with the test dataframe and 'France' as the country
        result = how_many_medals_by_country(test_dataframe, 'France')

        # Check that the result is correct
        expected_result = {2000: {'G': 1, 'S': 1, 'B': 0},
                           2004: {'G': 1, 'S': 0, 'B': 1},
                           2008: {'G': 0, 'S': 2, 'B': 0}}
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()