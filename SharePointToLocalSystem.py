from office365.sharepoint.client_context import ClientContext
from office365.runtime.auth.client_credential import ClientCredential
from office365.sharepoint.files.file import File

class sharePointToLocalSystem:
    def __init__(self):
        pass
    
    @staticmethod
    def extraction(site_url, dataset_url, client_id, client_secret):
        client_credentials = ClientCredential(client_id, client_secret)
        ctx = ClientContext(site_url).with_credentials(client_credentials)
        response = File.open_binary(ctx, dataset_url)
        return response
        
    @staticmethod
    def SaveLocalSystem(client_id, client_secret, site_url, dataset_url):
        client_id = client_id # open(str(username),"r").read().strip("\n")
        client_secret = client_secret # open(str(psswrd),"r").read().strip("\n")
        
        # Create the local path and ready it for save
        # file_path_temp = file_path.replace('\\', '/')
        # local_path = file_path_temp + '/' + file_name
        
        # Get response
        response = sharePointToLocalSystem.extraction(site_url, dataset_url, client_id, client_secret)

        return response.content
        # # Write files in our local system via local path
        # with open(local_path, "wb") as local_file:
        #     local_file.write(response.content)
        # # print("Successfully compiled!")