from flask import Flask

app = Flask(__name__)


@app.route('/')
def index(path):
    return 'Index'


app.run(
#   host='0.0.0.0',
#   port=8080, 
#   debug=True,
)
