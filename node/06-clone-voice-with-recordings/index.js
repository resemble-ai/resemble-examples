import * as Resemble from "@resemble/node"
import fs from 'fs'
import path from 'path'

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

function readFolder(folderPath) {
    const dataList = [];

    // Iterate through files in the folder
    fs.readdirSync(folderPath).forEach(filename => {
        // For each wav file
        if (filename.endsWith(".wav")) {
            // Check if there is a corresponding .txt file
            const txtFilename = filename.replace(".wav", ".txt");
            const txtFilePath = path.join(folderPath, txtFilename);

            // If the pair exists, use it
            if (fs.existsSync(txtFilePath)) {
                // Read the text content from the .txt file
                const textContent = fs.readFileSync(txtFilePath, 'utf-8');

                // Create a dictionary and append to the list
                const fileDict = {
                    file: path.join(folderPath, filename),
                    text: textContent,
                    recordingName: txtFilename
                };

                dataList.push(fileDict);
            } else {
                console.warn(`WARN: Unable to find corresponding transcript txt file for ${filename} - SKIPPING`);
            }
        }
    });

    return dataList;
}

async function uploadRecordings(voiceUuid, recordingsFolder) {
    console.log(`Beginning recording upload process from folder: ${recordingsFolder}`)

    let dataList = readFolder(recordingsFolder)

    let failures = 0
    let success = 0

     for (let num in dataList) {
         let recording = dataList[num]

         console.log(`Attempting to upload recording: ${recording.recordingName}`) 

        const file = fs.createReadStream(recording.file)
        const fileSize = fs.statSync(recording.file).size 

        let response = await Resemble.Resemble.v2.recordings.create(voiceUuid, {
          emotion: 'neutral',
          is_active: true,
          name: recording.recordingName,
          text: recording.text
        }, file, fileSize)

         let item = response.item

         if (response.success) {
             let uuid = item.uuid
             console.log(`Request to create recording ${recording.recordingName} was successful! Recording uuid is ${uuid}`) 

             success += 1
         } else {
             console.log(`Request to create recording ${recording.recordingName} FAILED!`) 
             console.log(response) 

             failures += 1
         }
     }

    console.log(`Recording upload completed, finished uploading ${success} successful and ${failures} failures`)
}

async function createVoice(voiceName) {
  console.log(`Submitting request to Resemble to create a voice: ${voiceName}`);

  try {
    // Make a request to the API, note that we do not provide a callback_uri so this
    // request will execute synchronously.
    //   Make request to the API, note that we do not provide a callback_uri so this 
    //   will request will execute synchronously.
    //  
    //   This will trigger the voice creation process but not the voice building process# we need to trigger that through the voice building API 
    //  
    //   https://docs.app.resemble.ai/docs/resource_voice/build/
    //  
    // 

    let base64Conset = '';

    // In order to clone a voice, you MUST provide a base64 encoded consent file 
    //
    // https://docs.app.resemble.ai/docs/resource_voice/create#voice-consent
    //
    // FIXME: You will need update this function to the path to your consent file
    const fileContents = fs.readFileSync('FIXME: path/to/consent file', 'binary');

    base64Conset = Buffer.from(fileContents).toString('base64')

    console.log(`Submitting request to Resemble to create a voice: ${voiceName}`);

    // Make a request to the API, note that we do not provide a callback_uri so this
    // request will execute synchronously.
    const response = await Resemble.Resemble.v2.voices.create({ name: voiceName, consent: base64Conset });

    const voice = response.item;

    if (response.success) {
      const voiceStatus = voice.status;
      const voiceUuid = voice.uuid;

      console.log(`Response was successful! ${voiceName} has been created with UUID ${voiceUuid}. The voice is currently ${voiceStatus}.`);

        return [voiceUuid, true]
    } else {
      console.log('Response was unsuccessful!');
      // In case of an error, print the error to console
      console.log(response);

      return [undefined, false]
    }
  } catch (error) {
    console.error('An error occurred:', error);

    return [undefined, false]
  }
}

async function triggerVoiceBuild(voiceUuid) {
    let response = await Resemble.Resemble.v2.voices.build(voiceUuid)


    if (response.success) {
        console.log(`Request to initiate voice build for voice ${voice_uuid} was successful!`)
        return true
    } else {
        console.log(`Request to initiate voice build for voice ${voiceUuid} was NOT successful! Response was: `)
        console.log(response) 

        return false
    }
}

async function runExample(args) {
  const [uuid, ok] = await createVoice(args.voiceName);

    if (!ok) {
        console.log("FAILURE: THe process was aborted because the voice was not created")
        throw new Error();
    }

    await uploadRecordings(
        uuid,
        args.recordingsFolder
    )

    let voiceBuildOk = await triggerVoiceBuild(uuid)

    if (!voiceBuildOk) {
        console.log("Failed to trigger voice build")
    }
}


const args = process.argv.slice(2);

// Check if the required number of arguments is provided
if (args.length !== 2) {
  console.error('Usage: node index.js <voice_name> <recordings>');
  process.exit(1);
}

const [voiceName, recordings] = args;

// Command-line arguments
const cloneArgs = {
    voiceName: voiceName, 
    recordingsFolder: recordings
};

runExample(cloneArgs)
