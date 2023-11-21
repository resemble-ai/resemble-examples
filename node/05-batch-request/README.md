# 05. Creating Multiple Clips with Batching

This is a repository that provides a basic example of using the `@resemble/node` SDK to synthesize synthesize multiple clips using the batch API.

## Build and Usage
- Clone the repository
- Install dependencies
```bash
# Install dependencies
yarn 
```
- Set your `RESEMBLE_API_KEY` and run the NodeJS script.

To run the script, use the following command:

```bash
RESEMBLE_API_KEY=... node index.js <project_uuid> <voice_uuid> <csv-of-clips>

# Example:
# RESEMBLE_API_KEY=... node index.js "abcdef123" "123fedabc" "hello,hi,goodbye"

Response was successful! Batch of 3 clips has been created with UUID deadbeef
```

### Arguments
`project_uuid`: The UUID of the project to use (required).
`voice_uuid`: The UUID of the voice to use (required).
`clips`: A comma-separated list of clip content to create (required).

