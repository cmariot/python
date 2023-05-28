from pandas import DataFrame
from FileLoader import FileLoader
from matplotlib import pyplot as plt
import seaborn as sns
import unittest


class Komparator:

    def __init__(self, dataframe: DataFrame) -> None:
        if not isinstance(dataframe, DataFrame):
            raise Exception("Error, dataframe is not a pandas.DataFrame")
        if dataframe.empty:
            raise Exception("Error, dataframe is empty")
        self.categorical_vars = dataframe.select_dtypes(
            include=['object']).columns
        self.numerical_vars = dataframe.select_dtypes(
            include=['int64', 'float64']).columns
        if len(self.categorical_vars) == 0:
            raise ValueError("Error, dataframe has no categorical variables")
        if len(self.numerical_vars) == 0:
            raise ValueError("Error, dataframe has no numerical variables")
        self.dataframe = dataframe

    def __check_args(self, categorical_var: str, numerical_var: str):
        if not isinstance(categorical_var, str):
            raise TypeError("Error, categorical_var is not a string")
        if categorical_var not in self.categorical_vars:
            raise ValueError(
                "Error, {} not in dataframe".format(categorical_var))
        if isinstance(numerical_var, str):
            if numerical_var not in self.numerical_vars:
                raise ValueError(
                    "Error, {} not in dataframe".format(numerical_var))
        elif isinstance(numerical_var, list):
            if len(numerical_var) == 0:
                raise ValueError("Error, numerical_var is empty")
            for var in numerical_var:
                if not isinstance(var, str):
                    raise TypeError("Error, numerical_var is not a string")
                if var not in self.numerical_vars:
                    raise ValueError(
                        "Error, {} not in dataframe".format(var))
        else:
            raise TypeError("Error, numerical_var is not a string or a list")

    def __get_categorical_numerical_values(
            self, categorical_var: str, numerical_var: str):

        if isinstance(numerical_var, str):

            # create a new dataframe with only the columns we need and drop the
            # rows with NaN values
            df = self.dataframe[[categorical_var, numerical_var]].dropna()
            # get the categories
            categories = list(df[categorical_var].unique())
            # for each category, get the values of the numerical variable
            values = []
            for category in categories:
                values.append(df[df[categorical_var]
                                 == category][numerical_var])
            return categories, values

        else:
            ret_categories = []
            ret_values = []
            for var in numerical_var:
                df = self.dataframe[[categorical_var, var]].dropna()
                categories = list(df[categorical_var].unique())
                values = []
                for category in categories:
                    values.append(df[df[categorical_var] == category][var])
                ret_categories.append(categories)
                ret_values.append(values)
            return ret_categories, ret_values

    def compare_box_plots(
            self, categorical_var: str, numerical_var: str) -> None:
        """
        displays a series of box plots to compare how the distribution of
        the numerical variable changes if we only consider the subpopulation
        which belongs to each category.
        There should be as many box plots as categories.
        For example, with Sex and Height, we would compare the height
        distributions of men vs. women with two box plots.
        """
        self.__check_args(categorical_var, numerical_var)

        # get the categories and the values of the numerical variable for each
        categories, values = self.__get_categorical_numerical_values(
            categorical_var, numerical_var)

        if isinstance(numerical_var, str):
            # create the boxplot
            plt.boxplot(values, labels=categories)

            # add the title
            plt.title(
                "Comparative boxplot of {} depending on {}".format(
                    numerical_var.lower(), categorical_var.lower())
            )

            # add the y label
            plt.ylabel(numerical_var)

            # add the x label
            plt.xlabel(categorical_var)

            # add the grid as dotted lines
            plt.grid(True, linestyle='dotted')

            # show the figure
            plt.show()

        elif isinstance(numerical_var, list):

            # Create a figure with a subplot for each numerical variable
            fig, axs = plt.subplots(ncols=len(numerical_var))

            # add the title
            fig.suptitle(
                "Comparative boxplots of {} depending on {}".format(
                    ", ".join(numerical_var), categorical_var.lower())
            )

            # for each numerical variable
            for i in range(len(numerical_var)):

                # create the boxplot
                axs[i].boxplot(values[i], labels=categories[i])

                # add the y label
                axs[i].set_ylabel(numerical_var[i])

                # add the x label
                axs[i].set_xlabel(categorical_var)

                # add the grid as dotted lines
                axs[i].grid(True, linestyle='dotted')

            # adjust the space between the subplots
            plt.subplots_adjust(wspace=0.5)

            # show the figure
            plt.show()

    def density(self, categorical_var: str, numerical_var: str) -> None:
        """
        displays the density of the numerical variable.
        Each subpopulation should be represented by a separate curve
        on the graph.
        """

        self.__check_args(categorical_var, numerical_var)

        # get the categories and the values of the numerical variable for each
        categories, values = self.__get_categorical_numerical_values(
            categorical_var, numerical_var)

        if isinstance(numerical_var, str):

            # create the density plot
            for i in range(len(categories)):
                sns.kdeplot(
                    values[i], label=categories[i])

            # add the title
            plt.title(
                "Comparative density plot of {} depending on {}".format(
                    numerical_var.lower(), categorical_var.lower())
            )

            # add the y label : probability density
            plt.ylabel("Probability density")

            # add the x label : the numerical variable
            plt.xlabel(numerical_var)

            # add the grid as dotted lines
            plt.grid(True, linestyle='dotted')

            # add the legend with the categories as labels
            plt.legend(categories)

            # show the figure
            plt.show()

        elif isinstance(numerical_var, list):

            # Create a figure with a subplot for each numerical variable
            fig, axs = plt.subplots(ncols=len(numerical_var))

            # Add a title to the figure
            fig.suptitle(
                "Comparative density plot of {} depending on {}".format(
                    ", ".join(numerical_var), categorical_var.lower())
            )

            # for each numerical variable
            for i in range(len(numerical_var)):
                # create the density plot
                for j in range(len(categories[i])):
                    sns.kdeplot(
                        values[i][j], label=categories[i][j], ax=axs[i])

                # add the y label : probability density
                axs[i].set_ylabel("Probability density")

                # add the x label : the numerical variable
                axs[i].set_xlabel(numerical_var[i])

                # add the grid as dotted lines
                axs[i].grid(True, linestyle='dotted')

                # add the legend with the categories as labels
                axs[i].legend(categories[i])

            # adjust the space between the subplots
            plt.subplots_adjust(wspace=0.5)

            # show the figure
            plt.show()

    def compare_histograms(
            self, categorical_var: str, numerical_var: str) -> None:
        """
        plots the numerical variable in a separate histogram for each category.
        As an extra, you can use overlapping histograms with a color code.
        """
        self.__check_args(categorical_var, numerical_var)

        # get the categories and the values of the numerical variable for each
        categories, values = self.__get_categorical_numerical_values(
            categorical_var, numerical_var)

        if isinstance(numerical_var, str):
            # create the histogram
            plt.hist(values)

            # add the title
            plt.title(
                "Comparative histogram of {} depending on {}".format(
                    numerical_var.lower(), categorical_var.lower())
            )

            # add the y label : number of occurences
            plt.ylabel("Number of occurences")

            # add the x label : the numerical variable
            plt.xlabel(numerical_var)

            # add the grid as dotted lines
            plt.grid(True, linestyle='dotted')

            # add the legend with the categories as labels
            plt.legend(categories)

            # show the figure
            plt.show()

        elif isinstance(numerical_var, list):

            # Create a figure with a subplot for each numerical variable
            fig, axs = plt.subplots(ncols=len(numerical_var))

            # Add a title to the figure
            fig.suptitle(
                "Comparative histogram of {} depending on {}".format(
                    ", ".join(numerical_var), categorical_var.lower())
            )

            # for each numerical variable
            for i in range(len(numerical_var)):
                # create the histogram
                axs[i].hist(values[i])

                # add the y label : number of occurences
                axs[i].set_ylabel("Number of occurences")

                # add the x label : the numerical variable
                axs[i].set_xlabel(numerical_var[i])

                # add the grid as dotted lines
                axs[i].grid(True, linestyle='dotted')

                # add the legend with the categories as labels
                axs[i].legend(categories[i])

            # adjust the space between the subplots
            plt.subplots_adjust(wspace=0.5)

            # show the figure
            plt.show()


class TestKomparator(unittest.TestCase):

    def setUp(self):
        # create a sample dataframe for testing
        data = {'Sex': ['M', 'F', 'F', 'M', 'M', 'F', 'F', 'M', 'F', 'M'],
                'Height': [172, 168, 175, 180, 176, 165, 170, 178, 172, 182],
                'Weight': [70, 56, 64, 80, 72, 55, 60, 75, 68, 85]}
        self.df = DataFrame(data)

        # create a Komparator object for testing
        self.komparator = Komparator(self.df)

    def test_init(self):
        # test that the object is initialized correctly
        self.assertIsInstance(self.komparator, Komparator)
        self.assertIsInstance(self.komparator.dataframe, DataFrame)
        self.assertEqual(self.komparator.categorical_vars.tolist(), ['Sex'])
        self.assertEqual(
            self.komparator.numerical_vars.tolist(), ['Height', 'Weight'])

    def test_init_with_invalid_dataframe(self):
        # test that the constructor raises an exception for invalid dataframes
        with self.assertRaises(Exception):
            Komparator('invalid dataframe')

    def test_init_with_empty_dataframe(self):
        # test that the constructor raises an exception for empty dataframes
        with self.assertRaises(Exception):
            Komparator(DataFrame())

    def test_init_with_missing_categorical_var(self):
        # test that the constructor raises an exception for
        # missing categorical variables
        with self.assertRaises(ValueError):
            Komparator(self.df.drop('Sex', axis=1))

    def test_init_with_missing_numerical_var(self):
        # test that the constructor raises an exception for
        # missing numerical variables
        with self.assertRaises(ValueError):
            Komparator(self.df.drop(['Height', 'Weight'], axis=1))

    def test_compare_box_plots(self):
        # test that the compare_box_plots method generates a plot
        self.assertIsNone(
            self.komparator.compare_box_plots('Sex', ['Height', 'Weight']))

        # test that the method raises an exception for invalid arguments
        with self.assertRaises(TypeError):
            self.komparator.compare_box_plots(123, ['Height'])  # type: ignore
        with self.assertRaises(TypeError):
            self.komparator.compare_box_plots('Sex', 123)  # type: ignore
        with self.assertRaises(ValueError):
            self.komparator.compare_box_plots('invalid', ['Height'])

    def test_compare_box_plots_with_invalid_categorical_var(self):
        # test that the method raises an exception for invalid
        # categorical variables
        with self.assertRaises(ValueError):
            self.komparator.compare_box_plots('invalid', ['Height', 'Weight'])

    def test_compare_box_plots_with_invalid_numerical_var(self):
        # test that the method raises an exception for invalid
        # numerical variables
        with self.assertRaises(ValueError):
            self.komparator.compare_box_plots('Sex', ['invalid'])

    def test_compare_box_plots_with_missing_categorical_var(self):
        # test that the method raises an exception for missing
        # categorical variables
        with self.assertRaises(ValueError):
            self.komparator.compare_box_plots('Height', ['Weight'])

    def test_compare_box_plots_with_missing_numerical_var(self):
        # test that the method raises an exception for missing
        # numerical variables
        with self.assertRaises(ValueError):
            self.komparator.compare_box_plots('Sex', ['invalid'])


if __name__ == "__main__":
    fileloader = FileLoader()

    try:
        df = fileloader.load("../ressources/athlete_events.csv")
        komparator = Komparator(df)

        komparator.compare_box_plots("Medal", "Age")
        komparator.density("Medal", "Age")
        komparator.compare_histograms("Medal", "Age")

        komparator.compare_box_plots("Sex", ["Weight", "Height", "Age"])
        komparator.density("Sex", ["Weight", "Height", "Age"])
        komparator.compare_histograms("Sex", ["Weight", "Height", "Age"])

        unittest.main()

    except Exception as exception:
        print(exception)
