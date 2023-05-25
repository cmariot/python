import pandas
from FileLoader import FileLoader


def youngest_fellah(pandas_dataframe: 'pandas.DataFrame', olympic_year: int):

    if not isinstance(pandas_dataframe, pandas.DataFrame):
        raise TypeError("pandas_dataframe must be a pandas.DataFrame")
    if not isinstance(olympic_year, int):
        raise TypeError("olympic_year must be an integer")

    youngest_man = None
    youngest_woman = None

    try:

        dataframe_by_date = pandas_dataframe.loc[pandas_dataframe['Year'] == olympic_year]
        if dataframe_by_date.empty:
            raise ValueError("No data for this year")

        men_by_date = dataframe_by_date.loc[dataframe_by_date['Sex'] == 'M']
        women_by_date = dataframe_by_date.loc[dataframe_by_date['Sex'] == 'F']

        return {
            'f': youngest_woman,
            'm': youngest_man
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
