
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload

from apiclient import errors
from apiclient.http import MediaFileUpload
import webbrowser
# ...

def update_file(service, file_id, new_title, new_description, new_mime_type,
                new_filename, new_revision):
  """Update an existing file's metadata and content.

  Args:
    service: Drive API service instance.
    file_id: ID of the file to update.
    new_title: New title for the file.
    new_description: New description for the file.
    new_mime_type: New MIME type for the file.
    new_filename: Filename of the new content to upload.
    new_revision: Whether or not to create a new revision for this file.
  Returns:
    Updated file metadata if successful, None otherwise.
  """
  try:
    # First retrieve the file from the API.
    file = service.files().get(fileId=file_id).execute()
    
    # File's new metadata.
    file['title'] = new_title
    file['description'] = new_description
    file['mimeType'] = new_mime_type
    
    
    # File's new content.
    media_body = MediaFileUpload(
        new_filename, mimetype=new_mime_type, resumable=True)

    # Send the request to the API.
    print(file_id)
    print(file)
    print(media_body)
    del file["id"]
    updated_file = service.files().update(
        fileId = file_id, 
        body=file,    
        media_body=media_body).execute()
    print("complete")
    return updated_file
  except (errors.HttpError):
    print ('An error occurred: %s'% error)
    return None



# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/drive.metadata.readonly", 
"https://www.googleapis.com/auth/drive.file"]


def main():
  """Shows basic usage of the Drive v3 API.
  Prints the names and ids of the first 10 files the user has access to.
  """
    
  webbrowser.register("termux-open '%s'", None)





  creds = None
  # The file token.json stores the user's access and refresh tokens, and is
  # created automatically when the authorization flow completes for the first
  # time.
  if os.path.exists("token.json"):
    creds = Credentials.from_authorized_user_file("token.json", SCOPES)
  # If there are no (valid) credentials available, let the user log in.
  if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
      creds.refresh(Request())
    else:
      flow = InstalledAppFlow.from_client_secrets_file(
          "credentials.json", SCOPES
      )
      creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open("token.json", "w") as token:
      token.write(creds.to_json())

  try:
    service = build("drive", "v3", credentials=creds)

   
    file_id = "17akztcEzV24Vp5GDZWzKjc-z9zyfXMi6"
    update_file(service, file_id, "hello.txt", "description", 'application/json', "uploadme.txt", False)

  except HttpError as error:
    # TODO(developer) - Handle errors from drive API.
    print(f"An error occurred: {error}")


if __name__ == "__main__":
  main()
