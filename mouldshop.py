import streamlit as st
from google.cloud import firestore
# from google.auth import service_account
from google.oauth2 import service_account
import json

st.set_page_config(
    page_title="Sinapi",
    page_icon="👷🏼‍♂️",
)

st.write("# Welcome Stephan to the Sinapi Mouldshop Management 👋")

# Authenticate to Firestore with the JSON account key.
# db = firestore.Client.from_service_account_json("mouldshop_key.json")
# Install the dependency: e.g., pip install google-auth-oauthlib

key_dict = json.loads(st.secrets["textkey"])
creds = service_account.Credentials.from_service_account_info(key_dict)
db = firestore.Client(credentials=creds, project="mouldshop-management")

# Create a reference to the Google post.
doc_ref = db.collection("320ton").document("Iz9lWxifLYCnrikrBE0K")

# Then get the data at that reference.
doc = doc_ref.get()

# Let's see what we got!
st.write("The id is: ", doc.id)
st.write("The contents are: ", doc.to_dict())
# st.sidebar.success("Select a demo above.")

 #new code 
 
# This time, we're creating a NEW post reference for Apple
doc_ref = db.collection("320ton").document("new-random-id")

# And then uploading some data to that reference
doc_ref.set({
    "circulator-on" : True,

    "circulator-temp" : 25,

    "part-name" : "TUB017",

    "reject-parts" :5,

    "unit-weight-kg" : 500,

    "wastage-kg" : 20,
})
# st.markdown(
#     """
#     Streamlit is an open-source app framework built specifically for
#     Machine Learning and Data Science projects.
#     **👈 Select a demo from the sidebar** to see some examples
#     of what Streamlit can do!
#     ### Want to learn more?
#     - Check out [streamlit.io](https://streamlit.io)
#     - Jump into our [documentation](https://docs.streamlit.io)
#     - Ask a question in our [community
#         forums](https://discuss.streamlit.io)
#     ### See more complex demos
#     - Use a neural net to [analyze the Udacity Self-driving Car Image
#         Dataset](https://github.com/streamlit/demo-self-driving)
#     - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
# """
# )