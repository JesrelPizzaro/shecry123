# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
from cryptography.fernet import Fernet
import hashlib

# Function to encrypt text using Fernet symmetric encryption
def encrypt_text_symmetric(text, key):
    fernet = Fernet(key)
    encrypted_text = fernet.encrypt(text.encode())
    return encrypted_text

# Function to decrypt text using Fernet symmetric encryption
def decrypt_text_symmetric(encrypted_text, key):
    fernet = Fernet(key)
    decrypted_text = fernet.decrypt(encrypted_text).decode()
    return decrypted_text

# Function to hash text using SHA-256 hashing
def hash_text(text):
    hashed_text = hashlib.sha256(text.encode()).hexdigest()
    return hashed_text

def main():
    st.title("Applied Cryptography Application")

    # User input for encryption/decryption
    operation = st.sidebar.selectbox("Select Operation", ("Encrypt", "Decrypt", "Hash"))

    if operation == "Encrypt":
        text = st.text_input("Enter text to encrypt:")
        key = st.text_input("Enter encryption key:")
        if st.button("Encrypt"):
            encrypted_result = encrypt_text_symmetric(text, key)
            st.write("Encrypted Result:", encrypted_result)

    elif operation == "Decrypt":
        encrypted_text = st.text_input("Enter encrypted text:")
        key = st.text_input("Enter decryption key:")
        if st.button("Decrypt"):
            decrypted_result = decrypt_text_symmetric(encrypted_text.encode(), key)
            st.write("Decrypted Result:", decrypted_result)

    elif operation == "Hash":
        text_to_hash = st.text_input("Enter text to hash:")
        if st.button("Hash"):
            hashed_result = hash_text(text_to_hash)
            st.write("Hashed Result:", hashed_result)

if __name__ == "__main__":
    main()
