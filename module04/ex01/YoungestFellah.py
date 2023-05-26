import pandas
from FileLoader import FileLoader


def youngest_fellah(pandas_dataframe: 'pandas.DataFrame', olympic_year: int):
    """
    a function that will return a dictionary containing the age of the
    youngest woman and the youngest man who took part in the Olympics a
    given year.
    """

    if not isinstance(pandas_dataframe, pandas.DataFrame):
        raise TypeError("pandas_dataframe must be a pandas.DataFrame")
    if not isinstance(olympic_year, int):
        raise TypeError("olympic_year must be an integer")

    try:

        def get_min_age(pandas_dataframe, olympic_year, gender):
            filtered_by_year = pandas_dataframe.loc[pandas_dataframe['Year']
                                                    == olympic_year]
            filtered_by_sex = filtered_by_year.loc[filtered_by_year['Sex']
                                                   == gender]
            return filtered_by_sex['Age'].min()

        return {
            'f': get_min_age(pandas_dataframe, olympic_year, 'F'),
            'm': get_min_age(pandas_dataframe, olympic_year, 'M')
        }

    except Exception as error:
        print("Error: {}".format(error))
        exit(1)


if __name__ == "__main__":

    file_loader = FileLoader()

    try:
        pandas_dataframe = file_loader.load("../ressources/athlete_events.csv")
        youngest_dict = youngest_fellah(pandas_dataframe, 2004)
        print(youngest_dict)

    except Exception:
        exit(1)
