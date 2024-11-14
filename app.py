import streamlit as st
from PIL import Image
import io
import hashlib

# Function to encrypt and decrypt the image using XOR
def xor_encrypt_decrypt(data, key):
    key = key.encode('utf-8')
    return bytes([b ^ key[i % len(key)] for i, b in enumerate(data)])

# Function to hash the password
def hash_password(password):
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

# Hardcoded credentials (for demonstration purposes)
USERNAME = "admin"
PASSWORD = hash_password("password")

# Streamlit application
st.title("Image Encryption and Decryption Tool")

# Login form
if 'logged_in' not in st.session_state:
    st.subheader("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == USERNAME and hash_password(password) == PASSWORD:
            st.session_state.logged_in = True
            st.success("Logged in successfully!")
        else:
            st.error("Invalid username or password.")
            
else:
    # If logged in, show the main application
    st.success("Welcome to the Image Encryption and Decryption Tool!")

    # File uploader for image
    uploaded_file = st.file_uploader("Upload your image file", type=["jpg", "jpeg", "png"])

    # Input for encryption key
    key = st.text_input("Enter Encryption Key", type="password")

    if uploaded_file is not None and key:
        # Read the image
        image = Image.open(uploaded_file)
        buffered = io.BytesIO()
        image.save(buffered, format="PNG")
        img_data = buffered.getvalue()

        # Encrypt the image
        encrypted_data = xor_encrypt_decrypt(img_data, key)
        
        # Save encrypted data to a file
        st.download_button(
            label="Download Encrypted Image",
            data=encrypted_data,
            file_name="encrypted_image.enc",
            mime="application/octet-stream"
        )
        st.success("Image encrypted successfully!")

    # File uploader for encrypted image
    uploaded_file_enc = st.file_uploader("Upload your .enc file", type=["enc"])

    if uploaded_file_enc is not None:
        # Read the encrypted file
        encrypted_data = uploaded_file_enc.read()

        # Input for decryption key
        key_decrypt = st.text_input("Enter Decryption Key", type="password")

        if st.button("Decrypt Image"):
            if key_decrypt:  # Check if key is provided
                try:
                    # Decrypt the image
                    decrypted_data = xor_encrypt_decrypt(encrypted_data, key_decrypt)

                    # Load the decrypted image
                    image = Image.open(io.BytesIO(decrypted_data))
                    st.image(image, caption="Decrypted Image", use_container_width=True)

                    # Provide a download button for the decrypted image
                    st.download_button(
                        label="Download Decrypted Image",
                        data=decrypted_data,
                        file_name="decrypted_image.png",
                        mime="image/png"
                    )
                    st.success("Image decrypted successfully!")
                except Exception as e:
                    st.error(f"Error decrypting image: {str(e)}")
            else:
                st.error("Please enter a decryption key.")