from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)
CORS(app)

@app.route('/')
def home():
    return "Welcome to the AI-Powered Symptom Checker"

class SymptomChecker(Resource):
    def get(self):
        return {"message": "Welcome to the AI-Powered Symptom Checker"}

    def post(self):
        data = request.get_json()
        symptoms = data.get('symptoms', '')
        # Placeholder for the AI model prediction logic
        predicted_conditions = ["Condition A", "Condition B"]
        return jsonify({
            "symptoms": symptoms,
            "predicted_conditions": predicted_conditions
        })

api.add_resource(SymptomChecker, '/check')

if __name__ == '__main__':
    app.run(debug=True)
