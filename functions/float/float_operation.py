from flask import Flask, request, jsonify
from prometheus_flask_exporter import PrometheusMetrics


app = Flask(__name__)
metrics = PrometheusMetrics(app)


by_path_counter = metrics.counter(
    'by_path_counter', 'Request count by request paths',
    labels={'status': lambda r: r.status_code, 'path': lambda r: request.path}
)

@app.route('/float_operation', methods=['GET'])
@by_path_counter
def float_operation():
    try:
        result = 0.0
        for i in range(1000000):
            result += i / 3.14159265359
        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"error": str(e)})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

# Once it's deployed, we can make POST requests to http://<your-service-ip>:8080/float_operation 
# to invoke your function and get the result.
