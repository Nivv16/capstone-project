from flask import Flask, jsonify, request
from tensorflow.keras.models import load_model


app = Flask(__name__)


model = load_model("learnflow-model-1", compile = false)


@app.route("/")
def index():
    return jsonify({
        "status": {
            "code": 200,
            "message": "success fetching the API"
        },
        "data": None,
    }), 200

@app.route("/prediction", methods=["GET", "POST"])
def prediction():
    if request.method == "POST":
        try:
            input_data_str = request.form.get('input_data')
            
            input_data = ast.literal_eval(input_data_str)
            
            if not isinstance(input_data, list) or len(input_data) != 10:
                return jsonify({'message': 'input_data must contain 10 values'}), 400

            # ML model

            return jsonify({'status': 'success'}), 200

        except Exception as e:
            return jsonify({'error': 'Something went wrong'}), 500

    else:
        return jsonify({
            "status": {
                "code": 405,
                "message": "Method not allowed"
            },
            "data": None,
        }), 405


if __name__ == "__main__":
    app.run()
