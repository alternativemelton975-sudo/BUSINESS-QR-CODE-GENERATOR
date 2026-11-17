from flask import Flask, send_file
import qrcode
import io
import os

app = Flask(__name__)

@app.route("/")
def generate_qr():
    url = "https://b001.io"

    img = qrcode.make(url)

    img_buffer = io.BytesIO()
    img.save(img_buffer, format="PNG")
    img_buffer.seek(0)

    return send_file(
        img_buffer,
        mimetype="image/png",
        download_name="qr_code.png"
    )

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
