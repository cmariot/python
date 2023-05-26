from FileLoader import FileLoader
from pandas import DataFrame


def proportion_by_sport(dataframe: DataFrame,
                        olympic_year: int,
                        sport: str,
                        gender: str):
    """
    The function returns a float corresponding to the proportion (percentage)
    of particiants who played the given sport among the
    participants of the given gender.

    Answer the question : "What was the percentage of female basketball players
    among all the female participants of the 2016 Olympics?"
    """

    if not isinstance(dataframe, DataFrame):
        print("Error, dataframe is not a pandas.DataFrame")
    elif not isinstance(olympic_year, int):
        print("Invalid 'olympic_year' format, must be an int")
    elif not isinstance(sport, str):
        print("Error, invalid sport, must be a str")
    elif not isinstance(gender, str) or (gender != 'F' and gender != 'M'):
        print("Error: Gender must be 'F' or 'M'")

    filtered_by_year = dataframe[dataframe['Year'] == olympic_year]
    unique_athletes = filtered_by_year.drop_duplicates(
            subset=['Name', "Age", "Height", "Weight"]
        )
    filtered_by_gender = unique_athletes[
            unique_athletes['Sex'] == gender
        ]
    filtered_by_sport = filtered_by_gender[
            filtered_by_gender['Sport'] == sport
        ]
    return (filtered_by_sport.shape[0] / filtered_by_gender.shape[0])


if __name__ == "__main__":
    file_loader = FileLoader()
    try:
        pandas_dataframe = file_loader.load(
            "/Users/cmariot/42/python/module04/ressources/athlete_events.csv")
        prop_by_sport = proportion_by_sport(
            pandas_dataframe, 2004, 'Tennis', 'F')
        print(prop_by_sport)

    except Exception as error:
        print(error)
        exit(1)
