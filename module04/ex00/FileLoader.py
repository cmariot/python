import pandas


class FileLoader:

    def __init__(self) -> None:
        pass

    def load(self, path) -> 'pandas.DataFrame' or None:
        """
        takes as an argument the file path of the dataset to load,
        displays a message specifying the dimensions of the dataset
        (e.g. 340 x 500) and returns the dataset loaded as a pandas.DataFrame.
        """
        if not isinstance(path, str):
            raise TypeError("Path must be a string")
        try:
            csv_file = pandas.read_csv(path)
            pandas_df = pandas.DataFrame(data=csv_file)
            print("Loading dataset of dimensions {} x {}".format(
                pandas_df.shape[0], pandas_df.shape[1]))
            return pandas_df
        except FileNotFoundError:
            print("File not found")
        except Exception as error:
            print("Error: {}".format(error))
        return None

    def display(self, df, n=0) -> None:
        """
        takes a pandas.DataFrame and an integer as arguments,
        displays the first n rows of the dataset if n is positive,
        or the last n rows if n is negative.
        """
        if not isinstance(df, pandas.DataFrame):
            raise TypeError("df must be a pandas.DataFrame")
        if not isinstance(n, int):
            raise TypeError("n must be an integer")

        if n > df.shape[0] or n < -df.shape[0]:
            print("n must be between {} and {}".format(
                -df.shape[0], df.shape[0]))
        elif n > 0:
            print(df.head(n))
        elif n < 0:
            print(df.tail(-n))
        else:
            print(df)


if __name__ == "__main__":

    file_loader = FileLoader()

    try:
        pandas_dataframe = file_loader.load("../ressources/athlete_events.csv")
        file_loader.display(pandas_dataframe, -10)

    except Exception:
        exit(1)
