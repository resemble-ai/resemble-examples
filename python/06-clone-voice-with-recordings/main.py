from resemble import Resemble
import argparse
import os
import base64

# This function sets up the Resemble Python SDK
def initialize_resemble_client(): 
    try:
        # Attempt to retrieve the value of the environment variable
        resemble_api_key = os.environ['RESEMBLE_API_KEY']

        Resemble.api_key(resemble_api_key)
    except KeyError:
        # If the environment variable is not found, raise an error
        raise EnvironmentError(f"The 'RESEMBLE_API_KEY' environment variable is not set.")

import os

# Read folder pairs
def read_folder(folder_path):
    data_list = []

    # Iterate through files in the folder
    for filename in os.listdir(folder_path):
        # for each wav file
        if filename.endswith(".wav"):
            # Check if there is a corresponding .txt file
            txt_filename = filename.replace(".wav", ".txt")
            txt_filepath = os.path.join(folder_path, txt_filename)

            # if the pair exists use it
            if os.path.exists(txt_filepath):
                # Read the text content from the .txt file
                with open(txt_filepath, 'r') as txt_file:
                    text_content = txt_file.read()

                # Create a dictionary and append to the list
                file_dict = {
                         'file': os.path.join(folder_path, filename), 
                         'text': text_content, 
                         'recording_name': txt_filename
                }

                data_list.append(file_dict)
            else:
                print(f"WARN: Unable to find corresponding transcript txt file for {filename} - SKIPPING")

    return data_list

#
# The voice_uuid is the voice to upload to 
# The recordings_folder is the folder to upload recordings from
#
def upload_recordings(voice_uuid: str, recordings_folder:str):
    print(f"Beginning recording upload process from folder: {recordings_folder}")

    data_list  = read_folder(recordings_folder)

    failures = 0
    success = 0

    for recording in data_list:
        response = Resemble.v2.recordings.create(
                voice_uuid, 
                open(recording['file'],'rb'), 
                recording['recording_name'], 
                recording['text'],
                is_active=True, 
                emotion="neutral"
        )

        if response['success']:
            uuid = response['item']['uuid']

            print(f"Request to create recording {recording['recording_name']} was successful! Recording uuid is {uuid}")
            success+= 1
        else:
            print(f"Request to create recording {recording['recording_name']} was NOT successful!")
            print(response)
            failures+= 1

    print(f"Recording upload completed, finished uploading {success} successful and {failures} failures")

def trigger_voice_build(voice_uuid: str):
    response = Resemble.v2.voices.build(uuid=voice_uuid)

    if response['success']:
        print(f"Request to initiate voice build for voice {voice_uuid} was successful!")
        return True
    else:
        print(f"Request to initiate voice build for voice {voice_uuid} was NOT successful! Response was: ")

        print(response) 

        return False

# INSTRUCTIONS
# 1. Create voice 
# 2. Upload upload_recordings 
# 3. Trigger voice build via /build 

def create_voice(voice_name): 
    print(f"Submitting request to Resemble to create a voice: {voice_name}")

    # Make request to the API, note that we do not provide a callback_uri so this 
    # will request will execute synchronously.
    #
    # This will trigger the voice creation process but not the voice building process# we need to trigger that through the voice building API 
    #
    # https://docs.app.resemble.ai/docs/resource_voice/build/
    #

    # In order to clone a voice, you MUST provide a base64 encoded consent file 
    #
    # https://docs.app.resemble.ai/docs/resource_voice/create#voice-consent
    #
    # FIXME: You will need update this function to the path to your consent file
    with open('FIXME: path/to/consent/file', 'rb') as file:
        file_contents = file.read()

        # Encode the file contents as Base64
        base64_consent = base64.b64encode(file_contents).decode('utf-8')


    print(f"Submitting request to Resemble to create a voice: {voice_name}")

    # Make request to the API, note that we do not provide a callback_uri so this 
    # will request will execute synchronously.
    response = Resemble.v2.voices.create(
            name=voice_name, 
            consent=base64_consent
    )

    voice = response['item']

    if response['success']:
        voice = response['item']
        voice_status = voice['status']
        voice_uuid = voice['uuid']

        print(f"Response was successful! {voice_name} has been created with UUID {voice_uuid}. The voice is currently {voice_status}.")

        return voice_uuid
    else:
        print("Response was unsuccessful!")

        # In case of an error, print the error to STDOUT
        print(response)

        return None


# This is the main function that contains the example
def run_example(arguments):
    # Initialize the client using the environment variable RESEMBLE_API_KEY set
    initialize_resemble_client()

    # Run the voice creation function to call the Resemble API 
    uuid = create_voice(voice_name=arguments['voice_name'])

    if uuid is None:
        print("FAILURE: The process was aborted because the voice was not created")
        exit(1)

    upload_recordings(voice_uuid=uuid, recordings_folder=arguments['recordings_folder'])

    trigger_voice_build(voice_uuid=uuid)


# Create an argument parser
parser = argparse.ArgumentParser(description="A script builds a voice by uploading a set of recordings")

parser.add_argument("--name", required=True, help="The name of the voice to create")
parser.add_argument("--recordings", required=True, help="A path to the folder of recordings in the correct format")

# Parse the command-line arguments
args = parser.parse_args()

# Create a dictionary of arguments
arguments = {
    "voice_name": args.name,
    "recordings_folder": args.recordings,
}

if __name__ == '__main__':
    run_example(arguments)
