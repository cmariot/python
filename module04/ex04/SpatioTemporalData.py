from pandas import DataFrame
import unittest


class SpatioTemporalData:

    def __init__(self, dataframe: DataFrame):
        if not isinstance(dataframe, DataFrame):
            raise TypeError("Error, dataframe is not a pandas.DataFrame")
        self.dataframe = dataframe

    def when(self, location: str):
        """
        The function returns a list of the years where games were held
        in the given location.
        """
        if not isinstance(location, str):
            raise TypeError("Error, invalid location, must be a str")
        if location not in self.dataframe['City'].unique():
            raise ValueError("Error, invalid location, not in dataframe")

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
            raise TypeError("Error, invalid date, must be an int")
        if date not in self.dataframe['Year'].unique():
            raise ValueError("Error, invalid date, not in dataframe")

        filtered_by_date = self.dataframe[
            self.dataframe['Year'] == date
        ]
        return filtered_by_date['City'].drop_duplicates().tolist()


class TestSpatioTemporalData(unittest.TestCase):

    def setUp(self):
        # Create a test dataframe
        data = {'Year': [1896, 1896, 1900, 1900, 2016, 2016],
                'Sport': ['Athletics', 'Cycling', 'Athletics',
                          'Cycling', 'Athletics', 'Cycling'],
                'Event': ['Men\'s 100 metres', 'Men\'s Sprint',
                          'Men\'s 100 metres', 'Men\'s Sprint',
                          'Men\'s 100 metres', 'Men\'s Sprint'],
                'City': ['Athina', 'Athina', 'Paris', 'Paris',
                         'Rio de Janeiro', 'Rio de Janeiro'],
                'Country': ['Greece', 'Greece', 'France',
                            'France', 'Brazil', 'Brazil']}
        self.test_dataframe = DataFrame(data)
        self.sp = SpatioTemporalData(self.test_dataframe)

    def test_where(self):
        # Test the where() function with a valid year
        result = self.sp.where(1896)
        expected_result = ['Athina']
        self.assertEqual(result, expected_result)

        # Test the where() function with an invalid year
        with self.assertRaises(TypeError):
            self.sp.where('1896')  # type: ignore

    def test_when(self):
        # Test the when() function with a valid city
        result = self.sp.when('Athina')
        expected_result = [1896]
        self.assertEqual(result, expected_result)

        # Test the when() function with an invalid city
        with self.assertRaises(ValueError):
            self.sp.when('Invalid City')

    def test_invalid_date(self):
        # Test that an invalid date raises a TypeError
        with self.assertRaises(TypeError):
            self.sp.where('1896')  # type: ignore


if __name__ == '__main__':
    unittest.main()