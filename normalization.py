from math import sqrt
import numpy as np
import cv2

class Normalization:
    def __normalize_pixel(self, pixel, target_variance, variance, target_mean, mean):
        coefficient = sqrt((target_variance * (pixel - mean)**2) / variance)
        return target_mean + coefficient if pixel > mean else target_mean - coefficient

    def normalize_image(self, image, target_mean, target_variance):
        image_mean = np.mean(image)
        image_variance = np.std(image)**2
        (image_width, image_height) = image.shape
        normalized_image = image.copy()

        for i in range(image_height):
            for j in range(image_width):
                normalized_image[j, i] = self.__normalize_pixel(image[j, i], target_variance, image_variance, target_mean, image_mean)

        return normalized_image