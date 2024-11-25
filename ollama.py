from dotenv import find_dotenv, load_dotenv
from openai import OpenAI
from strenum import StrEnum

load_dotenv(find_dotenv())

OLLAMA_OPENAI = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama",
)


class OllamaModel(StrEnum):
    """ 模型列表
    Ref:
        https://ollama.com/search
    """
    GEMMA2_9B_SIMPO = "mannix/gemma2-9b-simpo"  # 目前(2024-11-25)最強 MIT 開源模型
    GEMMA2_2B = "gemma2:2b"
    LLAMA_3_2 = "llama3.2"
