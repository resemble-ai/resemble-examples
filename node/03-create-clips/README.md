# 03. Synthesize Audio Content

This is a repository that provides a basic example of using the `@resemble/node` SDK to synthesize audio content.

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
RESEMBLE_API_KEY=... node index.js <project_uuid> <voice_uuid> <clip_title> <clip_body> <is_public> <is_archived> 

# Example:
# RESEMBLE_API_KEY=... node index.js "abcdef123" "123fedabc" "Clip Title" "Clip Body" false false 

# Submitting request to Resemble to create audio clip content: Clip Body
# Response was successful! Clip Title has been created with UUID abcdef12345.
```

### Arguments
`project_uuid`: The UUID of the project to use (required).
`voice_uuid`: The UUID of the voice to use (required).
`clip_title`: The title of your clip (required).
`clip_body`: The body of your clip (required).
`is_public`: Set this flag to make the item public (default: False).
`is_archived`: Set this flag to archive the item (default: False).

