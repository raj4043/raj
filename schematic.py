import streamlit as st
import pandas as pd

# Load the dataset
def load_data(file_path):
    data = pd.read_csv(file_path, encoding='latin1')
    return data

# Basic query handling function
def handle_query(data, query):
    query = query.lower()

    if 'total sales' in query:
        total_sales = data['Sales'].sum()
        return f"The total sales amount is ${total_sales:,.2f}."
    elif 'average discount' in query:
        avg_discount = data['Discount'].mean()
        return f"The average discount is {avg_discount:.2%}."
    elif 'total profit' in query:
        total_profit = data['Profit'].sum()
        return f"The total profit is ${total_profit:,.2f}."
    elif 'order count' in query:
        order_count = data['Order ID'].nunique()
        return f"The total number of orders is {order_count}."
    elif 'unique customers' in query:
        unique_customers = data['Customer ID'].nunique()
        return f"The total number of unique customers is {unique_customers}."
    else:
        return "I'm sorry, I didn't understand your query. Please try asking something else."

# Function to provide data context
def data_context():
    context = """
    The Superstore dataset contains sales data for a retail store, including information on orders, products, customers, regions, and more.
    Key columns include:
    - Order ID: Unique identifier for each order
    - Order Date: The date when the order was placed
    - Ship Date: The date when the order was shipped
    - Ship Mode: The mode of shipment
    - Customer ID: Unique identifier for each customer
    - Customer Name: Name of the customer
    - Segment: The market segment the customer belongs to
    - Country: The country where the order was placed
    - City: The city where the order was placed
    - State: The state where the order was placed
    - Postal Code: The postal code of the shipping address
    - Region: The region where the order was placed
    - Product ID: Unique identifier for each product
    - Category: The category of the product
    - Sub-Category: The sub-category of the product
    - Product Name: Name of the product
    - Sales: The sales amount
    - Quantity: The quantity of products ordered
    - Discount: The discount applied to the order
    - Profit: The profit from the order
    """
    return context

# Streamlit component for the semantic layer
def semantic_layer_component():
    st.title("Semantic Layer for Data Interpretation")

    # Load data
    data = load_data('Superstore.csv')

    # Display data context
    st.subheader("Data Context")
    st.write(data_context())

    # User query
    query = st.text_input("Enter your query about the data:", placeholder="e.g., What is the total sales amount?")

    if query:
        # Generate response
        st.subheader("Query Response")
        answer = handle_query(data, query)
        st.write(answer)

if __name__ == "__main__":
    semantic_layer_component()
