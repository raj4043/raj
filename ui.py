import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

# Load the dataset
def load_data(file_path):
    data = pd.read_csv(file_path, encoding='latin1')
    return data

# Function to create visualizations
def create_visualizations(data):
    st.subheader("Data Visualizations")

    # Sales by Category
    fig1 = px.bar(data, x='Category', y='Sales', color='Category', title='Sales by Category')
    st.plotly_chart(fig1)

    # Profit by Region
    fig2 = px.bar(data, x='Region', y='Profit', color='Region', title='Profit by Region')
    st.plotly_chart(fig2)

    # Sales and Profit over Time
    data['Order Date'] = pd.to_datetime(data['Order Date'])
    sales_profit_time = data.groupby(data['Order Date'].dt.to_period('M')).agg(
        {'Sales': 'sum', 'Profit': 'sum'}).reset_index()
    sales_profit_time['Order Date'] = sales_profit_time['Order Date'].dt.to_timestamp()
    fig3, ax1 = plt.subplots()
    ax2 = ax1.twinx()
    ax1.plot(sales_profit_time['Order Date'], sales_profit_time['Sales'], color='g', label='Sales')
    ax2.plot(sales_profit_time['Order Date'], sales_profit_time['Profit'], color='b', label='Profit')
    ax1.set_xlabel('Date')
    ax1.set_ylabel('Sales', color='g')
    ax2.set_ylabel('Profit', color='b')
    ax1.set_title('Sales and Profit over Time')
    st.pyplot(fig3)

# Streamlit app for data visualization
def main():
    st.title("UI and Visualization Module")

    # Upload CSV file
    uploaded_file = st.file_uploader("Upload your Superstore CSV file", type=["csv"])

    if uploaded_file is not None:
        data = load_data(uploaded_file)

        st.subheader("Data Preview")
        st.write(data.head())

        # Visualize data
        create_visualizations(data)
    else:
        st.write("Please upload a CSV file to proceed.")

if __name__ == "__main__":
    main()
