#import flask
from flask import Flask, request, jsonify

#create instance of this class, the __name__ is the name of module or package
# the first arguement is the name of the application's module or package. __name__ is a convenient shortcut for this
app = Flask(__name__)

# use the route() decorator to tell flask what url shall triger the below function
@app.route("/hello")
def hello_world():
    return "<p>Hello, World!</p>"


# this is a second route() decorator, if the method parameter is not defined it will consider
# by default as a get method
@app.route('/greet', methods=['GET'])
def greet():
    # Get the 'name' parameter from the query string
    name = request.args.get('name', 'World')  # Default to 'World' if no name is provided
    
    # Return a greeting message as a JSON response, the jsonify will make the response in json format
    return jsonify(message=f"Hello, {name}!")

@app.route('/submit', methods=['POST'])
def submit():
    # Get data from the POST request
    data = request.get_json()  # Assume the client is sending JSON data

    # Extract 'name' and 'age' from the JSON data
    name = data.get('name')
    age = data.get('age')

    # Simple response using the provided data
    return jsonify(message=f"Hello, {name}! You are {age} years old.")


# Run the Flask app, the below if __name__ = '__main__'  this allows the script to check whether the script is run directly
# or being imported elsewhere the purpose of mentioning (debug=True) is the application runs in debug mode which is useful in development phase
# whenever there is a change to the code the flask automatically reloads the server
# Always ensure the debug=True is not set when deploying the model into the production
if __name__ == '__main__':
    app.run(debug=True)



