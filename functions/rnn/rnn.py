import tensorflow as tf
from flask import Flask, request, jsonify
from prometheus_flask_exporter import PrometheusMetrics


app = Flask(__name__)
metrics = PrometheusMetrics(app)


by_path_counter = metrics.counter(
    'by_path_counter', 'Request count by request paths',
    labels={'status': lambda r: r.status_code, 'path': lambda r: request.path}
)

model = tf.keras.models.load_model('model.h5')  # Load the model

@app.route('/rnn', methods=['GET'])
@by_path_counter
def rnn():
    try:
        data = request.get_json()
        input_data = data['input_data']

        inference_result = model.predict(input_data)

        return jsonify({"inference_result": inference_result.tolist()})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

# http://<service-ip>:8080/rnn
