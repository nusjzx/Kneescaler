import cv2
import numpy as np

def img_proc(event, context):
    image = cv2.imread('input_image.jpg')
  
    if image is not None:
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

        # Perform edge detection using Canny
        edges = cv2.Canny(blurred_image, 50, 150)

        # Create a new image that combines the original and the edges
        result_image = np.hstack((image, cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)))
      
        cv2.imwrite('result_image.jpg', result_image)

        return {"message": "Image processing completed."}
    else:
        return {"error": "Failed to load the image."}
