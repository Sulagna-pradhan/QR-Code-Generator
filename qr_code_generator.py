import qrcode

# Function to generate a QR code image
def generate_qr(data: str, filename: str):
    qr = qrcode.QRCode(
        version=1,  # Version can be between 1 to 40, controls the size of the QR code
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,  # Size of each box in the QR code grid
        border=4,  # Size of the border
    )
    qr.add_data(data)  # Add the data (text, URL, etc.)
    qr.make(fit=True)

    # Create an image from the QR code
    img = qr.make_image(fill='black', back_color='white')
    img.save(filename)  # Save the image as a file
    return filename
