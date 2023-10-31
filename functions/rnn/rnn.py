import tensorflow as tf

def rnn(event, context):

    model = tf.keras.models.load_model('model.h5')

    inference_result = model.predict(input_data)

    return {"inference_result": inference_result.tolist()}  # Convert to a list for JSON serialization

# Example usage:
# result = rnn('input_data', 'context')
