from flask import Flask, jsonify, request
from tensorflow.keras.models import load_model
import ast  

app = Flask(__name__)

model = load_model("learnflow-model-1", compile = False)

@app.route("/")
def index():
    return jsonify({
        "status": {
            "code" : 200,
            "message" : "success fetching api"
        },
        "data": None
    }), 200

@app.route("/predict", methods=["POST"])
def predict():
    if request.method == "POST":
        # Handle the POST request 
        data = request.get_json()
        if data is not None:
            try:
                input_data_str = request.form.get('input_data')
                input_data = ast.literal_eval(input_data_str)
                if not isinstance(input_data, list) or len(input_data) != 10:
                    return jsonify({'message': 'input_data must contain 10 values'}), 400 
                     # 10 values of data multiple coice (A, B, C, ... , D)
                
                # ML model prediction ???
                
                results = model.predict(...)  

                return jsonify({
                    "status": {
                        "code": 200,
                        #'results': results
                    },
                }), 200
            except Exception as e:
                return jsonify({
                    "status": {
                        "code": 500,
                        "message": "Internal Server Error"
                    },
                    "data": None
                }), 500
        else:
            return jsonify({
                "status": {
                    "code": 405,
                    "message": "Bad Request"
                },
                "data": None
            }), 405
    else:
        return jsonify({
            "status": {
                "code": 405,
                "message": "Method Not Allowed"
            },
            "data": None
        }), 405

if __name__=="__main__":
    app.run()
