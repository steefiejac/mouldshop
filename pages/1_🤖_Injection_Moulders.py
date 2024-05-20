import streamlit as st
import time
import numpy as np
import uuid 
from google.cloud import firestore
from google.oauth2 import service_account
import json

key_dict = json.loads(st.secrets["textkey"]["textkey"]) #json.loads(st.secrets["textkey"])
print("here is textkey ")
print(key_dict)
creds = service_account.Credentials.from_service_account_info(key_dict)
db = firestore.Client(credentials=creds, project="mouldshop-management")

st.set_page_config(page_title="Injection Moulders", page_icon="🤖")

st.markdown("# Injection Moulders")
st.sidebar.header("Injection Moulders")

st.title("Form Input for Dictionary")

    # Define the dictionary keys and their corresponding input types
input_fields = {
        "circulator-on": {"label": "Circulator On", "type": "boolean"},
        "circulator-temp": {"label": "Circulator Temperature (°C)", "type": "number"},
        "part-name": {"label": "Part Name", "type": "text"},
        "reject-parts": {"label": "Reject Parts", "type": "number"},
        "unit-weight-kg": {"label": "Unit Weight (kg)", "type": "number"},
        "wastage-kg": {"label": "Wastage (kg)", "type": "number"}
    }

# Create form inputs dynamically based on the dictionary
form_data = {}
for key, value in input_fields.items():
    print(key)
    input_type = value["type"]
    print(input_type)
    label = value["label"]
    print(label)

    if input_type == "boolean":
        form_data[key] = st.checkbox(label, key=key)
    elif input_type == "number":
        form_data[key] = st.number_input(label, key=key)
    elif input_type == "text":
        form_data[key] = st.text_input(label, key=key)

    
if st.button("Submit"):
    document_id = str(uuid.uuid4())
    doc_ref = db.collection("320ton").document(document_id)
    doc_ref.set(form_data)   

        # Display the submitted form data
    st.write("Submitted Form Data:", form_data)
        
