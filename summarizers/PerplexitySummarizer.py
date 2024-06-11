import requests

from summarizers.BaseSummarizer import BaseSummarizer


class PerplexitySummarizer(BaseSummarizer):
    def __init__(self):
        super().__init__()
        self.api_key = self.config.get('PERPLEXITY', 'api_key')

    def summarize_text(self, text):
        """
        This function uses the Perplexity API to summarize provided text.

        :param text: the text which will be summarized
        :return: summarized text
        """
        # Define the API endpoint
        url = "https://api.perplexity.ai/summarize"

        # Define the headers for the API request
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }

        # Define the body of the API request
        data = {
            "text": text
        }

        # Make the API request
        response = requests.post(url, headers=headers, json=data)

        # Check the response status code
        if response.status_code == 200:
            # If the request was successful, return the summarized text
            return response.json()["summary"]
        else:
            # If the request was not successful, raise an exception
            raise Exception(f"Perplexity API request failed with status code {response.status_code}")
