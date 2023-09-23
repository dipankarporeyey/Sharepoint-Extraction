# import os
from SharePointToLocalSystem import sharePointToLocalSystem
from CreateCredential import createCredential
import streamlit as st

# Header
st.title("Sharepoint Extraction Process!🦜")

# Text Input
client_id = st.text_input("Enter Client ID")

# Text Input
client_secret = st.text_input("Enter Client Secret Code")

# Text Input
datafile_link = st.text_input("Enter File Link")
local_file_name, dataset_url, site_url = createCredential.detailsCredential(datafile_link)

# Text Input
# local_file_path = os.getcwd() # st.text_input("Enter Client ID")

if st.button("Submit"):
    with st.spinner("In progress..."):
        try:
            response = sharePointToLocalSystem.SaveLocalSystem(client_id, client_secret, site_url, dataset_url)
            col1, col2 = st.columns(2)
            with col1:
                st.write("File extraction successfully!")
            with col2:
                st.write("Received file name:  "+str(local_file_name))
            with col1:
                st.write("Click to download the received file!")
            # Create a download button
            # csv_data = df.to_csv(index=False).encode()
            with col2:
                st.download_button(label="Download file",
                                data=response,
                                file_name=local_file_name,
                                key='download-button'
                                )
            # st.write("Please find the required file in the local path:  "+str(local_file_path))
            # st.write(local_file_path)
        except Exception as e:
            st.write("Please enter correct credentials. Thank you!")
    # st.write("Received File: "+str(local_file_name))




