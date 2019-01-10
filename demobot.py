from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/')
def helloworld():
    return "404 site not found"

@app.route('/ask', methods=['GET', 'POST'])
def greet():
    text = request.post()
    return f"Hiiiiiiiiiiiii {text}"


@app.route('/ncss')
def ncss():
    return "<h1>ncss</h1>"

if __name__ == "__main__":
    app.run(debug=True)
    #