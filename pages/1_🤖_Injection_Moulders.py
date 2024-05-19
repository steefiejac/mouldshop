import streamlit as st
import time
import numpy as np

st.set_page_config(page_title="Injection Moulders", page_icon="🤖")

st.markdown("# Injection Moulders")
st.sidebar.header("Injection Moulders")

selected_option = st.selectbox("Select an Machine Option", ["320 Ton", "240 Ton", "200 Ton"])

# Display the selected option
st.write("You selected:", selected_option)

machine_specs = {
    "Machine A": {"Capacity": "100 tons", "Max Shot Size": "200 grams", "Manufacturer": "Manufacturer A"},
    "Machine B": {"Capacity": "150 tons", "Max Shot Size": "300 grams", "Manufacturer": "Manufacturer B"},
    "Machine C": {"Capacity": "200 tons", "Max Shot Size": "400 grams", "Manufacturer": "Manufacturer C"}
}

# Create a dropdown menu to select the injection moulder machine
selected_machine = st.selectbox("Select Injection Moulder Machine", list(machine_specs.keys()))

# Display the selected machine's specifications
if selected_machine:
    st.write("Specifications for", selected_machine)
    st.write("Capacity:", machine_specs[selected_machine]["Capacity"])
    st.write("Max Shot Size:", machine_specs[selected_machine]["Max Shot Size"])
    st.write("Manufacturer:", machine_specs[selected_machine]["Manufacturer"])

    # Add a submission form based on the selected machine
    st.subheader("Submit Form for " + selected_machine)
    with st.form(key='machine_form'):
        # Add form fields
        part_name = st.text_input("Part Name")
        part_quantity = st.number_input("Part Quantity", min_value=1)
        submit_button = st.form_submit_button(label='Submit')

    # Process form submission
    if submit_button:
        # Print submitted form data
        st.write("Submitted Form Data:")
        st.write("Part Name:", part_name)
        st.write("Part Quantity:", part_quantity)

