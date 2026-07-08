from app.models.router import get_model


class CompanionAgent:

    def __init__(self):

        self.model = get_model()


    async def chat(self, message: str):

        response = await self.model.chat(
            message
        )

        return response
