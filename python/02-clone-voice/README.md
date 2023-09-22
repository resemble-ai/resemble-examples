# 01. Fetch Projects

This is a repository that provides a basic example of using the `resemble` SDK to fetch projects.

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
RESEMBLE_API_KEY=... python main.py
```

- Use the `curl` utility to request the `/projects` endpoint 

```
curl localhost:5000/projects

{
  "success": true,
  "page": 1,
  "num_pages": 2,
  "page_size": 11,
  "items": [
    {
      "uuid": "abcdef",
      "name": "My Project",
      "description": "My first project description",
      "created_at": "2023-07-25T16:35:11.689Z",
      "updated_at": "2023-08-28T13:48:21.617Z",
      "is_public": false,
      "is_collaborative": true,
      "is_archived": false
    },
    {
      "uuid": "deadbeef",
      "name": "My Second Project",
      "description": "My second project description",
      "created_at": "2023-05-23T19:37:38.348Z",
      "updated_at": "2023-06-26T17:10:52.957Z",
      "is_public": false,
      "is_collaborative": false,
      "is_archived": true
    }
  ]
}

```

## Getting Started

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/flask-json-api-server.git
   cd flask-json-api-server
Create a virtual environment to isolate dependencies:

bash
Copy code
Running the Server
To start the Flask API server, run the following command from the project's root directory:

bash
Copy code
python main.py
The server will start and listen on http://localhost:5000. You can access the health check endpoint at http://localhost:5000/ping.

Stopping the Server
To stop the server, press Ctrl + C in the terminal where the server is running.
