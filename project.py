import cv2

# Load the image
img = cv2.imread(r'C:\Users\sathv\OneDrive\Documents\Sketchart\Original_Image.jpg')

# Check if the image is loaded properly
if img is None:
    print("Error: Image not loaded. Check the file path.")
else:
    # Convert to grayscale
    gr = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Invert the grayscale image
    invert = cv2.bitwise_not(gr)

    # Apply Gaussian blur
    blur = cv2.GaussianBlur(invert, (5, 5), 0)  # Reduced kernel size

    # Invert the blurred image
    inverted_blur = cv2.bitwise_not(blur)

    # Create the sketch
    sketch = cv2.divide(gr, inverted_blur, scale=256.0)

    # Save the sketch image
    cv2.imwrite(r'C:\Users\sathv\OneDrive\Documents\Sketchart\Sketch_Image.jpg', sketch)

    # Display images
    cv2.imshow('Original Image', img)
    cv2.imshow('Sketch Image', sketch)

    # Wait for a key and close windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()
