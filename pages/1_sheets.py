import streamlit as st
import time
import numpy as np
import uuid 
from google.cloud import firestore
from google.oauth2 import service_account
import json
from streamlit_gsheets import GSheetsConnection
st.set_page_config(page_title="Injection Moulders", page_icon="🤖")

st.markdown("# Example sheets")
st.sidebar.header("Example sheets")

st.title("Lets get cooking")



# Create a connection object.
conn = st.connection("gsheets", type=GSheetsConnection)

# df = conn.read()
df = conn.read(
    worksheet="Moulding",
    ttl="10m",
    usecols=[0, 1],
    nrows=3,
)

# Print results.
for row in df.itertuples():
    st.write(row)