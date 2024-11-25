import os

from dotenv import find_dotenv, load_dotenv
from openai import OpenAI
from strenum import StrEnum

load_dotenv(find_dotenv())
load_dotenv()

OPENAI_OPENAI = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
)


class OpenaiModel(StrEnum):
    """ 模型列表 
    Ref:
        https://platform.openai.com/docs/models/gpt-4-turbo-and-gpt-4#models-overview
    """
    GPT_4O = "gpt-4o"
    GPT_4O_MINI = "gpt-4o-mini"
    O1_PREVIEW = "o1-preview"
    O1_MINI = "o1-mini"
