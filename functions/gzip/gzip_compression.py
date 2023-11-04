import gzip
import shutil
from flask import Flask, request, jsonify

app = Flask(__name)

@app.route('/gzip_compression', methods=['POST'])
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
