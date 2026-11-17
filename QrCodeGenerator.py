import qrcode

def generate_qr_code(url, filename):
    img = qrcode.make(url)
    img.save(filename)

if __name__ == "__main__":
    url = "https://b001.io"
    filename = "qr_code.png"

    generate_qr_code(url, filename)

    print(f"QR code saved as {filename}")
