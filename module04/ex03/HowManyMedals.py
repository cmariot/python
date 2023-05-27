from pandas import DataFrame
import unittest


def how_many_medals(dataframe: DataFrame, participant_name: str):
    """
    The function returns a dictionary of dictionaries giving the number
    and type of medals for each year during which the participant won medals.
    The keys of the main dictionary are the Olympic games years.
    In each year's dictionary, the keys are 'G', 'S', 'B' corresponding to
    the type of medals won (gold, silver, bronze).
    The innermost values correspond to the number of medals of a given type won
    for a given year.
    """

    if not isinstance(dataframe, DataFrame):
        raise TypeError("Error, dataframe is not a pandas.DataFrame")
    elif not isinstance(participant_name, str):
        raise TypeError("Error, invalid participant_name, must be a str")

    filtered_by_name = dataframe[dataframe['Name'] == participant_name]

    filtered_by_name['Medal'] = filtered_by_name['Medal'].replace(
        {'Gold': 'G', 'Silver': 'S', 'Bronze': 'B'}
    )

    dict = {}
    for index, row in filtered_by_name.iterrows():
        year = row['Year']
        medal = row['Medal']
        if year not in dict:
            dict[year] = {'G': 0, 'S': 0, 'B': 0}
        dict[year][medal] += 1
    return dict


class TestHowManyMedals(unittest.TestCase):

    def setUp(self):
        # Create a test dataframe
        data = {'Year': [2000, 2000, 2004, 2004, 2008, 2008],
                'Sport': ['Basketball', 'Basketball', 'Basketball',
                          'Football', 'Football', 'Football'],
                'Event': ['Men\'s Basketball', 'Women\'s Basketball',
                          'Men\'s Basketball', 'Women\'s Football',
                          'Men\'s Football', 'Women\'s Football'],
                'Name': ['Kjetil Andr Aamodt', 'Kjetil Andr Aamodt',
                         'Kjetil Andr Aamodt', 'Kjetil Andr Aamodt',
                         'Kjetil Andr Aamodt', 'Kjetil Andr Aamodt'],
                'Medal': ['Gold', 'Silver', 'Gold', 'Bronze',
                          'Silver', 'Silver']}
        self.test_dataframe = DataFrame(data)

    def test_how_many_medals(self):
        # Test the how_many_medals() function with a valid dataframe
        # and participant name
        result = how_many_medals(self.test_dataframe, 'Kjetil Andr Aamodt')
        expected_result = {2000: {'G': 1, 'S': 1, 'B': 0},
                           2004: {'G': 1, 'S': 0, 'B': 1},
                           2008: {'G': 0, 'S': 2, 'B': 0}}
        self.assertEqual(result, expected_result)

        # Test the how_many_medals() function with an invalid dataframe
        with self.assertRaises(TypeError):
            how_many_medals(
                'invalid_dataframe', 'Kjetil Andr Aamodt')  # type: ignore

        # Test the how_many_medals() function with an invalid participant name
        with self.assertRaises(TypeError):
            how_many_medals(self.test_dataframe, 123)  # type: ignore


if __name__ == '__main__':
    unittest.main()
