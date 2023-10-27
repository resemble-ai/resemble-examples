
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
async function createAudioClip(projectUUID, title, body, voiceUUID, isPublic = false, isArchived = false) {
  console.log(`Submitting request to Resemble to create audio clip content: ${body}`);

  try {
    const response = await Resemble.Resemble.v2.clips.createSync(projectUUID, {
				title: title, 
				voice_uuid: voiceUUID, 
				body: body,
				is_public: isPublic, 
				is_archived: isArchived 
		})

    if (response.success) {
      const clip = response.item;
      const clipUUID = clip.uuid;
      const clipURL = clip.audio_src;

      console.log(`Response was successful! ${title} has been created with UUID ${clipUUID}.`);
      console.log(clipURL);
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
  const title = args.title;
  const body = args.body;
  const isPublic = args.public || false;
  const isArchived = args.archived || false;

  // Run the clip creation function to call the Resemble API
  await createAudioClip(projectUUID, title, body, voiceUUID, isPublic, isArchived);
}

const args = process.argv.slice(2);

// Check if the required number of arguments is provided
if (args.length !== 6) {
  console.error('Usage: node index.js <project_uuid> <voice_uuid> <title> <body> <public (true/false)> <archived (true/false)>');
  process.exit(1);
}

const [projectUUID, voiceUUID, title, body, isPublicStr, isArchivedStr] = args;
const isPublic = isPublicStr === 'true';
const isArchived = isArchivedStr === 'true';

// Command-line arguments
const clipArgs = {
  project_uuid: projectUUID,
  voice_uuid: voiceUUID,
  title: title,
  body: body,
  public: isPublic,
  archived: isArchived,
};

// Call the 'runExample' function with the provided arguments
runExample(clipArgs);
