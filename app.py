from flask import Flask, jsonify, request
from keras.models import load_model

app = Flask(__name__)

model = load_model("learnflow-model-1.h5")

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
        sentences = request.form.get('input_data')
        pred = model.predict(sentences)
        results = pred()
        return jsonify({'results': results})
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
