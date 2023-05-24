import csv
import numpy as np
import matplotlib.pyplot as plt
import argparse
import random


def planet_prediction(dataset, prediction, kmean):

    for i in range(len(kmean.centroids)):
        centroid = kmean.centroids[i]
        if i == 0:
            min_height = centroid[0]
            min_weight = centroid[1]
            min_bone_density = centroid[2]
            max_height = centroid[0]
            max_weight = centroid[1]
            max_bone_density = centroid[2]
            min_height_index = min_weight_index = i
            min_density_index = max_height_index = i
            max_weight_index = i
        else:
            if centroid[0] < min_height:
                min_height = centroid[0]
                min_height_index = i
            if centroid[1] < min_weight:
                min_weight = centroid[1]
                min_weight_index = i
            if centroid[2] < min_bone_density:
                min_bone_density = centroid[2]
                min_density_index = i
            if centroid[0] > max_height:
                max_height = centroid[0]
                max_height_index = i
            if centroid[1] > max_weight:
                max_weight = centroid[1]
                max_weight_index = i
            if centroid[2] > max_bone_density:
                max_bone_density = centroid[2]

    if max_height_index == min_density_index == max_weight_index:
        belt = max_height_index
    else:
        belt = max_weight_index
    earth = min_height_index
    venus = min_weight_index
    mars = 6 - belt - earth - venus

    return [("Belt", belt), ("Earth", earth), ("Venus", venus), ("Mars", mars)]


class KmeansClustering:

    def __init__(self, max_iter=20, ncentroid=4):
        self.ncentroid = int(ncentroid)
        self.max_iter = int(max_iter)
        self.centroids = []
        self.data_cluster_index = []

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

        # check if the number of centroids is not greater than the number
        # of datapoints
        if self.ncentroid > len(X):
            print(
                "Error: ncentroids must be lower than the number of datapoints"
                )
            exit(1)

        # check if there is at least ncentroids different datapoints
        if len(np.unique(X, axis=0)) < self.ncentroid:
            print(
                "Error: there must be at least ncentroids different datapoints"
                )
            exit(1)

        # normalize the dataset
        if np.std(X, axis=0).any() != 0:
            X = (X - np.mean(X, axis=0)) / np.std(X, axis=0)

        # - get the range of the dataset
        heigth_range = (np.min(X[:, 0]), np.max(X[:, 0]))
        weight_range = (np.min(X[:, 1]), np.max(X[:, 1]))
        bone_density_range = (np.min(X[:, 2]), np.max(X[:, 2]))

        # - check if the range of the dataset is not null
        if (heigth_range[0] == heigth_range[1] or
            weight_range[0] == weight_range[1] or
                bone_density_range[0] == bone_density_range[1]):
            print("Error: the range of the dataset is null.")
            exit(1)

        # - initialize the centroids randomly in the range of the dataset
        for i in range(self.ncentroid):
            random_heigth = random.uniform(heigth_range[0], heigth_range[1])
            random_weight = random.uniform(weight_range[0], weight_range[1])
            random_bone_density = random.uniform(bone_density_range[0],
                                                 bone_density_range[1])
            self.centroids.append([random_heigth,
                                   random_weight,
                                   random_bone_density])

        return None

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

        X_copy = X.copy()

        # - normalize the dataset
        X = (X - np.mean(X, axis=0)) / np.std(X, axis=0)

        # - run the K-means clustering algorithm for max_iter iterations
        i = 0
        while i < self.max_iter:
            print("Iteration {}".format(i))

            # save the old centroids
            old_centroids = self.centroids.copy()

            # initialize the data clusters indexes
            self.data_cluster_index = []

            # create a list of empty clusters
            clusters = [[] for i in range(self.ncentroid)]

            # for each datapoint:
            for datapoint in X:

                # compute the distance between the datapoint and each centroid
                distances = []
                for j in range(self.ncentroid):
                    distance = np.linalg.norm(self.centroids[j] - datapoint)
                    distances.append(distance)

                # assign the datapoint to the closest centroid
                closest_centroid_index = np.argmin(distances)
                clusters[closest_centroid_index].append(datapoint)
                self.data_cluster_index.append(closest_centroid_index)

            # if a cluster is empty, reinitialize the centroids
            new_centroids = False
            for j in range(self.ncentroid):
                if len(clusters[j]) == 0:
                    self.centroids = []
                    self.fit(X_copy)
                    new_centroids = True
                    break
            if new_centroids is True:
                i = 0
                print("Reinitializing centroids...")
                continue

            # update the centroids to the mean of each cluster
            for j in range(self.ncentroid):
                self.centroids[j] = np.mean(clusters[j], axis=0)

            # display the prediction
            display_prediction(X_copy, self.data_cluster_index, self)

            # if the centroids did not change, stop the algorithm
            if i > 0 and np.array_equal(self.centroids, old_centroids):
                break

            i += 1

        return self.data_cluster_index


def display_plots(dataset, prediction, kmean):
    """
      display on 3 differents plots, corresponding to 3 combinaisons of
      2 parameters, the results. (Use different colors to distinguish
      between Venus, Earth, Mars and Belt asteroids citizens.)
    """

    figure, ax = plt.subplots(1, 3)

    ax[0].set_xlabel('Height')
    ax[0].set_ylabel('Weight')

    ax[1].set_xlabel('Height')
    ax[1].set_ylabel('Bone density')

    ax[2].set_xlabel('Weight')
    ax[2].set_ylabel('Bone density')

    colors = ['r', 'g', 'b', 'y', 'c', 'm', 'k',
              'orange', 'purple', 'pink', 'brown', 'gray']

    # Get the results for each cluster and display them
    results = [[] for i in range(kmean.ncentroid)]

    for i, datapoint in enumerate(dataset):
        results[prediction[i]].append(datapoint)

    for i in range(len(results)):

        results[i] = np.array(results[i])
        ax[0].scatter(x=results[i][:, 0], y=results[i][:, 1],
                      c=colors[i % len(colors)], marker='o')
        ax[1].scatter(x=results[i][:, 0], y=results[i][:, 2],
                      c=colors[i % len(colors)], marker='o')
        ax[2].scatter(x=results[i][:, 1], y=results[i][:, 2],
                      c=colors[i % len(colors)], marker='o')

    if len(results) == 4:
        legend = planet_prediction(dataset, prediction, kmean)
        legend.sort(key=lambda x: x[1])
        # Add a legend to the plot
        ax[0].legend([legend[i][0] for i in range(len(legend))],
                     loc=(0, 1.02), ncol=4)

    plt.show()


def display_prediction(dataset, prediction, kmean):

    fig = plt.figure(0)
    plt.clf()
    ax1 = fig.add_subplot(111, projection='3d')
    ax1.set_xlabel('Height')
    ax1.set_ylabel('Weight')
    ax1.set_zlabel('Bone density')
    colors = ['r', 'g', 'b', 'y', 'c', 'm', 'k', 'orange', 'purple']

    # Get the results for each cluster and display them
    results = [[] for i in range(kmean.ncentroid)]

    for i, datapoint in enumerate(dataset):
        results[prediction[i]].append(datapoint)

    # Add the datapoints to the plot
    for i in range(len(results)):
        population = np.array(results[i])
        print("Cluster {}:".format(i))
        print(population)
        print("Number of individuals: {}".format(len(population)))
        centroid = kmean.centroids[i]
        centroid = (centroid * np.std(dataset, axis=0)
                    + np.mean(dataset, axis=0))
        print("Centroid: {}\n".format(centroid))
        ax1.scatter(population[:, 0],
                    population[:, 1],
                    population[:, 2],
                    c=colors[i % len(colors)],
                    marker='o')

    # Add the denormalized centroids to the plot
    for i in range(len(kmean.centroids)):
        centroid = kmean.centroids[i]
        centroid = (centroid * np.std(dataset, axis=0)
                    + np.mean(dataset, axis=0))
        ax1.scatter(centroid[0],
                    centroid[1],
                    centroid[2],
                    c=colors[i % len(colors)],
                    marker='x')

    plt.show()


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
                if len(line) != 4:
                    print("File is corrupted or is empty.")
                    exit(1)
                x = float(line[1])
                y = float(line[2])
                z = float(line[3])
                data.append([x, y, z])
            return np.array(data)

    except Exception as e:
        print(e)
        exit(1)


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


def main():
    try:
        filename, ncentroids, max_iter = get_args()
    except ValueError as error:
        print(error)
    else:
        dataset = read_file(filename)
        kmean = KmeansClustering(max_iter, ncentroids)
        kmean.fit(dataset)
        prediction = kmean.predict(dataset)
        display_prediction(dataset, prediction, kmean)
        display_plots(dataset, prediction, kmean)


if __name__ == "__main__":
    main()
