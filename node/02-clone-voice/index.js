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


async function createVoice() {
  const voiceName = 'My Voice Clone (Node)';

  // The dataset is important; it is the data that will be used to train our voice.
  // There are two ways to create and train a voice:
  //
  // 1. Providing a dataset URL; or
  // 2. Uploading individual recordings via the API
  //
  // https://docs.app.resemble.ai/docs/resource_voice/create
  //
  // Ensure that it is publicly accessible; otherwise, your Voicebuilding may result in
  // an error due to Resemble receiving a Forbidden request on an attempt to download.
  //
  // FIXME: You will need to change this to a URL that points to your dataset as a zip file.
  //
  const dataset = 'FIXME: Adds your dataseturl here';

  console.log(`Submitting request to Resemble to create a voice: ${voiceName}`);

  try {
    // Make a request to the API, note that we do not provide a callback_uri so this
    // request will execute synchronously.
    const response = await Resemble.Resemble.v2.voices.create({ name: voiceName, dataset_url: dataset });

    const voice = response.item;

    if (response.success) {
      const voiceStatus = voice.status;
      const voiceUuid = voice.uuid;

      console.log(`Response was successful! ${voiceName} has been created with UUID ${voiceUuid}. The voice is currently ${voiceStatus}.`);
    } else {
      console.log('Response was unsuccessful!');
      // In case of an error, print the error to console
      console.log(response);
    }
  } catch (error) {
    console.error('An error occurred:', error);
  }
}

// Execute the voice creation
createVoice()
