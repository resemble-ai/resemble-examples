from resemble import Resemble
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

def create_voice(): 
    voice_name = 'My Voice Clone'

    # The dataset is important, it is the data that will be used to train our voice. 
    # There are two ways to create and train a voice 
    #
    # 1. Providing a dataset URL; or 
    # 2. Uploading individual recordings via the API 
    #
    # https://docs.app.resemble.ai/docs/resource_voice/create
    #
    # Ensure that it is public accessible, otherwise, your Voicebuilding may result in 
    # an error due to Resemble receiving a Forbidden request on attempt to download.
    #
    # FIXME: You will need to change this to a url which points to your dataset as a zip file.
    #
    dataset = 'FIXME: add your dataset URL here!'
    base64_consent = ''

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
            voice_name, 
            dataset_url=dataset, 
            consent=base64_consent
    )

    voice = response['item']

    if response['success']:
        voice = response['item']
        voice_status = voice['status']
        voice_uuid = voice['uuid']

        print(f"Response was successful! {voice_name} has been created with UUID {voice_uuid}. The voice is currently {voice_status}.")
    else:
        print("Response was unsuccessful!")

        # In case of an error, print the error to STDOUT
        print(response)


# This is the main function that contains the example
def run_example():
    # Initialize the client using the environment variable RESEMBLE_API_KEY set
    initialize_resemble_client()

    # Run the voice creation function to call the Resemble API 
    create_voice()


if __name__ == '__main__':
    run_example()
