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
from sklearn.ensemble import RandomForestClassifier
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
# Instatiate the loading file widget
uploaded_file = st.file_uploader("Choose a CSV file")

# IF .. a file is uploaded then read it
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)
# ELSE .. no file is uploaded then display a message 
else : 
    st.info("Please, upload a CSV file to display data")
# -- x-----------------------------------------x --




# Create whitespace and separation lines
st.write("##")
st.divider()
st.write("##")




# -- SCRIPT TO USE ML
# -- x-----------------------------------------x --
st.subheader("Prediction using a ML model")

# Load data
# -- x-------------------x --
# Load iris dataset using sklearn
iris = load_iris(return_X_y=True)
X = iris[0]
y = iris[1]

# Extract the class names
iris_bunch = load_iris(as_frame=True) # Type "Bunch"
target_names = iris_bunch.target_names # Type np.array
# -- x-------------------x --

# Instantiate the mode
clf = RandomForestClassifier()

# Train the model
clf.fit(X, y)


# User interface for the model input - Sidebar
# -- x-------------------x --
#  Separate title within the sidebar
st.sidebar.divider()
st.sidebar.subheader("ML model input parameters")

# Slider to get model caracteristics
sepal_lenght = st.sidebar.slider(
    "Sepal length"
    , float(X[:, 0].min())
    , float(X[:, 0].max())
    , float(X[:, 0].mean())
)

sepal_width = st.sidebar.slider(
    "Sepal width"
    , float(X[:, 1].min())
    , float(X[:, 1].max())
    , float(X[:, 1].mean())
)

petal_lenght = st.sidebar.slider(
    "Petal length"
    , float(X[:, 2].min())
    , float(X[:, 2].max())
    , float(X[:, 2].mean())
)

petal_width = st.sidebar.slider(
    "Petal width"
    , float(X[:, 3].min())
    , float(X[:, 3].max())
    , float(X[:, 3].mean())
)

# Button to launch prediction
start_prediction = st.sidebar.button("Predict")
# -- x-------------------x --



# User interface for the model input - Mainwindow
# -- x-------------------x --
st.write("##")
st.subheader("Use ML model")

# Prediction part
# -- x--------x --
# IF .. the button have been pushed then activate protocol
if start_prediction : 
    # Create a table containing input values
    input_data = [[sepal_lenght, sepal_width, petal_lenght, petal_width]]
    # Predict the flower class
    prediction = clf.predict(input_data)
    # Get each class probability
    prediction_proba = clf.predict_proba(input_data)

    # Display the results
    st.write(f"##### -> Predicted class: {target_names[prediction][0]}")
    st.write("##### -> Probabilities")
    st.write(prediction_proba)
# -- x--------x --

# -- x-------------------x --

# -- x-----------------------------------------x --


# Create whitespace and separation lines
st.write("##")
st.divider()
st.write("##")










# -- ADVANCED TECHNICS -- 
##########################################


# -- USE HTML and CSS
# -- x-----------------------------------------x --
st.subheader("Use HTML and CSS")


# Inject personalised CSS to increase a text size
st.markdown(
    """
    <style>
        .grand-texte {
            font-size:50px !important;
        }
    </style>
    """
    , unsafe_allow_html=True
)

# Create an HTML tag using the CSS caracteristic
st.markdown('<p class="grand-texte">Text en grand</p>', unsafe_allow_html=True)
# -- x-----------------------------------------x --



# Create whitespace and separation lines
st.write("##")
st.divider()
st.write("##")



# -- USE CACHE
# -- x-----------------------------------------x --
st.subheader("Use CACHE")

# Use cache to temporary store loaded data
# -- x-------------------x --
# The cache expire after 60 seconds
@st.cache_data(ttl=60) # ttl = time to leave
def load_data():
    # Simulate data loading
    data = {"values":[1, 2, 3, 4, 5]}
    return data

# Call function to load data
data = load_data()
# Display data
st.write(data)
# -- x-------------------x --


# Use cache to temporary store loaded model
# -- x-------------------x --
@st.cache_data
def train_model():
    # Simulate a costly model training
    clf = RandomForestClassifier(n_estimators=100)
    clf.fit(X,y)
    return clf

# Call the function to train de model
clf = train_model()


# -- x-------------------x --


# -- x-----------------------------------------x --




# Create whitespace and separation lines
st.write("##")
st.divider()
st.write("##")



# -- USE SESSION
# -- x-----------------------------------------x --
st.subheader("Use session")


# Initialise a counter within the session
if "counter" not in st.session_state:
    st.session_state.counter = 0

# IF .. the button is pushed, then increment the counter
if st.button("Increment"):
    st.session_state.counter += 1

# Display the counter value
st.write(f"Counter value: {st.session_state.counter}")

# -- x-----------------------------------------x --


