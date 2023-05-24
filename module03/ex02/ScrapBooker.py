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


class ScrapBooker:

    def crop(self, array, dimensions, position):
        """

            Crops the image as a rectangle via dim arguments (being the new
            height and width of the image) from the coordinates given by
            position arguments.

            Args:
                array: numpy.ndarray
                dim: tuple of 2 integers.
                position: tuple of 2 integers.

            Return:
                new_arr: the cropped numpy.ndarray.
                None (if combinaison of parameters not compatible).

            Raise:
                This function should not raise any Exception.

        """
        if (len(dimensions) != 2 or len(position) != 2
                or dimensions[0] < 0 or dimensions[1] < 0
                or position[0] < 0 or position[1] < 0
                or position[0] + dimensions[0] > array.shape[0]
                or position[1] + dimensions[1] > array.shape[1]):
            return None
        return array[position[0]:position[0] + dimensions[0],
                     position[1]:position[1] + dimensions[1]]

    def thin(self, array, n, axis):
        """
            Deletes every n-th line pixels along the specified axis
            (0: Horizontal, 1: Vertical)

            Args:
                array: numpy.ndarray.
                n: non null positive integer lower than the number of
                    row/column of the array (depending of axis value).
                axis: integer of value 0 or 1.

            Return:
                new_arr: thined numpy.ndarray.
                None (if combinaison of parameters not compatible).

            Raise:
                This function should not raise any Exception.

        """
        if (n < 1 or axis < 0 or axis > 1
                or (axis == 0 and n > array.shape[0])
                or (axis == 1 and n > array.shape[1])):
            return None
        return np.delete(array, np.s_[::n], axis=axis)

    def juxtapose(self, array, n, axis):
        """

            Juxtaposes n copies of the image along the specified axis.

            Args:
                array: numpy.ndarray.
                n: positive non null integer.
                axis: integer of value 0 or 1.

            Return:
                new_arr: juxtaposed numpy.ndarray.
                None (combinaison of parameters not compatible).

            Raises:
                This function should not raise any Exception.

        """
        if (n < 1 or axis < 0 or axis > 1):
            return None
        return np.concatenate([array] * n, axis=axis)

    def mosaic(self, array, dimensions):
        """

        Makes a grid with multiple copies of the array. The dim argument
        specifies the number of repetition along each dimensions.

        Args:
            array: numpy.ndarray.
            dim: tuple of 2 integers.

        Return:
            new_arr: mosaic numpy.ndarray.
            None (combinaison of parameters not compatible).

        Raises:
            This function should not raise any Exception.

        """
        if (len(dimensions) != 2 or dimensions[0] < 1 or dimensions[1] < 1):
            return None
        return np.tile(array, dimensions + (1,))


if __name__ == "__main__":
    image_processor = ImageProcessor()
    scrap_booker = ScrapBooker()

    original_img = image_processor.load("../images/elon_canaGAN.png")

    if original_img is not None:

        print("Crop tests :")

        dimmensions = [(576, 576),
                       (300, 300),
                       (300, 300),
                       (500, 500),
                       (100, 100)]

        position = [(0, 0),
                    (0, 0),
                    (200, 200),
                    (500, 500),
                    (200, 200)]

        # Test crop
        for params in zip(dimmensions, position):

            cropped_arr = scrap_booker.crop(
                original_img, dimensions=params[0], position=params[1])

            if cropped_arr is not None:
                print("cropped_arr.shape:", cropped_arr.shape)
                image_processor.display(cropped_arr)
            else:
                print("cropped_arr is None, parameters not compatible")

        # Test thin

        print("Thin tests :")

        n_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        for n in n_array:
            thined_arr = scrap_booker.thin(original_img, n=n, axis=0)
            if thined_arr is not None:
                print("thined_arr.shape:", thined_arr.shape)
                image_processor.display(thined_arr)
            else:
                print("thined_arr is None, parameters not compatible")

        for n in n_array:
            thined_arr = scrap_booker.thin(original_img, n=n, axis=1)
            if thined_arr is not None:
                print("thined_arr.shape:", thined_arr.shape)
                image_processor.display(thined_arr)
            else:
                print("thined_arr is None, parameters not compatible")

        # Test juxtapose

        print("Juxtapose tests :")
        n_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        for n in n_array:
            juxtaposed_arr = scrap_booker.juxtapose(original_img, n=n, axis=0)
            if juxtaposed_arr is not None:
                print("juxtaposed_arr.shape:", juxtaposed_arr.shape)
                image_processor.display(juxtaposed_arr)
            else:
                print("juxtaposed_arr is None, parameters not compatible")

        for n in n_array:
            juxtaposed_arr = scrap_booker.juxtapose(original_img, n=n, axis=1)
            if juxtaposed_arr is not None:
                print("juxtaposed_arr.shape:", juxtaposed_arr.shape)
                image_processor.display(juxtaposed_arr)
            else:
                print("juxtaposed_arr is None, parameters not compatible")

        # Test mosaic

        print("Mosaic tests :")

        dimmensions = [(2, 2),
                       (3, 3),
                       (2, 5),
                       (5, 5),
                       (10, 10)]

        for dim in dimmensions:
            mosaic_arr = scrap_booker.mosaic(original_img, dimensions=dim)
            if mosaic_arr is not None:
                print("mosaic_arr.shape:", mosaic_arr.shape)
                image_processor.display(mosaic_arr)
            else:
                print("mosaic_arr is None, parameters not compatible")
