from pandas import DataFrame, plotting
from FileLoader import FileLoader
from matplotlib import pyplot as plt


class MyPlotLib:

    def __check_args(self, df: DataFrame, features: list) -> None:
        """
        Check if the dataframe and the features are valid
        """
        if not isinstance(df, DataFrame):
            raise Exception("Error, dataframe is not a pandas.DataFrame")
        if not isinstance(features, list):
            raise Exception("Error, features is not a list")
        for feature in features:
            if not isinstance(feature, str):
                raise Exception("Error, feature is not a str")
            if feature not in df.columns:
                raise Exception("Error, feature not found in dataframe")

    def histogram(self, data: DataFrame, features: list) -> None:
        """
        Plots one histogram for each numerical feature in the list
        """
        self.__check_args(data, features)
        data.hist(column=features)
        plt.show()

    def density(self, df: DataFrame, features: list) -> None:
        """
        Plots the density curve of each numerical feature in the list
        """
        self.__check_args(df, features)
        df.plot.density(y=features)
        plt.show()

    def pair_plot(self, df: DataFrame, features: list) -> None:
        """
        Plots a matrix of subplots (also called scatter plot matrix).
        On each subplot shows a scatter plot of one numerical variable against
        another one.
        The main diagonal of this matrix shows simple histograms.
        """
        self.__check_args(df, features)
        plotting.scatter_matrix(df[features], diagonal='hist')
        plt.show()

    def box_plot(self, df: DataFrame, features: list) -> None:
        """
        Displays a box plot for each features.
        """
        self.__check_args(df, features)
        df.boxplot(column=features)
        plt.show()


if __name__ == "__main__":

    file_loader = FileLoader()
    myplotlib = MyPlotLib()

    try:
        pandas_dataframe = file_loader.load(
            "/Users/cmariot/42/python/module04/ressources/athlete_events.csv")
        myplotlib.histogram(pandas_dataframe, ['Height', 'Weight'])
        myplotlib.density(pandas_dataframe, ['Weight', 'Height'])
        myplotlib.pair_plot(pandas_dataframe, ['Weight', 'Height'])
        myplotlib.box_plot(pandas_dataframe, ['Weight', 'Height'])

    except Exception as error:
        print(error)
        exit(1)
