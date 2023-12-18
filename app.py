from flask import Flask, jsonify, request
from tensorflow.keras.models import load_model






app = Flask(__name__)

#load model
model = load_model('Model_tanpa_self_learning.h5')

# def model_prediction(model, Sentence):
#   input_sequence = tokenizer.texts_to_sequences([Sentence])
#   input_padded = pad_sequences(input_sequence)

#   prediction =  model.predict (input_padded)

#   predicted_style = label_encoder.inverse_transform([np.argmax(prediction)])

#   return predicted_style[0]



#fetching api
@app.route("/")
def index():
    return jsonify({
        "status": {
            "code" : 200,
            "message" : "success fetching api"
        },
        "data": None
    }), 200

#prediction route
@app.route("/predict", methods=["POST"])




def predict():
    if request.method == "POST":
        # Handle the POST request
        json_data = request.get_json()
        if json_data is not None:
            try:
                # #checking data type
                # data_type = type(json_data)
                # data = f'The data type is: {data_type}'
                
                # return jsonify({
                #     "status":({
                #         "code": 200,
                #         "status": "success",
                #         "message": data,
                #         "data": json_data
                #     }),
                # })
                
                # data processing
                # data masuk harus melewati proses model_prediction

                
                # data final(save the final data as a variable, ex: data = )
                sentence_to_predict =
            
                # preditct data final + predict score 
                predicted_style = model_prediction(model, sentence_to_predict)
                
                return
                return jsonify({
                    "status":({
                        "code": 200,
                        "message": "Success predicting"
                    }),
                    "data": {
                        "learning_types_prediction": learning_type,
                        #return hasil prediksi + skor prediksi
                    }
                }), 200
            except Exception as e:
                return jsonify({
                    "status":({
                        "code": 500,
                        "message": "Internal Server Error"
                    }),
                    "data": None
                }), 500
        else:
            return jsonify({
                "status": {
                    "code": 400,
                    "message": "Bad Request"
                },
                "data": None
            }), 400
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
