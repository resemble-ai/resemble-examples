# 05. Batch Request

This is a repository that provides a basic example of using the `resemble` SDK to synthesize multiple audio files in a batch request.

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

- Set your `RESEMBLE_API_KEY` and run the python script

To run the script, use the following command:

```bash
python main.py --project_uuid PROJECT_UUID --voice_uuid VOICE_UUID --clips CLIPS
```

### Arguments
`--project_uuid`: The UUID of the project (required).
`--voice_uuid`: The UUID of the voice (required).
`--clips`: A comma-separated list of clip content to create (required).

