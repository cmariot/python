from FileLoader import FileLoader
from pandas import DataFrame


class SpatioTemporalData:

    def __init__(self, dataframe: DataFrame):
        if not isinstance(dataframe, DataFrame):
            raise Exception("Error, dataframe is not a pandas.DataFrame")
        self.dataframe = dataframe

    def when(self, location: str):
        """
        The function returns a list of the years where games were held
        in the given location.
        """
        if not isinstance(location, str):
            print("Error, invalid location, must be a str")

        filtered_by_location = self.dataframe[
            self.dataframe['City'] == location
        ]
        return filtered_by_location['Year'].drop_duplicates().tolist()

    def where(self, date: int):
        """
        The function returns a list of the cities where games were held
        during the given year.
        """
        if not isinstance(date, int):
            print("Invalid 'date' format, must be an int")

        filtered_by_date = self.dataframe[
            self.dataframe['Year'] == date
        ]
        return filtered_by_date['City'].drop_duplicates().tolist()


if __name__ == "__main__":
    file_loader = FileLoader()
    try:
        pandas_dataframe = file_loader.load(
            "/Users/cmariot/42/python/module04/ressources/athlete_events.csv")
        sp = SpatioTemporalData(pandas_dataframe)
        print(sp.where(1896))
        print(sp.where(2016))
        print(sp.when('Athina'))
        print(sp.when('Paris'))

    except Exception as error:
        print(error)
        exit(1)
