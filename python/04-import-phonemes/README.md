# 04. Import Phonemes

This is a repository that provides a basic example of using the `resemble` SDK to import phonemes

## Prerequisites

- Python 3.6 or higher
- pip (Python package manager)

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
- Run the server and provide your API key as an input environment variable:
```
RESEMBLE_API_KEY=... python main.py --csv-file path/to/csvfile
```

