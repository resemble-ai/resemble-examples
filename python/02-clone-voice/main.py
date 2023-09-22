from resemble import Resemble
import os

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

    print(f"Submitting request to Resemble to create a voice: {voice_name}")

    # Make request to the API, note that we do not provide a callback_uri so this 
    # will request will execute synchronously.
    response = Resemble.v2.voices.create(voice_name, dataset_url=dataset)

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
