from flask import Flask, render_template
app = Flask(__name__)

from blueprints import *

app.register_blueprint(predict_api)

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 