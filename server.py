"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']


@app.route("/")
def start_here():
    """Home page."""

    return """<!doctype html>
    <html>
    <a href="/hello"> 
    Hi! This is the home page.</a>
    </html>
    """


@app.route("/hello")
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet" method="GET">
          What's your name? <input type="text" name="person">
          <br>
          Choose a compliment: 
          <input type="radio" name="compliment" value="awesome">Awesome</input>
          <input type="radio" name="compliment" value="terrific">Terrific</input>
          <input type="radio" name="compliment" value="fantastic">Fantastic</input>
          <input type="radio" name="compliment" value="neato">Neato</input>
          <input type="radio" name="compliment" value="fantabulous">Fantabulous</input>
          <input type="radio" name="compliment" value="wowza">Wowza</input>
          <input type="radio" name="compliment" value="oh-so-not-meh">Oh-so-not-meh</input>
          <input type="radio" name="compliment" value="brilliant">Brilliant</input>
          <input type="radio" name="compliment" value="ducky">Ducky</input>
          <input type="radio" name="compliment" value="coolio">Coolio</input>
          <input type="radio" name="compliment" value="incredible">Incredible</input>
          <input type="radio" name="compliment" value="wonderful">Wonderful</input>
          <input type="radio" name="compliment" value="smashing">Smashing</input>
          <input type="radio" name="compliment" value="lovely">Lovely</input>
        <br>
        <input type="submit" value="Submit">
        </form>
        <form action="/diss" method="GET">
        Type out your insult here: <input type="text" name="insult">
        <input type="submit" value="Submit">
        </form>
      </body>
    </html>
    """

#   



@app.route("/greet")
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    compliment = request.args.get("compliment")

    # y = x

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {}! I think you're {}!
      </body>
    </html>
    """.format(player, compliment)


@app.route("/diss")
def diss_person():
    """Dish out an insult"""

    player = request.args.get("person")

    insult = request.args.get("insult")

    return """
    <!doctype html>
    <html>
      <head>
        <title>An Insult</title>
      </head>
      <body>
        Hi, {}! Did you know you're a {}!
      </body>
    </html>
    """.format(player, insult)

    




if __name__ == "__main__":
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")



