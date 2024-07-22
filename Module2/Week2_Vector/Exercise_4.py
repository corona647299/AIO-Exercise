import numpy as np
import cv2


bg1_image = cv2.imread("D:\\Demo-git\\AIO-Exercise\\Module2\\Week2_Vector\\GreenBackground.png", 1)
bg1_image = cv2.resize(bg1_image, (678, 381))

ob_image = cv2 .imread (r"D:\Demo-git\AIO-Exercise\Module2\Week2_Vector\Object.png", 1)
ob_image = cv2 .resize (ob_image , (678, 381))

bg2_image = cv2.imread("D:\\Demo-git\\AIO-Exercise\\Module2\\Week2_Vector\\NewBackground.jpg", 1)
bg2_image = cv2.resize(bg2_image, (678, 381))

differences = cv2.absdiff(bg1_image, ob_image)
differences_single = np.sum(differences, axis=2) / 3.0
differences_single = differences_single.astype(np.uint8)

def compute_binary_mask(differences_single):
    differences_binary = np.where(differences_single >= 15, 255, 0)
    differences_binary = np.stack((differences_binary,)*3, axis=-1)
    return differences_binary
binary_img = np.where(differences_single >= 15, 255, 0)
binary_img = np.stack((binary_img,)*3, axis=-1)

binary_mask = compute_binary_mask(differences_single)
bg2_image = cv2.cvtColor(bg2_image, cv2.COLOR_BGR2GRAY)
output = np.where(compute_binary_mask == 255, ob_image, bg2_image)
cv2.imshow('Image Window', output)
cv2.waitKey(0)