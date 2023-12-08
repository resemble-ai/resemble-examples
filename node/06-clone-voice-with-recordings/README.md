# 06. Clone Voice with Recordings

This is a repository that provides a basic example of using the `@resemble/node` SDK to clone a voice using the recording API and voice API.

## Prerequisites

- node >18.17
- A folder containing at least 20 WAVE files and transcripts of those files in the following format:

```bash 
$ tree 

example-data/
├── wav-1.txt
├── wav-1.wav
├── wav-2.txt
└── wav-2.wav

... additional files

```

## Usage
- Clone the repository
- Install dependencies via `yarn`
- Run the program 
```
 RESEMBLE_API_KEY=... node index.js <voice-name-goes-here> <path-to-recording-folder-goes-here> 
```

