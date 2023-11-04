import cv2
import numpy as np
from flask import Flask, request, jsonify
from prometheus_flask_exporter import PrometheusMetrics


app = Flask(__name__)
metrics = PrometheusMetrics(app)


by_path_counter = metrics.counter(
    'by_path_counter', 'Request count by request paths',
    labels={'status': lambda r: r.status_code, 'path': lambda r: request.path}
)

@app.route('/img_proc', methods=['GET'])
@by_path_counter
def img_proc():
    try:
        image = cv2.imread('input_image_path')
        
        if image is not None:
            gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

            # Perform edge detection using Canny
            edges = cv2.Canny(blurred_image, 50, 150)

            # Create a new image that combines the original and the edges
            result_image = np.hstack((image, cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR))
            
            cv2.imwrite('result_image.jpg', result_image)

            return jsonify({"message": "Image processing completed."})
        else:
            return jsonify({"error": "Failed to load the image."})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

# POST request using http://<your-service-ip>:8080/img_proc
