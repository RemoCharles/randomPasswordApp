from flask import Flask, render_template, url_for, request, redirect
from random import *


app = Flask(__name__)

@app.route("/")
def index():
  return render_template('index.html')

@app.route("/generate", methods=['POST'])
def randomP():
  lettersUppercase = 'abcdefghijklmnopqrstuvwxyz'
  lettersLowercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  numbers = '123456789'
  characters = '.!@#$%^*'
  password1 = "".join(choice(lettersLowercase + lettersUppercase) for x in range(randint(6, 8)))
  password2 = "".join(choice(lettersLowercase + lettersUppercase + numbers) for x in range(randint(8, 12)))
  password3 = "".join(choice(lettersLowercase + lettersUppercase + numbers + characters) for x in range(randint(12, 18)))
  try:
    if request.form.get("password") == "password1":
      return render_template('index.html', password1=password1)
    elif request.form.get("password") == "password2":
      return render_template('index.html', password2=password2)
    elif request.form.get("password") == "password3":
      return render_template('index.html', password3=password3)
  except:
    return 'There was an error'
  

if __name__ == "__main__":
  app.run(debug=True)