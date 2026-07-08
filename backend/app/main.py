from fastapi import FastAPI
from app.agents.core import CompanionAgent


app = FastAPI(
    title="AI Companion"
)


agent = CompanionAgent()


@app.get("/")
def root():

    return {
        "status":"AI Companion running"
    }


@app.post("/chat")
async def chat(message:str):

    response = await agent.chat(
        message
    )

    return {
        "reply":response
    }
