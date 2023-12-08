# 06. Clone Voice with Recordings

This is a repository that provides a basic example of using the `resemble` SDK to clone a voice using the recordings API and voice API.

## Prerequisites

- Python 3.6 or higher
- pip (Python package manager)
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

## Build and Usage
- Clone the repository
- Create virtual environment and install dependencies:
```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```
- Run the program and provide your API key as an input environment variable:
```
# FIXME:
RESEMBLE_API_KEY=... python main.py --name <name> --recordings path/to/folder
```

