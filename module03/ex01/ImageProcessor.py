import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


class ImageProcessor:

    def load(self, path: str):
        img = mpimg.imread(path)
        #print("Loading image of dimensions {} x {}".format(img.size[0], img.size[1]))
        return np.array(img)

    def display(self, array):
        plt.imshow(array)
        plt.show()
        return mpimg.fr

if __name__ == "__main__":
    imp = ImageProcessor()
    arr = imp.load("./elon_canaGAN.png")
    imp.display(arr)
    