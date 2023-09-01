# 01. Fetch Projects

This is a repository that provides a basic example of using the `resemble` Ruby SDK to fetch projects.

## Build and Usage
- Clone the repository
- Install dependencies via `bundle`
- Run the server and provide your API key as an input environment variable:
```
RESEMBLE_API_KEY=... bundle exec ruby main.rb
```

- Use the `curl` utility to request the `/projects` endpoint 

```
curl localhost:4567/projects

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
