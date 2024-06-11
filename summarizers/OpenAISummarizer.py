import openai

from summarizers.BaseSummarizer import BaseSummarizer


class OpenAISummarizer(BaseSummarizer):
    def summarize_text(self, text):
        model = self.config.get('OPENAI', 'model')
        temperature = self.config.getfloat('OPENAI', 'temperature')
        max_tokens = self.config.getint('OPENAI', 'max_tokens')
        top_p = self.config.getint('OPENAI', 'top_p')

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
