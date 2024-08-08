import streamlit as st
import numpy as np
import pandas as pd

# Load data from a CSV file
data = pd.read_csv("divorce.csv")

# Display dataset information (data types, non-null counts, etc.)
info = data.info()
st.text("Dataset Information:")
st.text(info)

# Display the entire dataframe in your Streamlit app
st.subheader("Complete DataFrame")
st.dataframe(data)  # Allows users to explore the data interactively
st.write(data)      # Another way to display the dataframe, similar to st.dataframe()

# Display a static table with a random sample of 3 rows from the data
st.subheader("Sample Data (Static View)")
data_sample_3 = data.sample(3)
st.table(data_sample_3)

# Displaying metrics: positive and negative examples
st.subheader("Metric Examples")

# Example of a metric with a positive delta
st.metric(label="Metric Positive Label", value=30, delta=20, 
          delta_color="normal", help="This is Ahmad")  # Delta shows a positive change

# Example of a metric with a negative delta
st.metric(label="Metric Negative Label", value=data['income_man'].mean().round(2), delta=-20, 
          delta_color="normal", help="This is negative Ahmad")  # Delta shows a negative change

# Additional filtering and sorting functionality can be added below
# For example, sorting the dataframe by a specific column or searching for specific data
