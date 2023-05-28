import unittest
from pandas import DataFrame
from FileLoader import FileLoader
from sys import exit


def youngest_fellah(pandas_dataframe: 'DataFrame', olympic_year: int):
    """
    Returns a dictionary containing the minimum age of the youngest female and
    male athletes who participated in the specified Olympic year.

    :param pandas_dataframe: A pandas.DataFrame containing the Olympic
     athlete data.
    :param olympic_year: An integer representing the Olympic year to
     filter by.
    :return: A dictionary containing the minimum age of the youngest
     female and male athletes.
    """

    if not isinstance(pandas_dataframe, DataFrame):
        raise TypeError("pandas_dataframe must be a pandas.DataFrame")
    if not isinstance(olympic_year, int):
        raise TypeError("olympic_year must be an integer")

    try:

        def get_min_age(pandas_dataframe, olympic_year, gender):
            filtered_by_year = pandas_dataframe.loc[pandas_dataframe['Year']
                                                    == olympic_year]
            filtered_by_sex = filtered_by_year.loc[filtered_by_year['Sex']
                                                   == gender]
            if filtered_by_sex.empty:
                return None
            return filtered_by_sex['Age'].min()

        return {
            'f': get_min_age(pandas_dataframe, olympic_year, 'F'),
            'm': get_min_age(pandas_dataframe, olympic_year, 'M')
        }

    except Exception as error:
        print("Error: {}".format(error))
        exit(1)


class TestYoungestFellah(unittest.TestCase):

    def setUp(self):
        self.loader = FileLoader()
        self.df = self.loader.load('../ressources/athlete_events.csv')

    def test_invalid_dataframe_type(self):
        # Test that the function raises a TypeError if the input is not
        #  a pandas.DataFrame
        with self.assertRaises(TypeError):
            youngest_fellah('invalid_df', 2004)  # type: ignore

    def test_invalid_year_type(self):
        # Test that the function raises a TypeError if the year
        # input is not an integer
        with self.assertRaises(TypeError):
            youngest_fellah(self.df, 'invalid_year')  # type: ignore

    def test_valid_output(self):
        # Test that the function returns the correct output for a valid input
        expected_output = {'f': 13.0, 'm': 14.0}
        self.assertEqual(youngest_fellah(self.df, 2004), expected_output)

    def test_invalid_year(self):
        # Test that the function returns an empty dictionary
        # for an invalid year
        self.assertEqual(
            youngest_fellah(self.df, 3000), {'f': None, 'm': None})

    def test_invalid_dataframe(self):
        # Test that the function raises an exception for an invalid
        # DataFrame
        with self.assertRaises(Exception):
            youngest_fellah(None, 2004)  # type: ignore


if __name__ == '__main__':
    unittest.main()
