import argparse
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

def create_audio_clip(
        project_uuid: str, 
        title: str, 
        body: str, 
        voice_uuid: str,
        is_public: bool = False, 
        is_archived: bool = False): 

    print(f"Submitting request to Resemble to create audio clip content: {body}")

    # Make request to the API, note that we do not provide a callback_uri so this 
    # will request will execute synchronously.
    response = Resemble.v2.clips.create_sync(
      project_uuid,
      voice_uuid,
      body,
      is_public=is_public,
      is_archived=is_archived,
      title=None,
      sample_rate=None,
      output_format=None,
      precision=None,
      include_timestamps=None,
      raw=None
    )
  

    if response['success']:
        clip = response['item']
        clip_uuid = clip['uuid']
        clip_url = clip['audio_src']

        print(f"Response was successful! {title} has been created with UUID {clip_uuid}.")
        print(clip_url)
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
    title = arguments.get("title")
    body = arguments.get("body")
    public = arguments.get("public", False)
    archived = arguments.get("archived", False)

    # Run the clip creation function to call the Resemble API 
    create_audio_clip(
            project_uuid=project_uuid, 
            title=title, 
            body=body, 
            voice_uuid=voice_uuid, 
            is_public=public, 
            is_archived=archived
            )


# Create an argument parser
parser = argparse.ArgumentParser(description="A script that creates static audio content using Resemble AI")

# Add option flags to the parser
parser.add_argument("--project_uuid", required=True, help="Project UUID to store this clip under")
parser.add_argument("--voice_uuid", required=True, help="Voice UUID to use for this clip content")
parser.add_argument("--title", required=True, help="The title of the clip")
parser.add_argument("--body", required=True, help="The text to synthesize audio content with, can be SSML or plain text")
parser.add_argument("--public", action="store_true", help="Set to make public (default: False)")
parser.add_argument("--archived", action="store_true", help="Set to archive (default: False)")

# Parse the command-line arguments
args = parser.parse_args()

# Create a dictionary of arguments
arguments = {
    "project_uuid": args.project_uuid,
    "voice_uuid": args.voice_uuid,
    "title": args.title,
    "body": args.body,
    "public": args.public,
    "archived": args.archived
}

# Call the 'run_example' function with the provided arguments
if __name__ == '__main__':
    run_example(arguments)
