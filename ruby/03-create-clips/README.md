# 03. Synthesize Audio Content

This is a repository that provides a basic example of using the `resemble` SDK to synthesize audio content.

## Build and Usage
- Clone the repository
- Install dependencies
```bash
# Install dependencies
bundle 
```
- Set your `RESEMBLE_API_KEY` and run the Ruby script.

To run the script, use the following command:

```bash
RESEMBLE_API_KEY=... bundle exec ruby main.rb --project_uuid <project_uuid> --voice_uuid <voice_uuid> --title <clip_title> --body <clip_body>

# Submitting request to Resemble to create audio clip content: Clip Body
# Response was successful! Clip Title has been created with UUID abcdef12345.
```

### Arguments
`--project_uuid`: The UUID of the project to use (required).
`--voice_uuid`: The UUID of the voice to use (required).
`--title`: The title of your clip (required).
`--body`: The body of your clip (required).
`--public`: Set this flag to make the item public (default: False).
`--archived`: Set this flag to archive the item (default: False).
