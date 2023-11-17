import os
import argparse
import csv
from resemble import Resemble

# This function sets up the Resemble Python SDK
def initialize_resemble_client(): 
    try:
        # Attempt to retrieve the value of the environment variable
        resemble_api_key = os.environ['RESEMBLE_API_KEY']

        Resemble.api_key(resemble_api_key)
    except KeyError:
        # If the environment variable is not found, raise an error
        raise EnvironmentError(f"The 'RESEMBLE_API_KEY' environment variable is not set.")


def import_phonemes(csv_file_path): 
    # Keep track of successful and failed imports (possibly due to already existing)
    successful_imports = 0
    failed_imports = 0

    try:
        with open(csv_file_path, 'r') as file:
            # Create a CSV reader object
            reader = csv.reader(file)

            # Skip the header row if it exists
            next(reader, None)

            # Iterate over each row in the CSV file
            for row in reader:
                # Ensure the row has at least two elements (word and phonetic_transcription)
                if len(row) >= 2:
                    word, phonetic_transcription = row[0], row[1]

                    try:
                        # Make a POST request to create a new widget entry
                        response = Resemble.v2.phonemes.create(word, phonetic_transcription)
                        if response['success']:
                            successful_imports += 1
                            print(f"Imported phoneme pair: {word} and {phonetic_transcription}")
                        else:
                            # Failed to import for some reason
                            raise Exception(response)

                    except Exception as e:
                        failed_imports += 1

                        print(f"ERROR: Could not import phoneme pair: {word} and {phonetic_transcription} - {e}")

    except FileNotFoundError:
        print(f"ERROR: File not found - {csv_file_path}")

    # Print summary
    print(f"\nCompleted\nSuccessfully imported phonemes: {successful_imports}\nFailed to import phonemes: {failed_imports}")

# This is the main function that contains the example
def run_main(arguments):
    # Initialize the client using the environment variable RESEMBLE_API_KEY set
    initialize_resemble_client()
    # Run the voice creation function to call the Resemble API 
    import_phonemes(arguments['csv_file'])

parser = argparse.ArgumentParser(description="A script that imports phonemes using Resemble AI")

# Add option flags to the parser
parser.add_argument("--csv-file", required=True, help="The CSV file containing phonemes to import")

# Parse the command-line arguments
args = parser.parse_args()

arguments = { 'csv_file': args.csv_file }

if __name__ == '__main__':
    run_main(arguments)
