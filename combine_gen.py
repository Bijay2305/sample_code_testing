add_gaussian_noise

random_color_jitter

Combining Transformations 

++++

from PIL import Image, ImageEnhance, ImageOps
import random
import os

def random_flip(image):
    if random.random() < 0.5:
        return ImageOps.flip(image)
    return image

def random_rotation(image, max_angle=30):
    angle = random.randint(-max_angle, max_angle)
    return image.rotate(angle)

def random_color_jitter(image):
    brightness_factor = random.uniform(0.8, 1.2)
    contrast_factor = random.uniform(0.8, 1.2)
    saturation_factor = random.uniform(0.8, 1.2)
    hue_factor = random.uniform(-0.1, 0.1)

    return ImageEnhance.Brightness(image).enhance(brightness_factor), \
           ImageEnhance.Contrast(image).enhance(contrast_factor), \
           ImageEnhance.Color(image).enhance(saturation_factor).enhance(hue_factor)

def apply_combined_transformations_to_images(input_folder, output_folder, num_augmented_images=5):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    image_files = os.listdir(input_folder)
    for file_name in image_files:
        image_path = os.path.join(input_folder, file_name)
        original_image = Image.open(image_path)

        for i in range(num_augmented_images):
            # Create a sequence of transformations
            transformations = [
                random_flip,
                random_rotation,
                random_color_jitter
            ]

            # Apply the transformations to the original image
            augmented_image = original_image.copy()
            for transform in transformations:
                augmented_image = transform(augmented_image)

            # Save the augmented image with a unique filename
            augmented_filename = f"augmented_{i}_{file_name}"
            augmented_output_path = os.path.join(output_folder, augmented_filename)
            augmented_image.save(augmented_output_path)

if __name__ == "__main__":
    input_folder = "path_to_input_folder"
    output_folder = "path_to_output_folder"
    num_augmented_images = 5

    apply_combined_transformations_to_images(input_folder, output_folder, num_augmented_images)
+++++++++++++++

from PIL import Image
import numpy as np
import os

def add_gaussian_noise(image, mean=0, std=20):
    np_image = np.array(image)
    h, w, c = np_image.shape

    # Generate random Gaussian noise
    noise = np.random.normal(mean, std, (h, w, c))

    # Clip the pixel values to [0, 255]
    noisy_image = np.clip(np_image + noise, 0, 255).astype(np.uint8)

    return Image.fromarray(noisy_image)

def add_noise_to_images_in_folder(input_folder, output_folder, mean=0, std=20):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    image_files = os.listdir(input_folder)
    for file_name in image_files:
        image_path = os.path.join(input_folder, file_name)

        # Read the original image
        original_image = Image.open(image_path)

        # Add Gaussian noise to the image
        noisy_image = add_gaussian_noise(original_image, mean, std)

        # Save the noisy image in the output folder
        noisy_filename = f"noisy_{file_name}"
        noisy_output_path = os.path.join(output_folder, noisy_filename)
        noisy_image.save(noisy_output_path)

if __name__ == "__main__":
    input_folder = "path_to_input_folder"
    output_folder = "path_to_output_folder"
    mean = 0
    std = 20

    add_noise_to_images_in_folder(input_folder, output_folder, mean, std)
