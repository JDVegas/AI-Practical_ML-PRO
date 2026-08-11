# -- SECOND PAGE : STATISTICS --





# -- SETUP
# -- x-----------------------------------------x --

# Load libraries
# -- x-------------------------x --
# Standard libraries
import sys
from pathlib import Path
from typing import Dict, List
import pandas as pd

# Visualization libraries
import streamlit as st
# -- x-------------------------x --

# Load functions
# -- x-------------------------x --
# Manually force project modules path
root_dir = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(root_dir))

from Modules.app_initialization import app_initialization, init_config_page
import Modules.crud_functions_cards_table as cfct 
import Modules.crud_functions_themes_table as cftt
# -- x-------------------------x --


# Configure page
# -- x-------------------------x --
st.set_page_config(page_title="Flashcards", layout='wide')

# Initialize app
app_initialization()
# -- x-------------------------x --






# -- x-----------------------------------------x --





# -- PAGE CONTAINT
# -- x-----------------------------------------x --


# -- x-----------------------------------------x --
