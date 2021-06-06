
import numpy as np
from PIL import Image


def bw_convert(image):
    data = np.asarray(image)
    data = np.round(np.sum(data * [[0.2989, 0.5870, 0.1140]], axis=2)).reshape(-1)
    img = Image.new("L", image.size)
    img.putdata(data)
    img.show()


img = Image.open("Test.jpg", "r")
bw_convert(img)
