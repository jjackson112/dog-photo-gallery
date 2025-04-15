from flask import Flask, render_template, request
import requests

#imports a dictionary of data from dog_breeds.py and "prettifies", or styles, the dog names when they appear in the HTML page
from dog_breeds import prettify_dog_breed

# Initialize the Flask application
app = Flask("app")

#function adds a dash in the URL between breed names with multiple words like miniature poodle
def check_breed(breed):
  return "/".join(breed.split("-"))

@app.route("/", methods=["GET", "POST"])
def dog_image_gallery():
# empty list to handle errors, will hold error message
  errors = []
# request.form.get collects values with GET
  if request.method == "POST":
    breed = request.form.get("breed")
  if not breed:
    errors.append("Oops! Please select a breed.")
  if breed:
# concatenating the check_breed(breed) will place the breed name after the last /
# concatenating the URL parameter pulls 30 random images of selected breed
    response = requests.get("https://www.dog.ceo/api/breed/" + check_breed(breed) + "/images/random/30")
    data = response.json()
    dog_images = data["message"]
  return render_template("dogs.html")

app.debug = True

# Run the flask server
if __name__ == "__main__":
    app.run()
