# -- PAGE 2 : SELECTOR --





# -- SETUP
# -- x-----------------------------------------x --
# Visualization library
import streamlit as st

# Set page configuration 
st.set_page_config(page_title="Selection", layout="wide")
# -- x-----------------------------------------x --





# -- PAGE CONTAINT
# -- x-----------------------------------------x --
st.title("Selection Page")

# Associate a selector within the session
# -- x-------------------------x --
# IF .. the selector key name does not exist, then create it and initialize a list as value
if 'selection' not in st.session_state:
    st.session_state.selection = []
# -- x-------------------------x --

# Define a specific space to display the current selection
selection_placeholder = st.empty()


# Define the selector
option = st.selectbox(
    "Choose an option to add"
    # Define the options that can be selected
    , ["Option A", "Option B", "Option C", "Option D"]
    , key="add_selectbox"
)


# Add an option to the list
# -- x-------------------------x --
st.subheader("Add an option")

# Define a button to add the selected option within the selection list associated to the session
if st.button("Add to the selection", key="add_button"):
    # IF .. option does not already exist within the list, then add it
    if option not in st.session_state.selection:
        st.session_state.selection.append(option)
        # Return a success message to the user
        st.success(f"Option '{option}' have been properly added to the selection")
    # ELSE .. the option already exists within the list, then return a warning message 
    else :
        st.warning(f"Option '{option}' already is within the selection")
# -- x-------------------------x --



# Remove an option from the list
# -- x-------------------------x --
st.subheader("Remove an option")

# IF .. a option have been selected then .. 
if st.session_state.selection:

    # .. create a new selectbox
    remove_option = st.selectbox(
        'Choose a selection to remove',
        # The list of option is based on the current selected options
        st.session_state.selection,
        key='remove_selectbox'
    )

    # Create a button to remove a selected option from the new selectbox
    if st.button('Remove from the selection', key='remove_button'):
        st.session_state.selection.remove(remove_option)
        st.success(f'Option "{remove_option}" have been properly removed from the selection.')


# ELSE .. indicate that no option have been removed
else:
    st.info('No option have been removed')



# -- x-------------------------x --



# Update current selection displayer
# -- x-------------------------x --
# IF .. a selection exists, then display it
if st.session_state.selection:
    selection_placeholder.write("##### Current selection :")
    selection_placeholder.write(st.session_state.selection)

# ELSE .. indicate that no option have been selected
else:
    selection_placeholder.write("##### Current selection : no option selected")
# -- x-------------------------x --

