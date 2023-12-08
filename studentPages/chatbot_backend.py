from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import config
import openai

app = FastAPI()

# Set up CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

openai.api_key = config.api_key

@app.post("/get-response/")
async def get_response(request: Request):
    try:
        data = await request.json()
        user_input = data['input']

        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=user_input,
            max_tokens=150
        )
        return response.choices[0].text
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


