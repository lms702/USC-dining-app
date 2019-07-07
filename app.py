from flask import Flask, render_template, send_file

app = Flask(__name__)

@app.route('/')
def home():
	return("<h1>Welcome to the USC Dining App homepage!</h1>")

if __name__ == "__main__":
  app.run()