from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
              margin: 10px 0;
              width: 540px;
              height: 120px;
            }}
        </style>
    </head>
    <body>
      <form method="post">
      <label for="rot">Rotate by</label>
        <input type="text" name="rot" val="0"></input>
        <br><br>
        <textarea name="text">{0}</textarea>
        <br>
        <input type="submit" value="Submit Query"></input>
      </form>
    </body>
</html>"""

@app.route("/")
def index():
    return form.format('')

@app.route("/", methods=['POST'])
def encrypt():
    rotate_by = int(request.form['rot'])
    cypher_this = request.form['text']

    cyphered = rotate_string(cypher_this, rotate_by)
    return form.format(cyphered)
app.run()