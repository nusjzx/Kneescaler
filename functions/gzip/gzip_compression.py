import gzip
import shutil
from flask import Flask, request, jsonify
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)

by_path_counter = metrics.counter(
    'by_path_counter', 'Request count by request paths',
    labels={'status': lambda r: r.status_code, 'path': lambda r: request.path}
)

@app.route('/gzip_compression', methods=['GET'])
@by_path_counter
def gzip_compression():
    try:
        data = request.get_json()
        input_file = data['input_file']
        output_file = data['output_file']
        num_iterations = data['num_iterations']

        for i in range(num_iterations):
            with open(input_file, 'rb') as f_in, gzip.open(output_file, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)

        return jsonify({"message": "Compression completed"})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)


# make post requests at http://<your-service-ip>:8080/gzip_compression
# expects a JSON payload containing the input file, output file, and the number of iterations.

# Compress 'input.txt' multiple times and overwrite 'output.txt.gz' each time (10 iterations).
# gzip_compression('input.txt', 'output.txt.gz')
