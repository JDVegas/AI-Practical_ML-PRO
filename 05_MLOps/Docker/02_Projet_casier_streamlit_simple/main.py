# -- 02 PROJET CASIER STREAMLIT --



# -- SETUP
# -- x------------------------------x --

# LIBRARIES
# -- x--------------------x --
# Standard libraries
import os

# Visualization libraries
import streamlit as st
# -- x--------------------x --


# PAGE CONFIGURATION
# -- x--------------------x --
st.set_page_config(page_title="App Docker Streamlit")
# -- x--------------------x --


# ENVIRONMENT VARIABLES
# -- x--------------------x --
# PATHS
DATA_FOLDER = "/data"

# -- x--------------------x --


# REPOSITORY ARCHITECTURE
# -- x--------------------x --
# Create the folder if it does not exists
os.makedirs(DATA_FOLDER, exist_ok=True)
# -- x--------------------x --



# -- x------------------------------x --






# -- SCRIPT
# -- x------------------------------x --
st.title("My Docker Locker")


# Define a widget to upload files
uploaded_file = st.file_uploader("Drop a file to upload it")

# IF .. a file have been droped, then save the file into the data file
if uploaded_file:
    # Generate the path where to save the file
    file_path = os.path.join(DATA_FOLDER, uploaded_file.name)
    # Create a file at the indicated location and open it in "write in binary" mode (wb)
    with open (file_path, "wb") as f:
        # Copy the file
        f.write(uploaded_file.getbuffer())
    # Return the user a message 
    st.success(f"File saved in : {file_path}")



st.subheader("Files saved within the volume :")
# Get the paths list of the files within the data folder
files = os.listdir(DATA_FOLDER)

# IF .. there is files within the folder, then display them within the streamlit interface
if files : 
    # Iterate through each element from the list 
    for f in files : 
        st.write(f"- {f}")
# ELSE .. there is no file in the folder
else :
    # Display a message to the user 
    st.info("The folder is empty.")

# -- x------------------------------x --