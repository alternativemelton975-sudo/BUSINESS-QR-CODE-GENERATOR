from flask import Flask, send_file
import qrcode
import io
import os

app = Flask(__name__)

@app.route("/")
def qr():
    img = qrcode.make("https://b001.io")

    buffer = io.BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)

    return send_file(buffer, mimetype="image/png")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
