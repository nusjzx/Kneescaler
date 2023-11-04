import tensorflow as tf
from flask import Flask, request, jsonify

app = Flask(__name)

model = tf.keras.models.load_model('model.h5')  # Load the model

@app.route('/rnn', methods=['POST'])
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
