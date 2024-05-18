
# 📰 News Collector in Python

Welcome to the **News Collector** project! This Python application fetches news feeds from a specified RSS URL and summarizes each news article using a summarization function.

[![Bandit Security Check](https://github.com/doribd/my-repo/actions/workflows/bandit.yml/badge.svg)](https://github.com/doribd/my-repo/actions/workflows/bandit.yml)

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

You can execute the application by running `main.py`:

```sh
python main.py
```

## ⚙️ Configuration

### `config.ini`

This file is used to specify the RSS feed URL and the number of days to fetch news for:

```ini
[RSS]
url = your_RSS_feed_url

[DAYS]
num_days = 7
```

### `.env`

This file stores your OpenAI API key:

```env
OPENAI_API_KEY=your_openai_api_key
```

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
