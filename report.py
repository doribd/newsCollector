def create_report(entries, feed):
    """
    Creates the html report

    :param entries: news which were parsed
    :param feed: instance of a feed class
    :return: nothing, creates the actual html report file
    """
    feed_name = feed.get_name()

    html_content = """
<html>
<head>
    <title>{0} News</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
        }}
        .panel {{
            background-color: #ffffff;
            border: 1px solid #ccc;
            border-radius: 5px;
            margin: 10px 0;
            padding: 10px;
            cursor: pointer;
        }}
        .panel-title {{
            font-size: 18px;
            font-weight: bold;
        }}
        .panel-content {{
            display: none;
            margin-top: 10px;
        }}
    </style>
    <script>
        function togglePanelContent(panel) {{
            var content = panel.querySelector('.panel-content');
            if (content.style.display === 'none' || content.style.display === '') {{
                content.style.display = 'block';
            }} else {{
                content.style.display = 'none';
            }}
        }}
    </script>
</head>
<body>
    <h1>{0} News</h1>
""".format(feed_name)
    for entry in entries:
        html_content += f"""
        <div class="panel" onclick="togglePanelContent(this)">
            <div class="panel-title">{entry['title']}</div>
            <div class="panel-content">
                <p><strong>Link:</strong> <a href="{entry['link']}">{entry['link']}</a></p>
                <p><strong>AI Summary:</strong> {entry['summary']}</p>
            </div>
        </div>
    """
    html_content += """
    </body>
</html>
    """
    filename = f"{feed_name}NewsBoard.html"
    with open(filename, "w", encoding="utf-8") as file:
        file.write(html_content)
    print(f"The {feed_name} entries have been saved.")
