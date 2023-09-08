import cv2
import os

# Specify the path to the folder containing the image files
folder_path = './images'

# Get a list of all image files in the folder
image_files = [f for f in os.listdir(folder_path) if f.endswith(('.jpg', '.png', '.jpeg', '.gif', '.bmp'))]
print(f'Found {len(image_files)} image files')


# loop through iimage and show them in a window
for image_file in image_files:
    # Construct the full path to the image file
    image_path = os.path.join(folder_path, image_file)
    
    # Read the image using OpenCV
    image = cv2.imread(image_path)
    
    if image is not None:
        # Display the image in a window
        cv2.imshow(image_file, image)
        
        # Wait for a keypress
        key = cv2.waitKey(0)

        # if the key is number
        if key in [ord('1'), ord('2'), ord('3'), ord('4'), ord('5'), ord('6'), ord('7'), ord('8'), ord('9')]:
            # get key pressed
            print(f'Moving {image_file} to {chr(key)}')
            os.rename(image_path, os.path.join(folder_path, chr(key), image_file))
        
        if key == ord('q') or key == ord('Q'):
            print(f'Moving {image_file} to etc')
            os.rename(image_path, os.path.join(folder_path, 'etc', image_file))
        
        # Close all open windows
        cv2.destroyAllWindows()

    else:
        print(f'Unable to read image: {image_file}')


# # Loop through the image files and get their dimensions
# for image_file in image_files:
#     # Construct the full path to the image file
#     image_path = os.path.join(folder_path, image_file)
    
#     # Read the image using OpenCV
#     image = cv2.imread(image_path)
    
#     if image is not None:
#         # Get the dimensions of the image (height, width, and number of channels)
#         height, width, channels = image.shape
        
#         if width < 32 or height < 32:
#             #move the image to a 'low' folder
#             print(f'Moving {image_file} to low')
#             os.rename(image_path, os.path.join(folder_path, 'low', image_file))
#     else:
#         print(f'Unable to read image: {image_file}')