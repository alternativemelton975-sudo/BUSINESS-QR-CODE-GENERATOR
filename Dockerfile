FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir qrcode[pil]

CMD ["python", "QrCodeGenerator.py"]
