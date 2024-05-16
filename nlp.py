import streamlit as st
import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Download NLTK data files
nltk.download('punkt')
nltk.download('stopwords')

# Load the dataset
def load_data(file_path):
    data = pd.read_csv(file_path, encoding='latin1')
    return data

# Function to handle natural language queries
def handle_query(data, query):
    tokens = word_tokenize(query.lower())
    filtered_words = [word for word in tokens if word not in stopwords.words('english')]

    if 'total' in filtered_words and 'sales' in filtered_words:
        total_sales = data['Sales'].sum()
        return f"The total sales amount is ${total_sales:,.2f}."
    elif 'average' in filtered_words and 'discount' in filtered_words:
        avg_discount = data['Discount'].mean()
        return f"The average discount is {avg_discount:.2%}."
    elif 'total' in filtered_words and 'profit' in filtered_words:
        total_profit = data['Profit'].sum()
        return f"The total profit is ${total_profit:,.2f}."
    elif 'order' in filtered_words and 'count' in filtered_words:
        order_count = data['Order ID'].nunique()
        return f"The total number of orders is {order_count}."
    elif 'unique' in filtered_words and 'customers' in filtered_words:
        unique_customers = data['Customer ID'].nunique()
        return f"The total number of unique customers is {unique_customers}."
    else:
        return "I'm sorry, I didn't understand your query. Please try asking something else."

# Streamlit app for NLP query handling
def main():
    st.title("NLP Query Module")

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
