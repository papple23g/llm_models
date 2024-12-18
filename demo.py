import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))  # noqa
from llm_models import OLLAMA_OPENAI, OllamaModel

if __name__ == '__main__':
    # OPENAI = OPENAI_OPENAI
    # MODEL_STR = OpenAIModel.GPT_4O_MINI

    # OPENAI = XAI_OPENAI
    # MODEL_STR = XaiModel.GROK_BETA

    # OPENAI = GITHUB_OPENAI
    # MODEL_STR = GithubModel.GPT_4O_MINI

    # OPENAI = GROQ_OPENAI
    # MODEL_STR = GorqModel.GEMMA2_9B_IT

    OPENAI = OLLAMA_OPENAI
    # MODEL_STR = OllamaModel.GEMMA2_9B_SIMPO
    MODEL_STR = OllamaModel.GEMMA2_2B

    completion = OPENAI.chat.completions.create(
        model=MODEL_STR,
        messages=[{
            "role": "user",
            "content": (
                "1+1=多少?"
            ),
        }],
        seed=42,
        temperature=0.0,
    )
    print(completion.choices[0].message.content)
    # > 1 + 1 = 2。
