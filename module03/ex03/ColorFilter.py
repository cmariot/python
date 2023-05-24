import numpy as np
from numpy import ndarray
from PIL import Image
import matplotlib.pyplot as plt


class ImageProcessor:

    def load(self, path: str) -> ndarray:

        """
            Takes as a parameter a path to an image
            and returns a numpy array representing the image
            or None if something went wrong.
        """

        if not isinstance(path, str):
            print("Error: The path argument must be a string")
            return None

        try:
            # Open the image
            image = Image.open(path)

            # Display the dimensions of the image
            width, height = image.size
            print("Image dimensions: {} x {}".format(width, height))

            # Return the image as a NumPy array
            return np.array(image)

        except FileNotFoundError:
            print("The image file was not found.")
            return None

        except Exception as e:
            print("An error occurred:", str(e))
            return None

    def display(self, image_array):

        """
            Takes as a parameter a numpy array
            representing an image, and displays the image.
        """

        if not isinstance(image_array, np.ndarray):
            print("Error: The image_array argument must be a NumPy array")
            return None
        elif len(image_array.shape) != 3:
            print("Error: The image_array argument must be a 3D NumPy array")
            return None

        try:
            plt.imshow(image_array)
            plt.axis('off')
            plt.show()
        except Exception as error:
            print("An error occurred while displaying the image:", str(error))


class ColorFilter:

    def invert(self, array):
        """

            Inverts the color of the image received as a numpy array.

            Args:
                array: numpy.ndarray corresponding to the image.

            Return:
                array: numpy.ndarray corresponding to the transformed image.
                None: otherwise.

            Raises:
                This function should not raise any Exception.

        """
        inverted_array = array.copy()

        inverted_array[:, :, 0] = 255 - inverted_array[:, :, 0]  # R
        inverted_array[:, :, 1] = 255 - inverted_array[:, :, 1]  # G
        inverted_array[:, :, 2] = 255 - inverted_array[:, :, 2]  # B
        return inverted_array

    def to_blue(self, array):
        """

            Applies a blue filter to the image received as a numpy array.

            Args:
                array: numpy.ndarray corresponding to the image.

            Return:
                array: numpy.ndarray corresponding to the transformed image.
                None: otherwise.

            Raises:
                This function should not raise any Exception.

        """
        blue_array = array.copy()
        blue_array[:, :, 0] = 0  # R
        blue_array[:, :, 1] = 0  # G
        return blue_array

    def to_green(self, array):
        """

            Applies a green filter to the image received as a numpy array.

            Args:
                array: numpy.ndarray corresponding to the image.

            Return:
                array: numpy.ndarray corresponding to the transformed image.
                None: otherwise.

            Raises:
                This function should not raise any Exception.

        """
        green_array = array.copy()
        green_array[:, :, 0] = 0  # R
        green_array[:, :, 2] = 0  # B
        return green_array

    def to_red(self, array):
        """

            Applies a red filter to the image received as a numpy array.

            Args:
                array: numpy.ndarray corresponding to the image.

            Return:
                array: numpy.ndarray corresponding to the transformed image.
                None: otherwise.

            Raises:
                This function should not raise any Exception.

        """
        red_array = array.copy()
        red_array[:, :, 1] = 0  # G
        red_array[:, :, 2] = 0  # B
        return red_array

    def to_celluloid(self, array):
        """

            Applies a celluloid filter to the image received as a numpy array.

            Celluloid filter must display at least four thresholds of shades.
            Be careful! You are not asked to apply black contour on the object,
            you only have to work on the shades of your images.

            Remarks:
                celluloid filter is also known as cel-shading or toon-shading.

            Args:
                array: numpy.ndarray corresponding to the image.

            Return:
                array: numpy.ndarray corresponding to the transformed image.
                None: otherwise.

            Raises:
                This function should not raise any Exception.

        """
        celluloid_array = array.copy()
        threshold = 4  # number of thresholds of shades
        step = 255 // threshold  # step between each threshold
        for i in range(threshold):  # for each threshold
            # filter the array to get the pixels between the current threshold
            filter_array = ((celluloid_array > i * step)
                            & (celluloid_array <= (i + 1) * step))
            # set the pixels between the current threshold to the current
            celluloid_array[filter_array] = i * step
        return celluloid_array

    def to_grayscale(self, array, filter, **kwargs):
        """

            Applies a grayscale filter to the image received as a numpy array.
            For filter = "mean": performs the mean of RBG channels.
            For filter = "weight": performs a weighted mean
            of RBG channels.

            Args:
                array: numpy.ndarray corresponding to the image.
                filter: string with accepted values in ["mean", "weight"]
                weights: [kwargs] list of 3 floats where the sum equals to 1,
                        corresponding to the weights of each RBG channels.

            Return:
                array: numpy.ndarray corresponding to the transformed image.
                None: otherwise.

            Raises:
                This function should not raise any Exception.

        """
        grayscale_array = array * 1

        if filter == "mean":
            mean = np.sum(array[:, :, :3], axis=2) / 3
            for i in range(3):
                grayscale_array[:, :, i] = mean
        elif filter == "weight":
            if "weights" not in kwargs:
                return None
            weights = kwargs["weights"]
            if (not isinstance(weights, list)
                or len(weights) != 3
                    or sum(weights) != 1.0):
                return None
            weigthed_mean = np.sum(array[:, :, :3] * weights, axis=2) / 3
            for i in range(3):
                grayscale_array[:, :, i] = weigthed_mean
        else:
            return None
        return grayscale_array


if __name__ == "__main__":
    image_processor = ImageProcessor()

    original_img = image_processor.load("../images/elon_canaGAN.png")
    if original_img is None:
        exit()

    image_processor.display(original_img)

    color_filter = ColorFilter()

    inverted_img = color_filter.invert(original_img)
    if inverted_img is not None:
        image_processor.display(inverted_img)

    blue_img = color_filter.to_blue(original_img)
    if blue_img is not None:
        image_processor.display(blue_img)

    green_img = color_filter.to_green(original_img)
    if green_img is not None:
        image_processor.display(green_img)

    red_img = color_filter.to_red(original_img)
    if red_img is not None:
        image_processor.display(red_img)

    celluloid_img = color_filter.to_celluloid(original_img)
    if celluloid_img is not None:
        image_processor.display(celluloid_img)

    grayscale_img = color_filter.to_grayscale(original_img, "mean")
    if grayscale_img is not None:
        image_processor.display(grayscale_img)

    grayscale_img = color_filter.to_grayscale(original_img, "weight",
                                              weights=[0.299, 0.587, 0.114])
    if grayscale_img is not None:
        image_processor.display(grayscale_img)

    grayscale_img = color_filter.to_grayscale(original_img, "weight",
                                              weights=[0.5, 0.5, 0])
    if grayscale_img is not None:
        image_processor.display(grayscale_img)

    grayscale_img = color_filter.to_grayscale(original_img, "weight",
                                              weights=[0.5, 0, 0.5])
    if grayscale_img is not None:
        image_processor.display(grayscale_img)

    grayscale_img = color_filter.to_grayscale(original_img, "weight",
                                              weights=[0, 0.5, 0.5])
    if grayscale_img is not None:
        image_processor.display(grayscale_img)
