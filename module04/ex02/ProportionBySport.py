import unittest
from pandas import DataFrame
from FileLoader import FileLoader


def proportion_by_sport(dataframe: DataFrame,
                        olympic_year: int,
                        sport: str,
                        gender: str):
    """
    The function returns a float corresponding to the proportion (percentage)
    of particiants who played the given sport among the
    participants of the given gender.

    Answer the question : "What was the percentage of female basketball players
    among all the female participants of the 2016 Olympics?"
    """

    if not isinstance(dataframe, DataFrame):
        raise TypeError("Error, dataframe is not a pandas.DataFrame")
    elif not isinstance(olympic_year, int):
        raise ValueError("Invalid 'olympic_year' format, must be an int")
    elif not isinstance(sport, str):
        raise ValueError("Error, invalid sport, must be a str")
    elif not isinstance(gender, str) or (gender != 'F' and gender != 'M'):
        raise ValueError("Error: Gender must be 'F' or 'M'")

    filtered_by_year = dataframe[dataframe['Year'] == olympic_year]
    unique_athletes = filtered_by_year.drop_duplicates(
            subset=['Name', "Age", "Height", "Weight"]
        )
    filtered_by_gender = unique_athletes[
            unique_athletes['Sex'] == gender
        ]
    filtered_by_sport = filtered_by_gender[
            filtered_by_gender['Sport'] == sport
        ]
    return (filtered_by_sport.shape[0] / filtered_by_gender.shape[0])


class TestProportionBySport(unittest.TestCase):
    def setUp(self):
        loader = FileLoader()
        self.df = loader.load('../ressources/athlete_events.csv')

    def test_invalid_dataframe(self):
        with self.assertRaises(TypeError):
            proportion_by_sport(None, 2016, 'Basketball', 'F')  # type: ignore

    def test_invalid_year(self):
        with self.assertRaises(ValueError):
            proportion_by_sport(
                self.df, '2016', 'Basketball', 'F')  # type: ignore

    def test_invalid_sport(self):
        with self.assertRaises(ValueError):
            proportion_by_sport(self.df, 2016, 123, 'F')  # type: ignore

    def test_invalid_gender(self):
        with self.assertRaises(ValueError):
            proportion_by_sport(self.df, 2016, 'Basketball', 'Female')

    def test_valid_input(self):
        self.assertEqual(proportion_by_sport(
            self.df, 2004, 'Tennis', 'F'), 0.019302325581395347)


if __name__ == '__main__':
    unittest.main()
