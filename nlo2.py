import streamlit as st
import pandas as pd
import openai

# Set your OpenAI API key here
openai.api_key ='sk-proj-zKjHg5MyW4goUWgxP8OgT3BlbkFJ8Qticf0FhLPZxVrdoyQz'  # Replace with your OpenAI API key

# Load the dataset
def load_data(file_path):
    data = pd.read_csv(file_path, encoding='latin1')
    return data

# Function to handle natural language queries using OpenAI
def handle_query(data, query):
    prompt = f"""
    You are an assistant that provides insights based on a dataset. The dataset has the following columns: {', '.join(data.columns)}.

    Here is a brief description of the dataset:
    - The dataset contains sales data for a retail store, including information on orders, products, customers, regions, and more.
    - Key columns include: Order ID, Order Date, Ship Date, Ship Mode, Customer ID, Customer Name, Segment, Country, City, State, Postal Code, Region, Product ID, Category, Sub-Category, Product Name, Sales, Quantity, Discount, Profit.

    Based on this dataset, please answer the following query: {query}
    """

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": query}
        ],
        max_tokens=150
    )
    answer = response.choices[0].text.strip()
    return answer

# Streamlit app for NLP query handling
def main():
    st.title("NLP Query Module Using OpenAI")

    # Upload CSV file
    uploaded_file = st.file_uploader("Upload your Superstore CSV file", type=["csv"])

    if uploaded_file is not None:
        data = load_data(uploaded_file)

        st.subheader("Data Preview")
        st.write(data.head())

        st.subheader("Ask a Question")
        query = st.text_input("Enter your query about the data:", placeholder="e.g., What is the total sales amount?")

        if query:
            st.subheader("Query Response")
            answer = handle_query(data, query)
            st.write(answer)
    else:
        st.write("Please upload a CSV file to proceed.")

if __name__ == "__main__":
    main()
