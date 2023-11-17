import fs from 'fs';
import csv from 'csv-parser';
import * as Resemble from "@resemble/node"

const apiKey = process.env.RESEMBLE_API_KEY;

if (!apiKey) {
  console.error('Please set the RESEMBLE_API_KEY environment variable.');
  process.exit(1);
}

const setupResembleAI = (apiKey) => {
	console.log("Setting Resemble API Key...")
	Resemble.Resemble.setApiKey(apiKey)
}

setupResembleAI(apiKey)

function importPhonemes(csvFilePath) {
    try {
        fs.createReadStream(csvFilePath)
            .pipe(csv())
            .on('data', async (row) => {
                const word = row.word
                const phoneticTranscription = row.phonetic_transcription

                try {
                    // Make a POST request to create a new widget entry
                    const response = await Resemble.Resemble.v2.phonemes.create(word, phoneticTranscription);

                    if (response.success) {
                        console.log(`Imported phoneme pair: ${word} and ${phoneticTranscription}`);
                    } else {
                        // Failed to import for some reason
                        throw new Error(JSON.stringify(response));
                    }
                } catch (e) {
                    console.error(`ERROR: Could not import phoneme pair: ${word} and ${phoneticTranscription} - ${e.message}`);
                }
            })
            .on('end', () => {
                // Print summary
                console.log(`\nCompleted`);
            });
    } catch (error) {
        console.error(`ERROR: File not found - ${csvFilePath}`);
    }
}
// Main function
async function runMain(args) {
  // Run the clip creation function to call the Resemble API
  await importPhonemes(args.csvFile);
}

const args = process.argv.slice(2);

// Check if the required number of arguments is provided
if (args.length !== 1) {
  console.error('Usage: node index.js <path/to/csv>');
  process.exit(1);
}

const [csvFile] = args;

// Command-line arguments
const mainArgs = {
    csvFile: csvFile
};

runMain(mainArgs);
