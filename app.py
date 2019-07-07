from flask import Flask, render_template, send_file

app = Flask(__name__)

@app.route('/')
def home():
	return("<h1>Welcome to the USC Dining App homepage!</h1>")

@app.route('/getrektdhivya')
def getrekt():
	return('<h2 style="text-align:center">Guess who just launched their first heroku app</h2>')

if __name__ == "__main__":
  app.run()