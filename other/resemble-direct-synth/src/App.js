import React, { useState } from 'react';
import './App.css';

function App() {
  const [name, setName] = useState('');
  const [voice, setVoice] = useState('');
  const [response, setResponse] = useState('');
  const [audio, setAudio] = useState('');

  // const resembleApiKey = 'YOUR_RESEMBLE_API_KEY'; // Replace with your Resemble API key
  // const resembleDirectSynEndpoint = 'your-direct-syn-endpoint'; // Replace with your Resemble direct syn url

  const resembleApiKey = 'fEgdNEdGy30SWKYWQazEPwtt'; // Replace with your Resemble API key
  const resembleDirectSynEndpoint ='https://p.cluster.resemble.ai/synthesize' ; // Replace with your Resemble direct syn url

	const decodeB64 = (input) => {
		return Buffer.from(input, 'base64').toString('utf-8');
	}

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
			console.log("Making request... " + resembleDirectSynEndpoint)

      const response = await fetch(resembleDirectSynEndpoint, {
        method: 'POST',
				mode: 'cors', // Set request mode to 'no-cors'
        headers: {
					"Content-Type": "application/json",
          'Authorization': `Bearer ${resembleApiKey}`,
					'Accept-Encoding': "gzip, deflate, br",
					'Access-Control-Allow-Origin': '*'
        },
        body: JSON.stringify({
          text: `Hello, ${name}!`, // Customize the text here
          voice: voice, // Replace with the voice ID you want to use
        }),
      });


      if (!response.ok) {
				setResponse("Request failed check logs")
				console.log(response)
        throw new Error('Failed to fetch audio');
      }

			const data = await response.json()

			setResponse(data)
			setAudio(decodeB64(data.audio_content))
    } catch (error) {
      console.error('Error:', error);
    }
  };

  return (
    <div className="center-div">
      <h1>Resemble Direct Synthesis</h1>
      <h2>Enter Your Name</h2>
			{ response  && (
					<pre>
						{ response }
					</pre>
				)
			}

      <form onSubmit={handleSubmit}>
        <label htmlFor="nameInput">Name:</label>
        <input
          type="text"
          id="nameInput"
          placeholder="Your Name"
          required
          value={name}
          onChange={(e) => setName(e.target.value)}
        />
				<br/>
        <label htmlFor="voiceInput">Voice UUID:</label>
        <input
          type="text"
          id="voiceInput"
          placeholder="uuid"
          required
          value={voice}
          onChange={(e) => setVoice(e.target.value)}
        />
				<br/>
        <button type="submit">Submit</button>
      </form>
		</div>
  );
}

export default App;
