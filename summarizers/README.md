# Summarizers

This directory contains the classes responsible for text summarization in the project. Each class represents a different
summarization API.

## BaseSummarizer

`BaseSummarizer` is an abstract base class that defines the common interface for all summarizers. It handles the common
functionality such as reading from the `config.ini` file. Any class that inherits from `BaseSummarizer` must implement
the `summarize_text` method.

## [OpenAISummarizer](https://openai.com)

`OpenAISummarizer` is a class that uses the OpenAI API for text summarization. It inherits from `BaseSummarizer` and
implements the `summarize_text` method.

## [ClaudeSummarizer](https://www.example.com)

`ClaudeSummarizer` is a class that uses the Claude API for text summarization. It inherits from `BaseSummarizer` and
implements the `summarize_text` method. The implementation is currently a placeholder and needs to be filled in with the
actual code to call the Claude API and summarize the text.

## [PerplexitySummarizer](https://www.perplexity.ai)

`PerplexitySummarizer` is a class that uses the Perplexity API for text summarization. It inherits from `BaseSummarizer` and
implements the `summarize_text` method.

