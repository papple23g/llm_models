import os

from dotenv import find_dotenv, load_dotenv
from openai import OpenAI
from strenum import StrEnum

load_dotenv(find_dotenv())

GROQ_OPENAI = OpenAI(
    api_key=os.environ.get("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1",
)


class GorqModel(StrEnum):
    """ 模型列表
    Ref:
        https://console.groq.com/docs/models
    """
    GEMMA2_9B_IT = "gemma2-9b-it"
    LLAMA_3_2_90B_VISION_PREVIEW = "llama-3.2-90b-vision-preview"
