import streamlit as st
import pandas as pd
from cryptography.fernet import Fernet

# Generate a key for encryption and decryption

key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Mock user database
USERS = {
    "admin": {"password": "admin_pass", "role": "admin"},
    "user": {"password": "user_pass", "role": "user"},
}

# Function to authenticate users
def authenticate(username, password):
    user = USERS.get(username)
    if user and user["password"] == password:
        return user
    return None

# Function to encrypt sensitive data
def encrypt_data(data):
    return cipher_suite.encrypt(data.encode())

# Function to decrypt sensitive data
def decrypt_data(data):
    return cipher_suite.decrypt(data).decode()

# Function to mask sensitive data
def mask_data(data, visible_chars=4):
    return f"{data[:visible_chars]}{'*' * (len(data) - visible_chars)}"

# Streamlit component for authentication
def auth_component():
    st.sidebar.title("Login")
    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password")
    if st.sidebar.button("Login"):
        user = authenticate(username, password)
        if user:
            st.session_state["user"] = user
            st.sidebar.success(f"Logged in as {username}")
        else:
            st.sidebar.error("Invalid username or password")

# Decorator for role-based access control
def role_required(role):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if "user" not in st.session_state:
                st.error("Please log in to access this page.")
                return
            user = st.session_state["user"]
            if user["role"] != role:
                st.error("You do not have permission to access this page.")
                return
            return func(*args, **kwargs)
        return wrapper
    return decorator

# Function to display user data with masking
def display_user_data(data):
    for col in data.columns:
        if col in ["Customer Name"]:  # Example of sensitive fields
            data[col] = data[col].apply(mask_data)
    st.write(data)

# Streamlit app for data management with authentication
def main():
    if "user" not in st.session_state:
        auth_component()
    else:
        user = st.session_state["user"]
        st.sidebar.title(f"Welcome, {user['role']}")
        if st.sidebar.button("Logout"):
            del st.session_state["user"]
            st.experimental_rerun()

        if user["role"] == "admin":
            st.title("Admin Dashboard")
            st.write("Admin functionalities here.")
        else:
            st.title("User Dashboard")
            st.write("User functionalities here.")

        # Upload CSV file
        uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

        if uploaded_file is not None:
            data = pd.read_csv(uploaded_file, encoding='latin1')

            st.subheader("Data Preview")
            st.write(data.head())

            # Display user data with masking for sensitive information
            st.subheader("User Data with Masked Sensitive Information")
            display_user_data(data)
        else:
            st.write("Please upload a CSV file to proceed.")

if __name__ == "__main__":
    main()
sk-proj-e2JEyJMcb6kBdKGYtkmuT3BlbkFJhXlN4jQea3ZI2Q5AX0tS