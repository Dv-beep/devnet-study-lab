### This is the main entry point of the Flask application ###

from flask import request, Flask, jsonify
from classes.mycar import Car
app = Flask(__name__) # this is the Flask application instance that will be used to define routes and handle requests.

## Define routes and request handlers here
@app.route('/api', methods=['GET']) # this decorator defines a route for the URL path '/api' that accepts GET requests.
def hello():                        # this function is the request handler for the '/api' route. It returns a JSON response with a message.
    return jsonify({'message': 'Hello, from your Flask API'}) # this function is the request handler for the '/api' route. It returns a JSON response with a message.


@app.route('/api/car', methods=['POST']) # this decorator defines a route for the URL path '/api/car' that accepts POST requests.
def handle_car_request():                        # this function is the request handler for the '/api/car' route
    data = request.get_json() # this line retrieves the JSON data sent in the POST request and stores it in the variable 'data'.
    try:
        make = data.get('make') # this line extracts the 'make' value from the JSON data.
        model = data.get('model') # this line extracts the 'model' value from the JSON data.
        year = data.get('year') # this line extracts the 'year' value from the JSON data.
        
        if not all([make, model, year]): # this line checks if any of the required fields (make, model, year) are missing in the JSON data.
            return jsonify({'error': 'Missing required fields: make, model, year'}), 400 # if any required field is missing, this line returns a JSON response with an error message and a 400 Bad Request status code.

        car = Car(make, model, year) # this line creates an instance of the Car class using the extracted values.
        return jsonify({'car': car.__dict__}), 201 # this line returns a JSON response containing the car's attributes (converted to a dictionary) and a 201 Created status code.
    except Exception as e: # this line catches any exceptions that occur during the processing of the request.
        return jsonify({'error': str(e)}), 500 # if an exception occurs, this line returns a JSON response with the error message and a 500 Internal Server Error status code.

if __name__ == '__main__': # this line checks if the script is being run directly (as the main program) and starts the Flask development server with debug mode enabled.
    app.run(debug=True)
    
## 