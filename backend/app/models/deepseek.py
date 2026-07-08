from .base import BaseModel


class DeepSeekModel(BaseModel):

    async def chat(self, message: str) -> str:

        # 后续接入 DeepSeek API
        return f"DeepSeek response: {message}"
