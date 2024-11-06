from flask import Flask, render_template, request, send_from_directory
import qrcode
import os

app = Flask(__name__)

# Function to generate the QR code
def generate_qr(data):
    qr = qrcode.make(data)
    qr_path = os.path.join('static', 'qr_code.png')
    qr.save(qr_path)
    return qr_path

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        qr_type = request.form["qr_type"]
        
        # Handle text, link, email, phone
        if qr_type in ["text", "link", "email", "phone"]:
            data = request.form["data"]
            qr_path = generate_qr(data)

        # Handle PDF and image files
        elif qr_type in ["pdf", "image"]:
            file = request.files["file"]
            filename = os.path.join('static', file.filename)
            file.save(filename)
            qr_path = generate_qr(filename)

        return render_template("index.html", qr_code=True)

    return render_template("index.html", qr_code=False)

# Route for downloading the QR code
@app.route("/download")
def download():
    return send_from_directory('static', 'qr_code.png', as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
