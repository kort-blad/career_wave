import openai
import json
import config

YANDEX_CLOUD_MODEL = "qwen3-235b-a22b-fp8/latest"

client = openai.OpenAI(
    api_key=config.key_ya,
    base_url="https://ai.api.cloud.yandex.net/v1",
    project=config.id_ya
)

def web_ai(text_ai):

    response = client.responses.create(
        model=f"gpt://{config.id_ya}/{YANDEX_CLOUD_MODEL}",
        input=text_ai,
        tools=[
            {
                "type": "web_search",
                "filters": {
                    "allowed_domains": [
                        "hh.ru"
                    ]
                },
                "user_location": {
                        "region": "213",
                    }
            }
        ],
        temperature=0.3,
        max_output_tokens=2000
    )

    # Response text
    # print("Response text:")
    
    # print("\n" + "=" * 50 + "\n")

    # # Full response
    
    # print("Full response (JSON):")
    # print(json.dumps(response.model_dump(), indent=2, ensure_ascii=False))

    return response.output_text


print(web_ai(''))