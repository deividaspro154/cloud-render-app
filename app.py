from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Cloud App</title>
    </head>

    <body>
        <h1>Cloud Computing App</h1>

        <button onclick="changeColor()">Change background color</button>

        <script>
            function changeColor() {
                document.body.style.backgroundColor = "lightblue";
            }
        </script>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
