# Image Encryption and Decryption Tool

This is a simple web application built with Streamlit that allows users to encrypt and decrypt images using a basic XOR encryption method. The application includes a login feature for added security.

## Features

- **User Authentication**: Secure login with hardcoded credentials.
- **Image Upload**: Upload images in JPG, JPEG, or PNG formats for encryption.
- **Encryption**: Encrypt images using a user-defined key.
- **Decryption**: Decrypt previously encrypted images using the same key.
- **Download Options**: Download both encrypted and decrypted images.

## Technologies Used

- [Streamlit](https://streamlit.io/) - A framework for building web applications in Python.
- [Pillow](https://pillow.readthedocs.io/en/stable/) - A Python Imaging Library (PIL) fork for image processing.
- [hashlib](https://docs.python.org/3/library/hashlib.html) - A built-in Python library for hashing passwords.

## Installation

To run this application locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/SaiGawand12/image-encryption-tool.git
   cd image-encryption-tool
   ```

2. **Install the required packages: Make sure you have Python installed, then run**:
   ```bash
   pip install streamlit Pillow
   ```

3. **Run the application**:
   ```bash
   streamlit run app.py
   ```
This will start the Streamlit server, and you can access the application in your web browser at <http://localhost:8501>

**Note:** This application uses a hardcoded username and password for simplicity. In a real-world application you should use a secure method to store and verify user credentials.

## Usage
1. **Login**: Enter the username and password to access the application. The default credentials are:

Username: **admin**
Password: **admin**

2. **Upload Image**: Select an image file to encrypt or decrypt.

3. **Encrypt**: Enter a key to encrypt the image. The encrypted image will be displayed below

4. **Decrypt**: Enter the same key used for encryption to decrypt the image. The decrypted image
will be displayed below.

5. **Download**: Download the encrypted or decrypted image.

**Encrypt an Image**:

* Upload an image file (JPG, JPEG, or PNG).
* Enter an encryption key.
* Click on "Download Encrypted Image" to save the encrypted file.

**Decrypt an Image**:

* Upload the encrypted .enc file.
* Enter the decryption key (same as the encryption key).
* Click on "Decrypt Image" to view the decrypted image and download it.


## Security Note
This application uses hardcoded credentials for demonstration purposes. For production use, consider implementing a more secure authentication method and storing user credentials securely.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments
* Thanks to the Streamlit community for their excellent documentation and support.
* Special thanks to the contributors of the Pillow library for their work on image processing in Python.
