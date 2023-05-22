import csv
import numpy as np
import matplotlib.pyplot as plt
import argparse


class KmeansClustering:

    def __init__(self, max_iter=20, ncentroid=5):
        self.ncentroid = int(ncentroid)
        self.max_iter = int(max_iter)
        self.centroids = []
        self.labels = ["Venus", "Earth", "Mars", "Belt asteroids"]

    def fit(self, X):
        """
            Run the K-means clustering algorithm.
            For the location of the initial centroids,
            random pick ncentroids from the dataset.

            Args:
                X: has to be an numpy.ndarray, a matrice of dimension m * n.
            Return:
                None.
            Raises:
                This function should not raise any Exception.
        """
        pass

    def predict(self, X):
        """
            Predict from wich cluster each datapoint belongs to.

            Args:
                X: has to be an numpy.ndarray, a matrice of dimension m * n.

            Return:
                the prediction has a numpy.ndarray, a vector of dimension m * 1

            Raises:
                This function should not raise any Exception.
        """
        # - random pick ncentroids from the dataset
        for i in range(self.ncentroid):
            random_index = np.random.randint(0, len(X))
            self.centroids.append(X[random_index])

        print("Centroids: {}".format(self.centroids))

        # - run the K-means clustering algorithm
        for i in range(self.max_iter):
            # - assign each datapoint to the closest centroid
            clusters = [[] for i in range(self.ncentroid)]
            for datapoint in X:
                distances = []
                for j in range(self.ncentroid):
                    # Distance between datapoint and centroid
                    distance = np.linalg.norm(self.centroids[j] - datapoint)
                    distances.append(distance)
                closest_centroid_index = np.argmin(distances)
                clusters[closest_centroid_index].append(datapoint)
            # - update the centroids
            for j in range(self.ncentroid):
                self.centroids[j] = np.mean(clusters[j], axis=0)
        return clusters


def get_args():
    """
    Parse the arguments of the program with argparse
    """
    parser = argparse.ArgumentParser(description='Kmeans clustering algorithm')
    parser.add_argument('filename', type=str, help='the file to read')
    parser.add_argument('ncentroids', type=int, help='the number of centroids')
    parser.add_argument('max_iter', type=int, help='the number of iterations')
    args = parser.parse_args()
    return args.filename, args.ncentroids, args.max_iter


class CsvReader():

    def __init__(self,
                 filename=None,
                 sep=',',
                 header=False,
                 skip_top=0,
                 skip_bottom=0):

        if (filename is None or type(filename) is not str):
            raise ValueError("filename must be a string")
        elif type(sep) is not str:
            raise ValueError("sep must be a string")
        elif type(header) is not bool:
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

        if not self.data:
            return None

        first_row_len = len(self.data[0])
        for i, line in enumerate(self.data):
            if len(line) != first_row_len:
                return None
            for j, field in enumerate(line):
                self.data[i][j] = field.strip()
                if len(self.data[i][j]) == 0:
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


def read_file(filename):
    try:
        with CsvReader(filename, sep=',', header=True) as file:
            if file is None:
                print("File is corrupted, does not exist or is empty.")
                exit(1)
            data = []
            for line in file.getdata():
                x = float(line[1])
                y = float(line[2])
                z = float(line[3])
                data.append([x, y, z])
            return np.array(data)

    except Exception as e:
        print(e)
        exit(1)


def main():
    # - parse the arguments
    filename, ncentroids, max_iter = get_args()

    # - read the dataset from the file and store the data in an array
    dataset = read_file(filename)
    print(dataset)

    # - create a Kmeans object
    kmean = KmeansClustering(max_iter, ncentroids)

    # - predict the result
    result = kmean.predict(dataset)

    # - display the coordinates of the different centroids and the
    #   associated region
    # - display the number of individuals associated to each centroid

    # - display on 3 differents plots, corresponding to 3 combinaisons of
    #   2 parameters, the results. (Use different colors to distinguish
    #   between Venus, Earth, Mars and Belt asteroids citizens.)
    fig = plt.figure()
    ax1 = fig.add_subplot(111, projection='3d')

    colors = ['r', 'g', 'b', 'y', 'c', 'm', 'k', 'w', 'orange', 'purple']
    for i in range(len(result)):
        result[i] = np.array(result[i])
        print("Cluster {}:".format(i))
        print(result[i])
        print("Number of individuals: {}".format(len(result[i])))
        print("Centroid: {}".format(kmean.centroids[i]))
        print()
        x = result[i][:, 0]
        y = result[i][:, 1]
        z = result[i][:, 2]
        color = colors[i]
        centroid_x = kmean.centroids[i][0]
        centroid_y = kmean.centroids[i][1]
        centroid_z = kmean.centroids[i][2]
        ax1.scatter(centroid_x, centroid_y, centroid_z, c=color, marker='x')
        ax1.scatter(x, y, z, c=color, marker='o')

    ax1.set_xlabel('Height')
    ax1.set_ylabel('Weight')
    ax1.set_zlabel('Bone density')

    plt.show()
    pass


if __name__ == "__main__":
    main()
