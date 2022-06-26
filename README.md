# Overview
This project includes a Django application that creates a simple REST API for counting words on a web page. It's written in Python. The REST API is implemented via the `djangorestframework` library. There are two endpoints available:
 - `/words_counter`
 - `/health`
  
The rationale for choosing this tech stack is as follows. Since this is a backend applicaiton, the REST API model seems appropriate - it's the most common way of building interfaces. Likewise, Django is one of the most popular backend frameworks allowing us to create a web server and define REST APIs using the `djangorestframework` library. The constraint was to use Docker and, based on the understanding of the assignment, to be able to launch the web app without using cloud services.

An alternative approach would be to use cloud-native services (if allowed) in a serverless architecture for example defining the APIs in the AWS API Gateway service and implementing the web page processing logic in AWS Lambda but that would require having an AWS account.

## `/words_counter` endpoint
This endpoint returns a JSON object with a list of different words on a webpage and their count. It accepts POST requests with the following payload:

```
{
    "url": "http://bbc.co.uk",
    "sort_method": "word_count"
}
```

- The `url` key is for the URL of the website that you would like to count the words on.
- `sort_method` is an **optional** key that specifies how to sort the results. The following options are supported:
  - `word_count` - sorts by the count of words in descending order
  - `alphabetical` - sort the words in alphabetical order
  - This key can also be omitted

Sample response for bbc.co.uk sorted by word count (truncated):
```
[
	["attribution", 64],
	["bbc", 38],
	["the", 32],
	["to", 17],
	["a", 17],
	["video", 14],
	["with", 14],
	["of", 13],
	["in", 10],
	["tennis", 9],
	["is", 9],
	["for", 8],
	["radio", 8],
	["and", 8],
	["his", 8],
	["food", 7],
	["wimbledon", 7]
]
```
Example on how to send a request to the endpoint assuming you've made Django available at localhost:8000:
```
curl -X POST -H "Content-Type: application/json" \
    -d '{"url": "http://bbc.co.uk","sort_method": "word_count"}' \
    http://localhost:8000/words_counter/
```

## `/health` endpoint
This endpoint reports the health of the application. If you open the http://localhost:8000/health/ page in the browser you should see a System status page with a few green checks. If something is wrong with the application this page will either not load or some checks will not be green. It can also be queried programmatically.

# Environment Variables
The `SECRET_KEY` environment variable needs to be set for Django app to work. It has not been comitted to the repo as it's a secret. You can set it to any value for the purpose of launching this app. If you are launching the app inside the Docker container you can provide set the variable as part of the `docker run` command. See details below.
# Docker
The application has been containerised so you can build it via the provided Dockerfile and then run it. The Dockerfile will install all the necessary dependencies and launch the Django app.
# Prerequisites & Dependencies
You only need Docker installed to be able to launch the app inside a Docker container. Below is a list of dependencies that come into play inside the container:

- Python 3.9+
- Various Python packages including Django as defined in `requirements.txt`
- Docker
# How to Work with This Repo
Follow these steps to launch the Django app:
1. Checkout the repo
2. `docker build -t words_counter .` 
3. `docker run --rm -it -p 8000:8000 -e SECRET_KEY=123 words_counter`. After this step, the app should be available at `localhost:8000`
4. `curl -X POST -H "Content-Type: application/json" \
    -d '{"url": "http://bbc.co.uk","sort_method": "word_count"}' \
    http://localhost:8000/words_counter/`

# To Do
- Unit testing using Pytest as an example
- Test coverage using pytest-cov as an example
- Better error handling
- Implement result pagination if the page has a huge amount of words
