from numpy import ndarray
import numpy as np
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

        try:
            # Display the image
            plt.imshow(image_array)
            plt.axis('off')
            plt.show()

        except Exception as e:
            print("An error occurred while displaying the image:", str(e))


if __name__ == "__main__":

    image_processor = ImageProcessor()
    image_path = input("Enter the path to an image file: ")

    pixels_array = image_processor.load(image_path)
    if pixels_array is not None:
        image_processor.display(pixels_array)
