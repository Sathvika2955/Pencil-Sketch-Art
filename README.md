# **Sketch Art Project**

## **Overview**

This is a Python project that converts a given image into a **pencil sketch** using OpenCV. The program loads an image, applies **grayscale conversion**, inverts it, applies **Gaussian blur**, and then blends it to create a **sketch effect**.

## **Features**

- **Converts images into realistic pencil sketches**
- **Uses OpenCV for image processing**
- **Adjustable sketch intensity** by modifying blur levels and scaling factors
- Supports **JPG and PNG** formats

## **Installation**

To run this project, install the required dependencies using the following command:

```bash
pip install -r requirements.txt

```
# **Usage**
-Place the image you want to convert in the project directory.

-Modify project.py to specify the correct image path.

-Run the script using: python project.py

# **Dependencies**

Python 3.x

OpenCV (cv2)


# **Customization**

To adjust the sketch intensity, modify the Gaussian blur kernel size in project.py:
```bash

blur = cv2.GaussianBlur(invert, (5, 5), 0)  # Change (5, 5) to (21, 21) for a softer effect
```

If the sketch is too light or dark, tweak the scale parameter in:
```bash

sketch = cv2.divide(gr, inverted_blur, scale=256.0)  # Lower the scale value for a darker sketch
```

# **Contributing**

If you have suggestions for improvements, feel free to fork the repository and submit a pull request!

# **License**

This project is for learning purposes. Feel free to modify and experiment!

# **Citation**
If you use this project or reference it in any work, please credit:

[Sathvika Nidadavolu]- (https://github.com/Sathvika2955)
