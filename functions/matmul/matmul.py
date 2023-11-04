import numpy as np
from flask import Flask, request, jsonify
from prometheus_flask_exporter import PrometheusMetrics


app = Flask(__name__)
metrics = PrometheusMetrics(app)


by_path_counter = metrics.counter(
    'by_path_counter', 'Request count by request paths',
    labels={'status': lambda r: r.status_code, 'path': lambda r: request.path}
)

fixed_size = 100  # Fixed size for the matrix

@app.route('/matmul', methods=['GET'])
@by_path_counter
def matmul():
    matrix_A = np.random.rand(fixed_size, fixed_size)
    matrix_B = np.random.rand(fixed_size, fixed_size)

    result_matrix = np.dot(matrix_A, matrix_B)

    return jsonify({"result_matrix": result_matrix.tolist()})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)


# We can POST request to http://<our-service-ip>:8080/matmul
