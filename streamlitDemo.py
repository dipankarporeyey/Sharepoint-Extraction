import time
from SharePointToLocalSystem import sharePointToLocalSystem
from CreateCredential import createCredential
import streamlit as st


# Header
st.title("Sharepoint Extraction Process!🦜")

# Main
#######################################
# st.write("Asking for credentials")
# st.caption('Asking for credentials :blue[colors] and emojis :sunglasses:')
st.caption(':blue[Asking for credentials]')
col1, col2, col3 = st.columns(3)

with col1:
    # Text Input: Client ID
    client_id = st.text_input("Enter Client ID")
with col2:
    # Text Input: Client Sceret Code
    client_secret = st.text_input("Enter Client Secret Code")
with col3:
    # Text Input: File Link
    datafile_link = st.text_input("Enter File Link")
    
local_file_name, dataset_url, site_url = createCredential.detailsCredential(datafile_link)

if st.button("Click here to submit"):
    try:
        st.caption(":blue[Status . . .]")
        with st.status("Downloading data . . .", expanded=True) as status:
            st.caption(":red[Searching for data . . .]")
            time.sleep(2)
            response = sharePointToLocalSystem.SaveLocalSystem(client_id, client_secret, site_url, dataset_url)
            st.caption(":blue[Found URL !]")
            time.sleep(1)
            st.caption(":green[Downloading data . . .]")
            time.sleep(1)
            st.success("File extraction successful✅!")
            status.update(label="Download complete!", state="complete", expanded=True)
        col1, col2 = st.columns(2)
        with col1:
            st.caption(":blue[Received file name:]  "+str(local_file_name))
        with col2:
            st.download_button(label="Click here to download!",
                                data=response,
                                file_name=local_file_name,
                                key='download-button'
                                )
        status.update(label="Download complete!", state="complete", expanded=True)
    except Exception as e:
        st.warning("Please enter correct credentials!", icon="⚠️")
