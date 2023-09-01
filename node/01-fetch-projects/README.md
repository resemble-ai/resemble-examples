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

