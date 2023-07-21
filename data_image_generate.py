from PIL import Image
import os

def rotate_images_in_folder(input_folder, target_folder):
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    image_files = os.listdir(input_folder)
    for file_name in image_files:
        image_path = os.path.join(input_folder, file_name)

        # Read the original image
        original_image = Image.open(image_path)

        # Rotate the image at each degree from 0 to 359
        for angle in range(360):
            rotated_image = original_image.rotate(angle)

            # Save the rotated image in the target folder
            rotated_filename = f"rotated_{angle:03d}_{file_name}"
            rotated_output_path = os.path.join(target_folder, rotated_filename)
            rotated_image.save(rotated_output_path)

if __name__ == "__main__":
    input_folder = "path_to_input_folder"
    target_folder = "path_to_target_folder"

    rotate_images_in_folder(input_folder, target_folder)
