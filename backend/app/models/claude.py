from .base import BaseModel


class ClaudeModel(BaseModel):

    async def chat(self, message: str) -> str:

        # 后续接入 Claude API
        return f"Claude response: {message}"
