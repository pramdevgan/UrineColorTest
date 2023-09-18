import cv2

# Load the image
image_path = '../media/strip_images/image1.jpg'  # Replace with the actual image path
image = cv2.imread(image_path)

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
contours, _ = cv2.findContours(gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
for contour in contours:
    # Approximate the contour to a polygon with a certain epsilon value
    epsilon = 0.04 * cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, epsilon, True)
    if len(approx) == 4:
        cv2.drawContours(image, [approx], 0, (0, 255, 0), 2)

        # Get the coordinates of the corners
        corners = [tuple(point[0]) for point in approx]

# Display the image with detected rectangles/squares
cv2.imshow('Rectangles and Squares', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
