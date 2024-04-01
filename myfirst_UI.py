import streamlit as st
import qrcode
from PIL import Image
import io

def generate_qr(data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    buffered = io.BytesIO()
    img.save(buffered, format="PNG")
    return buffered.getvalue()

def main():
    st.title("QR Code Generator")
    user_input = st.text_input("Enter the URL or text for the QR code:")

    if user_input:
        qr_code_img = generate_qr(user_input)
        st.image(qr_code_img, caption='Generated QR Code', use_column_width=True)

if __name__ == "__main__":
    main()
