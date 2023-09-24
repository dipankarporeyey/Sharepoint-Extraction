# import os
from SharePointToLocalSystem import sharePointToLocalSystem
from CreateCredential import createCredential
import streamlit as st

# Header
#######################################
st.sidebar.title("Asking for credential")

# Text Input
client_id = st.sidebar.text_input("Enter Client ID")

# Text Input
client_secret = st.sidebar.text_input("Enter Client Secret Code")

# Text Input
datafile_link = st.sidebar.text_input("Enter File Link")
local_file_name, dataset_url, site_url = createCredential.detailsCredential(datafile_link)

# Text Input
# local_file_path = os.getcwd() # st.text_input("Enter Client ID")
if st.sidebar.button("Click here to submit"):
    st.sidebar.success("Checking . . .", icon="✅")
##########################################

st.title("Sharepoint Extraction Process!🦜")

# if st.button("Submit"):
with st.spinner("File extraction in progress..."):
    try:
        response = sharePointToLocalSystem.SaveLocalSystem(client_id, client_secret, site_url, dataset_url)
        with st.status("Downloading data . . .", expanded=True) as status:
            st.write("Searching for data . . .")
            time.sleep(2)
            st.write("Found URL !")
            time.sleep(1)
            st.write("Downloading data . . .")
            time.sleep(1)
            st.download_button(label="Click here to download!",
                               data=response,
                               file_name=local_file_name,
                               key='download-button'
                              )
            status.update(label="Download complete!", state="complete", expanded=True)
        
        st.button('Rerun')
        col1, col2 = st.columns(1)
        with col1:
            st.write("File extraction successfully!")
        with col2:
            st.write("Received file name:  "+str(local_file_name))
        # with col1:
        #     st.write("Click to download the received file!")
        # Create a download button
        # csv_data = df.to_csv(index=False).encode()
        # with col2:
        #     st.download_button(label="Download file",
        #                     data=response,
        #                     file_name=local_file_name,
        #                     key='download-button'
        #                     )
        # st.write("Please find the required file in the local path:  "+str(local_file_path))
        # st.write(local_file_path)
    except Exception as e:
        st.write("Please enter correct credentials ⚠️. Thank you!")
# st.write("Received File: "+str(local_file_name))




