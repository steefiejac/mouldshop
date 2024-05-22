import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd


# Create a connection object.
conn = st.connection("gsheets", type=GSheetsConnection)

# df = conn.read()
df = conn.read(
    worksheet="Moulding",
    ttl="10m",
    # usecols=[0, 1],
    # nrows=3,
)
# print(df)
moulding_parts = pd.DataFrame(df)
moulding_parts = moulding_parts.iloc[15:].reset_index(drop=True)
moulding_parts.columns = moulding_parts.iloc[0]
moulding_parts = moulding_parts[1:].reset_index(drop=True)
# tonparts320 = moulding_parts[moulding_parts["UN320A5 (320t) ShWt=518.5"]==1]["Sinapi Alias"]
# st.write(tonparts320)
# st.write(len(tonparts320))
# [["1. 320ton", "2. 240ton", "3. 200ton", "4. 160ton"], "2. 240ton", "3. 200ton", "4. 160ton"]

def immparts(imm):
    print(imm)
    if imm == "1. 320ton":
        column = "UN320A5 (320t) ShWt=518.5"
    elif imm == "2. 240ton":
        column = "FF240 (240t) ShWt=371"
    elif imm == "3. 200ton":
        column = "FF200 (200t) ShWt=258"
    elif imm == "4. 160ton":
        column = "FF160 (160t) ShWt=159"
    elif imm == "5. 120ton":
        column = "FF120 (120t) ShWt=74"
    elif imm == "6. 120ton":
        column = "UN120A5 (120t) ShWt=71.7"
    elif imm == "7. 120ton":
        column = "UN120A5 (120t) ShWt=246.9" 
    elif imm == "8. 90ton":
        column = "UN90A5 (90t) ShWt=158.7"   
    return list(moulding_parts[moulding_parts[column]==1]["Sinapi Alias"])