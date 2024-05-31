
# 📰 News Collector in Python

Welcome to the **News Collector** project! This Python application fetches news feeds from a specified RSS URL and summarizes each news article using a summarization function.

[![Bandit Security Check](https://github.com/doribd/newsCollector/actions/workflows/bandit.yml/badge.svg)](https://github.com/doribd/newsCollector/actions/workflows/bandit.yml)

## 🚀 Features

- Fetches news from AWS (see Roadmap below) RSS feed URL
- Summarizes news articles based on OpenAI
- Easy configuration through `config.ini` and `.env` files

## 📦 Installation

1. **Clone the repository** to your local workspace:
    ```sh
    git clone https://github.com/your_username/news-collector.git
    ```
2. **Navigate to the project folder**:
    ```sh
    cd news-collector
    ```
3. **Install the required packages**:
    ```sh
    pip install -r requirements.txt
    ```

## 🛠️ Usage

You can execute the application by running `main.py` (CLI):

```sh
python main.py

Or you can run the application using the FastAPI server:

```sh
uvicorn main:app --reload
```

Once the application is running, you can access the following APIs in your browser:  
```bazaar
AWS News Report: http://localhost:8000/aws
Azure News Report: http://localhost:8000/azure
GCP News Report: http://localhost:8000/gcp
```
Each API will fetch the respective news feed, summarize the articles, and display the report in your browser. 

## ⚙️ Configuration

### `config.ini`

This file is used to specify the RSS feed URL and the number of days to fetch news for.
You can also specify the OpenAI model and its parameters:

### `config.ini`

```ini
[RSS]
aws_url=https://aws.amazon.com/about-aws/whats-new/recent/feed/
azure_url=https://azurecomcdn.azureedge.net/en-us/updates/feed/

[DAYS]
num_days=7

[OPENAI]
model=gpt-3.5-turbo
temperature=0.5
max_tokens=64
top_p=1
```

### `.env`

This file stores your OpenAI API key:

```env
OPENAI_API_KEY=your_openai_api_key
```
## 🔒 Security

This project uses the following open source Static Application Security Testing (SAST) tools to ensure the quality and security of the code:

- **bandit**: designed to find common security issues in Python code.
- **pip-audit**: scanning Python environments for packages with known vulnerabilities. It uses the Python Packaging Advisory Database.

These tools help us maintain high standards of code quality and security. They scan our codebase for common security vulnerabilities and coding errors, and provide feedback that we use to improve our code.

## 🤝 Contribution

Contributions are always welcome! To get started, check out `CONTRIBUTING.md` for guidelines on how to contribute to this project.

1. **Fork the repository**
2. **Create a new branch**: `git checkout -b feature/your_feature`
3. **Commit your changes**: `git commit -m 'Add some feature'`
4. **Push to the branch**: `git push origin feature/your_feature`
5. **Open a pull request**

## 📄 License

This project is licensed under the MIT License - see the `LICENSE.md` file for details.

## 📄 Roadmap

You can view the project's roadmap [here](ROADMAP.md).
