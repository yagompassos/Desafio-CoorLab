from flask import *

app = Flask(__name__)

@app.route("/")
def test():
    return 200


if __name__ == "__main__":
    app.run(port=3000)