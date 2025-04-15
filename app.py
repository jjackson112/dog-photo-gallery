from flask import Flask, render_template, request
import requests

#imports a dictionary of data from dog_breeds.py and "prettifies", or styles, the dog names when they appear in the HTML page
from dog_breeds import prettify_dog_breed

# Initialize the Flask application
app = Flask("app")

#function adds a dash in the URL between breed names with multiple words like miniature poodle
def check_breed(breed):
  return "/".join(breed.split("-"))

@app.route("/", methods=["GET","POST"])
def dog_image_gallery():
# empty list to handle errors, will hold error message
  errors = []
# request.form.get collects values with GET
  if request.method == "POST":
    breed = request.form.get("breed")
    number = request.form.get("number")
    if not breed:
      errors.append("Oops! Please choose a breed.")
    if not number:
      errors.append("Oops! Please choose a number.")
    if breed and number:
# concatenating the check_breed(breed) will place the breed name after the last /
# concatenating the URL parameter pulls 30 random images of selected breed
      response = requests.get("https://dog.ceo/api/breed/" + check_breed(breed) + "/images/random/" + number)
      data = response.json()
      dog_images = data["message"]
# images holds the dictionary data, breed holds the dog breed name from POST request, and then the errors list
      return render_template("dogs.html", images=dog_images, breed=prettify_dog_breed(breed), errors=[])
# the empty list and blank string will handle the HTML template when no selection has been made, errors will display the error message
  return render_template("dogs.html", images=[], breed="", errors=errors)
