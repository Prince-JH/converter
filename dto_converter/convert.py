import openai

# openai API 키 인증
openai.api_key = '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'


def query(statement):
    model = "gpt-3.5-turbo"

    # 메시지 설정하기
    messages = [
        {"role": "user",
         "content": f"Make me JPA DTO class able to carry following json format. "
                    f"I dont' need getter or setter or constructor, and name the class DTO.\n"
                    f"{statement}"}
    ]

    # ChatGPT API 호출하기
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages
    )
    answer = response['choices'][0]['message']['content']
    return answer
