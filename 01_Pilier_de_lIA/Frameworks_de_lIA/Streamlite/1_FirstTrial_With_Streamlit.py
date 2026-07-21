# -- 01 FIRST TRIAL WITH STREAMLIT -- 



# -- SETUP
# -- x-----------------------------------------x --
# Standard libraries
import numpy as np
import pandas as pd


# Visualization libraries
import streamlit as st
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt


# ML libraries
from sklearn.datasets import load_iris

# -- x-----------------------------------------x --



# -- SCRIPT TO CONFIGURE THE LAYOUT
# -- x-----------------------------------------x --
# Configuration of the Streamlit page's layout
st.set_page_config(layout="wide")

# Set titles
st.title("Hello World")
st.subheader("It is a subtitle")

# Add elements withon the sidebare
st.sidebar.title("Sidebar title")
st.sidebar.subheader("This is a sidebar subtitle")

# Add Markdown texte
st.markdown("## Markdown")



# Create 3 columns
c1, _, c2 = st.columns((2, 1, 2))

# Define columns titles
c1.title("Col1 Title")
c2.title("Col2 Title")

# Add containt within the columns
with c1 :
    st.write("Col1 containt")

with c2 : 
    st.write("Col2 containt")


# Create whitespace and separation lines
st.write("##")
st.divider()
st.write("##")

# -- x-----------------------------------------x --




# -- SCRIPT TO DEFINE WIDGETS
# -- x-----------------------------------------x --
# Add title
st.title("Input Widgets")

# Define a widget to fed a number
st.number_input("Number", value=42)

# Create a button that will display a notification when pushed
if st.button("Button"):
    st.toast(f"You clicked on the button!")

# Checkbox that returns a boolean
is_checked = st.checkbox("Check to activate")
st.write(f"Checkbox: {is_checked}")

# Toggle switch (like a check box)
is_toggle = st.toggle("Toggle to activate")
st.write(f"Toggle: {is_toggle}")

# Selectbox to choose an option amoung a list
one_select = st.selectbox("Selectbox", ["Option 1", "Option 2", "Option 3"])
st.write(f"Selectbox: {one_select}")

# Multiselect to choose multiple option amoung a list
multi_select = st.multiselect("Multiselect", ["Option 1", "Option 2", "Option 3"])
st.write(f"Multiselectbox: {multi_select}")

# Create forms with textual fields
with st.form("my_form"):
    text_input = st.text_input("Text input")
    text_area = st.text_area("Text area")
    submit_button = st.form_submit_button("Submit")

# Display values writen in the form
if submit_button:
    st.write(f"text input: {text_input}")
    st.write(f"text area: {text_area}")


# -- x-----------------------------------------x --


# Create whitespace and separation lines
st.write("##")
st.divider()
st.write("##")


# -- DISPLAY GRAPHICS
# -- x-----------------------------------------x --
# Add subheader
st.subheader("Graphics")


# Plotly
# -- x-------------------x --
# Load iris dataset using seaborn
#df = sns.load_dataset("iris")

# Load iris dataset using sklearn
iris = load_iris(as_frame=True)
df = iris.frame

# Generate a graphic to show interactively the dispersion - using PlotlyExpress
fig = px.scatter(df, x="sepal length (cm)", y="sepal width (cm)", color="target")

# Display the graphic
st.plotly_chart(fig)
# -- x-------------------x --


# Matplotlib
# -- x-------------------x --
# Generate sintetical data
X = np.linspace(0, 10, 100)
y = np.sin(X)

# Instantiate a figure
figure = plt.figure()
# Generate the graphic from the function
plt.plot(X, y)
# Display the graphic
st.pyplot(figure)

# -- x-------------------x --


# -- x-----------------------------------------x --



# Create whitespace and separation lines
st.write("##")
st.divider()
st.write("##")


# -- DISPLAY DATAFRAMES
# -- x-----------------------------------------x --
st.subheader("Display DataFrames")


# Generate a DataFrame with random values
df = pd.DataFrame(np.random.randn(50,5), columns=("Colonne %d" % i for i in range(5)))

# Display interactively the DataFrame
st.dataframe(df)
# -- x-----------------------------------------x --


# -- LOAD FILES
# -- x-----------------------------------------x --
# -- x-----------------------------------------x --
