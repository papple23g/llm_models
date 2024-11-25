import os

from dotenv import find_dotenv, load_dotenv
from openai import OpenAI
from strenum import StrEnum

load_dotenv(find_dotenv())

GITHUB_OPENAI = OpenAI(
    api_key=os.getenv("GITHUB_TOKEN"),
    base_url="https://models.inference.ai.azure.com",
)


class GithubModel(StrEnum):
    """ 模型列表
    Ref:
        https://github.com/marketplace/models
    """
    GPT_4O = "gpt-4o"
    GPT_4O_MINI = "gpt-4o-mini"
    O1_PREVIEW = "o1-preview"
    O1_MINI = "o1-mini"
