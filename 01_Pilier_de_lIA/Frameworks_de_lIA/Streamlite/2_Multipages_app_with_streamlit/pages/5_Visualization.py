# -- PAGE 5 : VISUALIZATION --



# -- SETUP
# -- x-----------------------------------------x --
# Visualization library
import streamlit as st
import plotly.express as px

# Set page configuration 
st.set_page_config(page_title="Visualization", layout="wide")
# -- x-----------------------------------------x --


st.title("Visualize data")


# -- PAGE CONTAINT
# -- x-----------------------------------------x --
# Check that the dataframe contains at least two numerical columns
if "df" in st.session_state:
    df = st.session_state["df"]

    # Select columns for X and y axes
    numeric_columns = df.select_dtypes(include=["float", "int"]).columns

    # IF .. there is more than two values, then generate a graph
    if len(numeric_columns) >= 2:
        # Extract the values
        x_axis = st.selectbox(
            "Select the column for the X axis"
            , options = numeric_columns
        )

        y_axis = st.selectbox(
            "Select the column for the y axis"
            , options = numeric_columns
        )

        # Generate a graph
        fig = px.scatter(df, x=x_axis, y=y_axis)

        # Display the graph
        st.plotly_chart(fig)

    # ELSE .. the DataFrame has less than 2 numerical columns, then display a warning message to the user
    else :
        st.warning("The CSV file must contains at least TWO numerical columns")
# ELSE .. Ask the user to upload a CSV file
else :
    st.error("No DaraFrame found. Please, upload an CSV file from the Home page.")



# -- x-----------------------------------------x --