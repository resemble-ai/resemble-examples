# 01. Fetch Projects

This is a repository that provides a basic example of using the `@resemble/node` SDK to fetch projects

## Usage
- Clone the repository
- Install dependencies via `yarn`
- Run the server and provide your API key as an input environment variable:
```
yarn 
```
- Run the server 
```
RESEMBLE_API_KEY=... yarn start

# 
# => Server is running on port 4000
```
- Use the `curl` utility to request the `/projects` endpoint 

```
curl localhost:4000/projects


```

