import streamlit as st
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# Load the dataset
def load_data(file_path):
    data = pd.read_csv(file_path, encoding='latin1')
    return data

# Preprocess data for clustering
def preprocess_data(data):
    numerical_features = ['Sales', 'Quantity', 'Discount', 'Profit']
    data_numerical = data[numerical_features]
    scaler = StandardScaler()
    data_scaled = scaler.fit_transform(data_numerical)
    return data_scaled

# Apply KMeans clustering
def apply_kmeans(data, n_clusters=5):
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    clusters = kmeans.fit_predict(data)
    return clusters, kmeans

# Generate insights based on clusters
def generate_insights(data, clusters):
    data['Cluster'] = clusters
    insights = []
    for cluster in data['Cluster'].unique():
        cluster_data = data[data['Cluster'] == cluster]
        cluster_insight = {
            'Cluster': cluster,
            'Total Sales': cluster_data['Sales'].sum(),
            'Average Discount': cluster_data['Discount'].mean(),
            'Total Profit': cluster_data['Profit'].sum(),
            'Order Count': cluster_data['Order ID'].nunique()
        }
        insights.append(cluster_insight)
    return insights

# Display insights in Streamlit app
def display_insights(insights):
    for insight in insights:
        st.write(f"Cluster {insight['Cluster']}:")
        st.write(f"  Total Sales: ${insight['Total Sales']:,.2f}")
        st.write(f"  Average Discount: {insight['Average Discount']:.2%}")
        st.write(f"  Total Profit: ${insight['Total Profit']:,.2f}")
        st.write(f"  Order Count: {insight['Order Count']}")
        st.write("")

# Streamlit app for data analysis and insights generation
def main():
    st.title("Analysis and Insights Generation Module")

    # Upload CSV file
    uploaded_file = st.file_uploader("Upload your Superstore CSV file", type=["csv"])

    if uploaded_file is not None:
        data = load_data(uploaded_file)

        st.subheader("Data Preview")
        st.write(data.head())

        n_clusters = st.slider("Select number of clusters", min_value=2, max_value=10, value=5)

        # Preprocess data
        data_scaled = preprocess_data(data)

        # Apply KMeans clustering
        clusters, kmeans = apply_kmeans(data_scaled, n_clusters)

        # Generate insights
        insights = generate_insights(data, clusters)

        # Display insights
        st.subheader("Generated Insights")
        display_insights(insights)
    else:
        st.write("Please upload a CSV file to proceed.")

if __name__ == "__main__":
    main()
