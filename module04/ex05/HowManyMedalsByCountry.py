from FileLoader import FileLoader
from pandas import DataFrame


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
    individual_sports = []
    for sport in dataframe['Sport'].unique():
        if sport not in team_sports:
            individual_sports.append(sport)

    # Filter dataframe by individual sports
    filtered_by_individual = filtered_by_country[
        filtered_by_country['Sport'].isin(individual_sports)]

    # Concatenate filtered_by_individual and filtered_by_team dataframes
    medals = DataFrame.append(filtered_by_individual, filtered_by_team)

    # Sort dataframe by Year
    medals = medals.sort_values(by=['Year'])

    dict = {}
    for index, row in medals.iterrows():
        if row['Year'] not in dict:
            dict[row['Year']] = {'G': 0, 'S': 0, 'B': 0}
        if row['Medal'] == 'Gold':
            dict[row['Year']]['G'] += 1
        elif row['Medal'] == 'Silver':
            dict[row['Year']]['S'] += 1
        elif row['Medal'] == 'Bronze':
            dict[row['Year']]['B'] += 1

    return dict


if __name__ == "__main__":
    file_loader = FileLoader()
    try:
        pandas_dataframe = file_loader.load(
            "/Users/cmariot/42/python/module04/ressources/athlete_events.csv")
        dict = how_many_medals_by_country(
            pandas_dataframe, "France")
        print(dict)

    except Exception as error:
        print(error)
        exit(1)
