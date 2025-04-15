from flask import Flask, render_template

#imports a dictionary of data from dog_breeds.py and "prettifies", or styles, the dog names when they appear in the HTML page
from dog_breeds import prettify_dog_breed

# Initialize the Flask application
app = Flask(__name__)

#function adds a dash in the URL between breed names with multiple words like miniature poodle
def check_breed(breed):
  return "/".join(breed.split("-"))

@app.route("/")
def hello_world():
  return render_template("dogs.html")


app.debug = True

# Run the flask server
if __name__ == "__main__":
    app.run()