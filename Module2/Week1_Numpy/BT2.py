import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

img = mpimg.imread(
    'D:\\Demo-git\\AIO-Exercise\\Module2\\Week1_Numpy\\download.jpg')


def color2grayscale1(vector):
    return np.max(vector)*0.5 + np.min(vector)*0.5


grayscale_01 = np.apply_along_axis(color2grayscale1, axis=2, arr=img)

plt.imshow(grayscale_01, cmap=plt.get_cmap('gray'))
plt.show()
print(grayscale_01[0, 0])


def color2grayscale2(vector):
    return np.sum(vector)/3


grayscale_02 = np.apply_along_axis(color2grayscale2, axis=2, arr=img)
plt.imshow(grayscale_02, cmap=plt.get_cmap('gray'))
plt.show()
print(grayscale_02[0, 0])


def color2grayscale3(vector):
    return 0.21*vector[0] + 0.72*vector[1] + 0.07*vector[2]


grayscale_03 = np.apply_along_axis(color2grayscale3, axis=2, arr=img)
plt.imshow(grayscale_03, cmap=plt.get_cmap('gray'))
plt.show()
print(grayscale_03[0, 0])
