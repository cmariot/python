from pandas import DataFrame, read_csv
import unittest
from unittest.mock import patch
from io import StringIO


class FileLoader:

    def load(self, path) -> DataFrame:
        """
        takes as an argument the file path of the dataset to load,
        displays a message specifying the dimensions of the dataset
        (e.g. 340 x 500) and returns the dataset loaded as a pandas.DataFrame.
        """
        if not isinstance(path, str):
            raise TypeError("Path must be a string")
        if not path.endswith('.csv'):
            raise ValueError("Path must be a .csv file")
        if not path:
            raise ValueError("Path must not be empty")
        
        try:
            csv_file = read_csv(path)
            pandas_df = DataFrame(data=csv_file)
            print("Loading dataset of dimensions {} x {}".format(
                pandas_df.shape[0], pandas_df.shape[1]))
            return pandas_df
        except Exception as error:
            print("Error: {}".format(error))
            return DataFrame()

    def display(self, df, n=0) -> None:
        """
        takes a pandas.DataFrame and an integer as arguments,
        displays the first n rows of the dataset if n is positive,
        or the last n rows if n is negative.
        """
        if not isinstance(df, DataFrame):
            raise TypeError("df must be a pandas.DataFrame")
        if not isinstance(n, int):
            raise TypeError("n must be an integer")

        if n > df.shape[0] or n < -df.shape[0]:
            raise ValueError("n must be between {} and {}".format(
                -df.shape[0], df.shape[0]))
        elif n > 0:
            print(df.head(n))
        elif n < 0:
            print(df.tail(-n))
        else:
            print(df)


class TestFileLoader(unittest.TestCase):

    def setUp(self):
        self.loader = FileLoader()

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
        with self.assertRaises(ValueError):
            self.loader.load('test_data.txt')

    def test_display_first_n_rows(self):
        # Test displaying the first n rows of a DataFrame
        df = DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.loader.display(df.head(2))
            self.assertEqual(fake_out.getvalue().strip(),
                             'A  B\n0  1  4\n1  2  5')

    def test_display_last_n_rows(self):
        # Test displaying the last n rows of a DataFrame
        df = DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.loader.display(df.tail(2))
            self.assertEqual(fake_out.getvalue().strip(),
                             'A  B\n1  2  5\n2  3  6')

    def test_display_all_rows(self):
        # Test displaying all rows of a DataFrame
        df = DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.loader.display(df)
            self.assertEqual(fake_out.getvalue().strip(),
                             'A  B\n0  1  4\n1  2  5\n2  3  6')

    def test_display_invalid_df(self):
        # Test displaying rows with an invalid DataFrame
        with self.assertRaises(TypeError):
            self.loader.display('invalid_df')


if __name__ == '__main__':
    unittest.main()
