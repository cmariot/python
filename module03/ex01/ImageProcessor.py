import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np


class ImageProcessor:

    def load(self, path: str):
        """
        Takes as a parameter a path to an image
        and returns a numpy array representing the image
        """
        img = mpimg.imread(path)
        print("Loading image of dimensions {} x {}".format(img.shape[0], img.shape[1]))
        return np.array(img)

    def display(self, array):
        """
        Takes a numpy array as a parameter and displays
        the corresponding RGB image
        """
        plt.imshow(array)
        plt.show()


if __name__ == "__main__":
    imp = ImageProcessor()
    arr = imp.load("./elon_canaGAN.png")
    imp.display(arr)
