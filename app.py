from flask import Flask, send_file

import qrcode
import io
import os

app = Flask(__name__)

def make_qr(url, filename):
    img = qrcode.make(url)

    buffer = io.BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)

    return send_file(
        buffer,
        mimetype="image/png",
        download_name=filename
    )

@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>William Melton QR Codes</title>
    </head>
    <body style="font-family:Arial;text-align:center;padding:20px;">
        <h1>William Melton</h1>
        <h2>Business Card QR Codes</h2>

        <p><a href="/linkedin">LinkedIn QR Code</a></p>
        <p><a href="/github">GitHub QR Code</a></p>
        <p><a href="/docker">Docker Hub QR Code</a></p>
        <p><a href="/web">Web Portfolio QR Code</a></p>
        <p><a href="/cyber">Cybersecurity Portfolio QR Code</a></p>
        <p><a href="/twitch">Twitch QR Code</a></p>
    </body>
    </html>
    """

@app.route("/linkedin")
def linkedin():
    return make_qr(
        "https://www.linkedin.com/in/william-melton-080207261/",
        "linkedin_qr.png"
    )

@app.route("/github")
def github():
    return make_qr(
        "https://github.com/alternativemelton975-sudo",
        "github_qr.png"
    )

@app.route("/docker")
def docker():
    return make_qr(
        "https://hub.docker.com/u/thecorvidwarrior",
        "docker_qr.png"
    )

@app.route("/web")
def web():
    return make_qr(
        "https://alternativemelton975-sudo.github.io/Web-Development-Portfolio/",
        "web_portfolio_qr.png"
    )

@app.route("/cyber")
def cyber():
    return make_qr(
        "https://alternativemelton975-sudo.github.io/Cyber-Security-Portfolio/",
        "cyber_portfolio_qr.png"
    )

@app.route("/twitch")
def twitch():
    return make_qr(
        "https://www.twitch.tv/crowsflyingnorth",
        "twitch_qr.png"
    )

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
