from flask import Flask, render_template, request, send_file
import os
from qr_code_generator import generate_qr  # The file where your QR code generation function resides

app = Flask(__name__)

# Route to display the form and accept user input
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data = request.form['data']  # User input from the form
        if data:
            # Generate the QR code from the input data
            filename = 'static/qr_code.png'  # Save the image in the static folder
            generate_qr(data, filename)
            return render_template('index.html', qr_image=filename)  # Show QR code on the webpage
    return render_template('index.html', qr_image=None)

# Route to serve the generated QR code image for download
@app.route('/download')
def download():
    return send_file('static/qr_code.png', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
