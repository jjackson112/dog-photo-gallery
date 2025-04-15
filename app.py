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
# add error handling to the app, will hold error message
  errors=[]
# save data from request.method, add breed variable
  if request.method == "POST":
    breed = request.form.get("breed")
    number = request.form.get("number")
    if not breed:
      errors.append("Oops! Please select a breed.")
    if not number:
      errors.append("Oops! Please select a number.")
    if breed and number:
      response = requests.get("https://dog.ceo/api/breed/" + check_breed(breed) + "/images/random/" + number)
      data = response.json()
      dog_images = data["messages"]
      return render_template("dogs.html", images=dog_images, breed=prettify_dog_breed(breed), errors=[])
  # this return will handle the HTML template when no dropmenu selection has been made
  return render_template("dogs.html", images=[], breed="", errors=errors)

app.debug = True
# Run the flask server
app.run(host='0.0.0.0', port=8080)
