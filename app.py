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
        <button onclick="changeImage()">Change background image</button>

        <script>
            function changeColor() {
                document.body.style.backgroundImage = "none";
                document.body.style.backgroundColor = "lightblue";
            }

            function changeImage() {
                document.body.style.backgroundImage =
                    "url('https://t4.ftcdn.net/jpg/00/90/76/59/360_F_90765953_xgLAsm6N7VZD1zMlO9CA8t7qwBpZ4lSr.jpg')";

                document.body.style.backgroundSize = "cover";
            }
        </script>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
