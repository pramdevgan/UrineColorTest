import cv2


def values(image_path):
    # Load the image
    image = cv2.imread(image_path)

    # Define the coordinates of the points
    coordinates = [(155, 65), (155, 165), (155, 265), (155, 365), (155, 465),
                   (155, 555), (155, 655), (155, 755), (155, 855), (155, 950)]

    # Dictionary to store the RGB values
    colors = {}

    # Get the RGB values at each coordinate
    for i, (x, y) in enumerate(coordinates, start=1):
        # Get the BGR values at the given coordinate
        b, g, r = image[y, x]

        # Store the RGB values in the dictionary
        colors[f'Point {i}'] = (r, g, b)

    return (colors)
# Print the RGB values
