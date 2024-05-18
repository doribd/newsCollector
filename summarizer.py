from configparser import ConfigParser

import openai

config = ConfigParser()
config.read('config.ini')


def summarize_text(text):
    """
    This function uses the OpenAI Chat completion api to summarize provided text.

    :param text: the text which will be summarized
    :return: summarized text
    """
    model = config.get('OPENAI', 'model')
    temperature = config.getfloat('OPENAI', 'temperature')
    max_tokens = config.getint('OPENAI', 'max_tokens')
    top_p = config.getint('OPENAI', 'top_p')

    response = openai.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "system",
                "content": "Summarize content you are provided with for a second-grade student."
            },
            {
                "role": "user",
                "content": f"Summarize the following text in one sentence:\n\n{text}"
            }
        ],
        temperature=temperature,
        max_tokens=max_tokens,
        top_p=top_p
    )
    return response.choices[0].message.content
