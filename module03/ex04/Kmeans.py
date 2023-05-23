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
    if args.ncentroids < 1 or args.max_iter < 1:
        raise ValueError(
            "Error: ncentroids and max_iter args must be positive intergers.")
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


def display_plots(results, kmean):
    """
      display on 3 differents plots, corresponding to 3 combinaisons of
      2 parameters, the results. (Use different colors to distinguish
      between Venus, Earth, Mars and Belt asteroids citizens.)
    """

    fig1 = plt.figure(1)
    height_weight = fig1.add_subplot()
    height_weight.set_xlabel("Height")
    height_weight.set_ylabel("Weight")

    colors = ['r', 'g', 'b', 'y', 'c', 'm', 'k', 'orange', 'purple']
    for i in range(len(results)):
        results[i] = np.array(results[i])
        height_weight.plot(results[i][0], results[i][1], colors[i], 'x')

    plt.show()
#    height_bonedensity = 0
#    bonedensity_weight = 0


def display_results(result, kmean):
    fig = plt.figure(0)
    ax1 = fig.add_subplot(111, projection='3d')
    ax1.set_xlabel('Height')
    ax1.set_ylabel('Weight')
    ax1.set_zlabel('Bone density')
    colors = ['r', 'g', 'b', 'y', 'c', 'm', 'k', 'orange', 'purple']

    for i in range(len(result)):
        result[i] = np.array(result[i])
        print("Cluster {}:".format(i))
        print(result[i])
        print("Number of individuals: {}".format(len(result[i])))
        print("Centroid: {}".format(kmean.centroids[i]))
        print()

        ax1.scatter(kmean.centroids[i][0],
                    kmean.centroids[i][1],
                    kmean.centroids[i][2],
                    c=colors[i],
                    marker='x')

        ax1.scatter(result[i][:, 0],
                    result[i][:, 1],
                    result[i][:, 2],
                    c=colors[i],
                    marker='o')

    plt.show()


def main():
    try:
        filename, ncentroids, max_iter = get_args()
    except ValueError as error:
        print(error)
        exit(0)
    else:
        dataset = read_file(filename)
        kmean = KmeansClustering(max_iter, ncentroids)
        result = kmean.predict(dataset)
        display_results(result, kmean)
        display_plots(result, kmean)


if __name__ == "__main__":
    main()
