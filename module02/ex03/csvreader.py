import csv


class CsvReader():

    def __init__(self,
                 filename=None,
                 sep=',',
                 header=False,
                 skip_top=0,
                 skip_bottom=0):
        if (filename is None or type(filename) is not str):
            raise ValueError("filename must be a string")
        elif (type(sep) is not str):
            raise ValueError("sep must be a string")
        elif (type(header) is not bool):
            raise ValueError("header must be a boolean")
        elif ((type(skip_top) is not int) or (skip_top < 0)):
            raise ValueError("skip_top must be a positive integer")
        elif ((type(skip_bottom) is not int) or (skip_bottom < 0)):
            raise ValueError("skip_bottom must be a positive integer")

        self.filename = filename
        self.fd = None
        self.sep = sep
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom
        self.header = header
        self.data = None

    def __enter__(self):

        try:
            self.fd = open(self.filename, newline='')
            csv_reader = csv.reader(self.fd, delimiter=self.sep)
        except OSError:
            return None

        self.data = list(csv_reader)

        if self.header is True:
            self.header = self.data[0]
            for i, field in enumerate(self.header):
                self.header[i] = field.strip()
            self.data = self.data[1:]
        else:
            self.header = None

        if self.skip_top > 0:
            self.data = self.data[self.skip_top:]
        if self.skip_bottom > 0:
            self.data = self.data[:-self.skip_bottom]

        if len(self.data) == 0:
            return None

        first_row_len = len(self.data[0])
        for i, line in enumerate(self.data):
            if len(line) != first_row_len:
                return None
            for j, field in enumerate(line):
                self.data[i][j] = field.strip()
                if len(field) == 0:
                    return None
        return self

    def __exit__(self, exception_type, exception_value, exception_traceback):
        if self.fd is not None:
            self.fd.close()

    def getheader(self):
        """ Retrieves the header from csv file.
        Returns:
                list: representing the data (when self.header is True).
                None: (when self.header is False).
        """
        return self.header

    def getdata(self):
        """
        Retrieves the data/records from skip_top to skip bottom.
        Return:
            nested list(list(list, list, ...)) representing the data.
        """
        return self.data


if __name__ == "__main__":

    with CsvReader('good.csv', header=True) as file:
        if file is None:
            print("File is corrupted")
        else:
            data = file.getdata()
            header = file.getheader()
            print("Header :", header)
            print("Data :", data)

    with CsvReader('bad.csv', header=True) as file:
        if file is None:
            print("File is corrupted")
        else:
            data = file.getdata()
            header = file.getheader()
            print(header)
            print(data)
