from pandas import DataFrame, plotting, read_csv
from matplotlib import pyplot as plt
import unittest


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
            if df[feature].dtype not in ['int64', 'float64']:
                raise Exception("Error, feature is not numerical")

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


class TestMyPlotLib(unittest.TestCase):

    def setUp(self):
        self.myplotlib = MyPlotLib()
        self.df = DataFrame({'A': [1, 2, 3],
                             'B': [4, 5, 6],
                             'C': [7, 8, 9],
                             'D': ["a", "b", "c"]})

    def test_histogram(self):
        self.assertIsNone(self.myplotlib.histogram(self.df, ['A', 'B']))

    def test_density(self):
        self.assertIsNone(self.myplotlib.density(self.df, ['A', 'B']))

    def test_pair_plot(self):
        self.assertIsNone(self.myplotlib.pair_plot(self.df, ['A', 'B']))

    def test_box_plot(self):
        self.assertIsNone(self.myplotlib.box_plot(self.df, ['A', 'B']))

    def test_histogram_invalid_df(self):
        with self.assertRaises(Exception) as context:
            self.myplotlib.histogram(1, ['A', 'B'])
        self.assertTrue("Error, dataframe is not a pandas.DataFrame"
                        in str(context.exception))

    def test_histogram_invalid_features(self):
        with self.assertRaises(Exception) as context:
            self.myplotlib.histogram(self.df, 1)
        self.assertTrue("Error, features is not a list"
                        in str(context.exception))

    def test_histogram_invalid_feature(self):
        with self.assertRaises(Exception) as context:
            self.myplotlib.histogram(self.df, [1])
        self.assertTrue("Error, feature is not a str"
                        in str(context.exception))

    def test_histogram_feature_not_found(self):
        with self.assertRaises(Exception) as context:
            self.myplotlib.histogram(self.df, ['E'])
        self.assertTrue("Error, feature not found in dataframe"
                        in str(context.exception))

    def test_histogram_feature_not_numerical(self):
        with self.assertRaises(Exception) as context:
            self.myplotlib.histogram(self.df, ['D'])
        self.assertTrue("Error, feature is not numerical"
                        in str(context.exception))


class FileLoader:

    def load(self, path) -> DataFrame:
        """
        takes as an argument the file path of the dataset to load,
        displays a message specifying the dimensions of the dataset
        (e.g. 340 x 500) and returns the dataset loaded as a pandas.DataFrame.
        """
        if not isinstance(path, str):
            print("Path must be a string")
            return DataFrame()
        if not path:
            print("Path must not be empty")
            return DataFrame()
        if not path.endswith('.csv'):
            print("Path must be a .csv file")
            return DataFrame()
        try:
            df = read_csv(path)
            print(
                f"Loading dataset of dimensions {df.shape[0]} x {df.shape[1]}")
            return df
        except FileNotFoundError:
            print("File not found")
            return DataFrame()

    def display(self, df, n=0) -> None:
        """
        takes a pandas.DataFrame and an integer as arguments,
        displays the first n rows of the dataset if n is positive,
        or the last n rows if n is negative.
        """
        if not isinstance(df, DataFrame):
            print("Error: df must be a pandas.DataFrame")
            return
        if not isinstance(n, int):
            print("Error: n must be an integer")
            return
        if n < -df.shape[0] or n > df.shape[0]:
            print(f"Error: n must be between {-df.shape[0]} and {df.shape[0]}")
            return
        if n > 0:
            print(df.head(n))
        elif n < 0:
            print(df.tail(-n))
        else:
            print(df.to_string())


if __name__ == "__main__":

    file_loader = FileLoader()
    myplotlib = MyPlotLib()

    try:
        pandas_dataframe = file_loader.load(
            "../ressources/athlete_events.csv")
        myplotlib.histogram(pandas_dataframe, ['Height', 'Weight'])
        myplotlib.density(pandas_dataframe, ['Weight', 'Height'])
        myplotlib.pair_plot(pandas_dataframe, ['Weight', 'Height'])
        myplotlib.box_plot(pandas_dataframe, ['Weight', 'Height'])

        unittest.main()

    except Exception as error:
        print(error)
        exit(1)
