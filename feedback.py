import streamlit as st
import pandas as pd
import os

# Load the dataset
def load_data(file_path):
    data = pd.read_csv(file_path, encoding='latin1')
    return data

# Function to capture and store user feedback
def capture_feedback(insight_id, feedback):
    feedback_file = 'feedback.csv'
    feedback_data = {'Insight ID': [insight_id], 'Feedback': [feedback]}
    feedback_df = pd.DataFrame(feedback_data)

    if os.path.exists(feedback_file):
        feedback_df.to_csv(feedback_file, mode='a', header=False, index=False)
    else:
        feedback_df.to_csv(feedback_file, mode='w', header=True, index=False)

    st.success("Thank you for your feedback!")

# Streamlit app for capturing feedback
def main():
    st.title("Feedback and Continuous Learning Module")

    # Upload CSV file
    uploaded_file = st.file_uploader("Upload your Superstore CSV file", type=["csv"])

    if uploaded_file is not None:
        data = load_data(uploaded_file)

        st.subheader("Data Preview")
        st.write(data.head())

        # Display insights for feedback
        st.subheader("Provide Feedback on Insights")
        for i in range(5):  # For simplicity, let's assume we display 5 insights
            st.write(f"Insight ID: {i}, Insight: Example insight {i}")
            feedback = st.text_input(f"Enter your feedback for Insight ID {i}:", key=f"feedback_{i}")
            if st.button(f"Submit Feedback for Insight ID {i}", key=f"submit_feedback_{i}"):
                capture_feedback(i, feedback)
    else:
        st.write("Please upload a CSV file to proceed.")

if __name__ == "__main__":
    main()
