from flask import Flask, request
from caesar import rotate_string

form = """
    <!DOCTYPE html>
    <html>
    <head>
        <style>
        form {
            background-color: #eee;
            padding: 20px;
            margin: 0 auto;
            width: 540px;
            font: 16px sans-serif;
            border-radius: 10px;
        }
        textarea {
          margin: 10px 0;
          width: 540px;
          height: 120px;
        }
        </style>
    </head>
    <body>
        <form action="/" method="POST">
            <label for=a >Rotate by:</label>  
            <input id=a type="text" method="POST" name="rot" value="0"/>
            <textarea name="text"></textarea>
            <input type="Submit" />
        </form>  
    </body>
    </html>
    """
app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return form

@app.route("/", methods=['POST'])
def encrpyt():
    rot = int(request.form['rot'])
    text = request.form['text']
    rotated = rotate_string(text,rot)
    return '<h1>'+ rotated + '</h1>'
    
app.run()