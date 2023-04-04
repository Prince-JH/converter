import openai

openai.api_key = ''


def query(statement):
    model = "gpt-3.5-turbo"

    messages = [
        {"role": "user",
         "content": f"Make me JPA DTO class able to carry following json format. "
                    f"I dont' need getter or setter or constructor, and name the class DTO.\n"
                    f"{statement}"}
    ]

    response = openai.ChatCompletion.create(
        model=model,
        messages=messages
    )
    answer = response['choices'][0]['message']['content']
    return answer
