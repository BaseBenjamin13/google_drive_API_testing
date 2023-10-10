from __future__ import print_function

import google.auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# setup credentials 
# https://cloud.google.com/docs/authentication/provide-credentials-adc#how-to

# if new session developer must rerun cmd: 
#   $env:GOOGLE_APPLICATION_CREDENTIALS="C:\Code\morpheus\Drive_API_testing\drive-api-testing-400801-72f8278a7522.json"

def create_folder():
    """
    Load pre-authorized user credentials from the environment.
    TODO(developer) - See https://developers.google.com/identity
    for guides on implementing OAuth2 for the application.
    """
    creds, _ = google.auth.default()

    try:
        # create drive api client
        service = build('drive', 'v3', credentials=creds)
        file_metadata = {
            'name': 'api_folder_test',
            'mimeType': 'application/vnd.google-apps.folder'
        }

        # pylint: disable=maybe-no-member
        file = service.files().create(body=file_metadata, fields='id').execute()
        print(F'Folder ID: "{file.get("id")}".')
        return file.get('id')

    except HttpError as error:
        print(F'An error occurred: {error}')
        return None


if __name__ == '__main__':
    create_folder()