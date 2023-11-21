import argparse
from resemble import Resemble
from typing import List
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

def batch_create_clips(
        project_uuid: str, 
        clips: List[str], 
        voice_uuid: str): 

    # Make request to the API, note that we do not provide a callback_uri so this 
    # will request will execute synchronously.
    response = Resemble.v2.batches.create(
        project_uuid, 
        voice_uuid, 
        body=clips,
        sample_rate=None,
        output_format=None,
        precision=None
    )

    if response['success']:
        batch = response['item']
        batch_uuid = batch['uuid']
        count = batch['total_count']

        print(f"Response was successful! Batch of {count} clips has been created with UUID {batch_uuid}.")
    else:
        print("Response was unsuccessful!")

        # In case of an error, print the error to STDOUT
        print(response)


# This is the main function that contains the example
def run_example(arguments):
    # Initialize the client using the environment variable RESEMBLE_API_KEY set
    initialize_resemble_client()

    project_uuid = arguments.get("project_uuid")
    voice_uuid = arguments.get("voice_uuid")
    clips_arg = arguments.get("clips")

    clips = clips_arg.split(',')

    # Run the clip creation function to call the Resemble API 
    batch_create_clips(
            project_uuid=project_uuid, 
            clips=clips, 
            voice_uuid=voice_uuid, 
            )


# Create an argument parser
parser = argparse.ArgumentParser(description="A script that creates static audio clips using the Resemble AI Batch API")

# Add option flags to the parser
parser.add_argument("--project_uuid", required=True, help="Project UUID to store this clip under")
parser.add_argument("--voice_uuid", required=True, help="Voice UUID to use for this clip content")
parser.add_argument('--clips', required=True, help='A comma-separated list of clip body content')

# Parse the command-line arguments
args = parser.parse_args()

# Create a dictionary of arguments
arguments = {
    "project_uuid": args.project_uuid,
    "voice_uuid": args.voice_uuid,
    "clips": args.clips
}

# Call the 'run_example' function with the provided arguments
if __name__ == '__main__':
    run_example(arguments)
