from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def helloworld():
    return "404 site not found"

@app.route('/ask', methods=['GET', 'POST'])
def greet():
    name = request.values.get("name")
    return f"Hiiiiiiiiiiiii {name}"


@app.route('/ncss')
def ncss():
    return "<h1>ncss</h1>"

if __name__ == "__main__":
    app.run(debug=True)
    #