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

// Function to create an audio clip
async function batchCreateClips(projectUUID, voiceUUID, clipsArray) {

  try {
    const response = await Resemble.Resemble.v2.batch.create(
        projectUUID, 
        voiceUUID, 
        clipsArray,
        {}
    )

    if (response.success) {
      const batch = response.item;
      const batchUUID = batch.uuid;
      const count = batch.total_count;

      console.log(`Response was successful! Batch of ${count} clips has been created with UUID ${batchUUID}.`);
    } else {
      console.log('Response was unsuccessful!');
      console.log(response);
    }
  } catch (error) {
    console.error('Error creating audio clip:', error);
  }
}

// Main function
async function runExample(args) {
  const projectUUID = args.project_uuid;
  const voiceUUID = args.voice_uuid;
  const clips = args.clips;
  const clipsArray = clips.split(',')


  // Run the clip creation function to call the Resemble API
  await batchCreateClips(projectUUID, voiceUUID, clipsArray);
}

const args = process.argv.slice(2);

// Check if the required number of arguments is provided
if (args.length !== 3) {
  console.error('Usage: node index.js <project_uuid> <voice_uuid> <csv-of-clips>');
  process.exit(1);
}

const [projectUUID, voiceUUID, clips] = args;

// Command-line arguments
const batchArgs = {
  project_uuid: projectUUID,
  voice_uuid: voiceUUID,
  clips: clips,
};

// Call the 'runExample' function with the provided arguments
runExample(batchArgs);
