import os

from dotenv import find_dotenv, load_dotenv
from openai import OpenAI
from strenum import StrEnum

load_dotenv(find_dotenv())

XAI_OPENAI = OpenAI(
    api_key=os.getenv("XAI_API_KEY"),
    base_url="https://api.x.ai/v1",
)


class XaiModel(StrEnum):
    """ 模型列表
    Ref:
        https://docs.x.ai/docs#models
    """
    GROK_BETA = "grok-beta"
