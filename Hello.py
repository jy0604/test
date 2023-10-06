import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load your CSV data
df = pd.read_csv('toy_dataset.csv')

# Group the data
gen_med = df.groupby(['City', 'Gender'])['Income'].mean().reset_index(name='count')

# Create a Streamlit app
st.title("Average Income Per City by Gender")

# Create a bar plot
fig, ax = plt.subplots(figsize=(10, 5))

# Customize the plot
ax.bar(gen_med['City'], gen_med['count'])
ax.set_xlabel("Average Income Per City")
ax.set_ylabel("Average Income")
ax.set_title("City")
plt.xticks(rotation=45, horizontalalignment='right')

# Display the plot in Streamlit
st.pyplot(fig)
