import os

from .deepseek import DeepSeekModel
from .claude import ClaudeModel


def get_model():

    provider = os.getenv(
        "AI_PROVIDER",
        "deepseek"
    )


    if provider == "claude":
        return ClaudeModel()


    return DeepSeekModel()
