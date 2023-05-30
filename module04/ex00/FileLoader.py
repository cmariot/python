from pandas import DataFrame, read_csv
from csv import writer
import unittest


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


class TestFileLoader(unittest.TestCase):

    def setUp(self):
        self.loader = FileLoader()
        data = [
            ['A', 'B'],
            [1, 4],
            [2, 5],
            [3, 6]
        ]
        with open('test_data.csv', 'w', newline='') as file:
            w = writer(file)
            w.writerows(data)

    def test_load_valid_csv(self):
        # Test loading a valid CSV file
        df = self.loader.load('test_data.csv')
        self.assertIsInstance(df, DataFrame)
        self.assertEqual(df.shape, (3, 2))

    def test_load_invalid_path(self):
        # Test loading a non-existent file
        df = self.loader.load('nonexistent.csv')
        self.assertEqual(df.shape, (0, 0))

    def test_load_invalid_extension(self):
        # Test loading a file with an invalid extension
        df = self.loader.load('test_data.txt')
        self.assertEqual(df.shape, (0, 0))

    def test_display_valid_df(self):
        # Test displaying a valid DataFrame
        df = DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
        self.loader.display(df, n=2)
        self.loader.display(df, n=-1)
        self.loader.display(df, n=0)

    def test_display_invalid_df(self):
        # Test displaying an invalid DataFrame
        self.loader.display('invalid_df', n=2)

    def test_display_invalid_n(self):
        # Test displaying a DataFrame with an invalid n
        df = DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
        self.loader.display(df, n=4)
        self.loader.display(df, n=-4)
        self.loader.display(df, n='invalid_n')


if __name__ == '__main__':
    # path = "../ressources/athlete_events.csv"

    try:
        # loader = FileLoader()
        # df = loader.load(path)
        # loader.display(df, n=50)

        unittest.main()

    except Exception as e:
        print(e)
