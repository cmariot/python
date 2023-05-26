from FileLoader import FileLoader
from pandas import DataFrame


def how_many_medals(dataframe: DataFrame, participant_name: str):
    """
    The function returns a dictionary of dictionaries giving the number
    and type of medals for each year during which the participant won medals.
    The keys of the main dictionary are the Olympic games years.
    In each year's dictionary, the keys are 'G', 'S', 'B' corresponding to
    the type of medals won (gold, silver, bronze).
    The innermost values correspond to the number of medals of a given type won
    for a given year.
    """

    if not isinstance(dataframe, DataFrame):
        print("Error, dataframe is not a pandas.DataFrame")
    elif not isinstance(participant_name, str):
        print("Error, invalid participant_name, must be a str")

    filtered_by_name = dataframe[dataframe['Name'] == participant_name]

    dict = {}
    for index, row in filtered_by_name.iterrows():
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
        dict = how_many_medals(
            pandas_dataframe, 'Kjetil Andr Aamodt')
        print(dict)

    except Exception as error:
        print(error)
        exit(1)
