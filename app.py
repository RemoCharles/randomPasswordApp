from flask import Flask, render_template, url_for, request, redirect
from random import *


app = Flask(__name__)

@app.route("/")
def index():
  return render_template('index.html')

@app.route("/generate", methods=['POST'])
def randomP():
  characters = 'abcdefghijklmnopqrstuvwxyz123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^*'
  password = "".join(choice(characters) for x in range(randint(8, 16)))
  try:
    return render_template('index.html', password=password)
  except:
    return 'There was an error'
  

if __name__ == "__main__":
  app.run(debug=True)