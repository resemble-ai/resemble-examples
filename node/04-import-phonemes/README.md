# 04. Import Phonemes

This is a repository that provides a basic example of using the `@resemble/node` SDK to import phonemes from a CSV.

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
RESEMBLE_API_KEY=... node index.js <path/to/csv>

# Example:
# RESEMBLE_API_KEY=... node index.js "example.csv"
# 
#
# Imported phoneme pair: vodaphone and voduhphone
# Imported phoneme pair: cosmic and kozmik
#
# Completed
```

### Arguments
`csvFile`: A path to the CSV file to use in the following format:

```
word,phonetic_transcription
vodaphone,voduhphone
cosmic,kozmik
```
