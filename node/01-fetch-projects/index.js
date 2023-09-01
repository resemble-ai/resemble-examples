import express from 'express';
import * as Resemble from "@resemble/node"

const app = express();
const PORT = 4000;

const apiKey = process.env.RESEMBLE_API_KEY;

if (!apiKey) {
  console.error('Please set the RESEMBLE_API_KEY environment variable.');
  process.exit(1);
}

console.log(Resemble) 

const setupResembleAI = (apiKey) => {
	// TODO
	console.log("Setting Resemble API Key...")
	Resemble.Resemble.setApiKey(apiKey)
}

setupResembleAI(apiKey)

app.use(express.json());

app.get('/ping', (req, res) => {
  res.json({ message: 'pong' });
});

app.get('/projects', async (req, res) => {
	const resp = await Resemble.Resemble.v2.projects.all(1, 11) 

  res.status(201).json(resp);
});

setupResembleAI(apiKey)

app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
