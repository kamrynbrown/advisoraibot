# advisoraibot

To be able to use the chatbot, you must have OpenAI and FastAPI installed on your computer.
**Note**: You need to have Python installed on your computer to use pip.

### OpenAI
- `pip show openai`: This command will show details about the OpenAI package if it's installed, including its version. If it's not installed, this command won't return any details.

- `pip install openai`: This command will download and install the latest version of the OpenAI Python package.

### FastAPI
- `pip show fastapi`: This command will display details about the FastAPI package if it is installed on your computer, including its version number. If FastAPI is not installed, this command won't return any details.

- `pip install fastapi`: This command will download and install the latest version of FastAPI.

- `pip install uvicorn` : This server is used to run your FastAPI application. Once both FastAPI and Uvicorn are installed, you can develop and run FastAPI web applications on your local machine.

### Using the Chatbot
Provide your own OpenAI API key in the studentPages directory; place it in a file named config.py.
In config.py, the only thing in it should be (with your API key in the ""):
api_key = ""

Once you have all these packages and files ready: open a terminal, cd to the studentPages directory, then run the following command:
`uvicorn chatbot_backend:app`

This command runs the FastAPI server. As long as the server is running, the chatbot will work on all the sites.

