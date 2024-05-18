def create_report(entries):
    """
    Creates the html report

    :param entries: news which were parsed
    :return: nothing, creates the actual html report file
    """

    html_content = """
<html>
<head>
    <title>AWS News</title>
    <style>
        body {
            font-family: Arial, sans-serif;
        }
        .panel {
            background-color: #ffffff;
            border: 1px solid #ccc;
            border-radius: 5px;
            margin: 10px 0;
            padding: 10px;
            cursor: pointer;
        }
        .panel-title {
            font-size: 18px;
            font-weight: bold;
        }
        .panel-content {
            display: none;
            margin-top: 10px;
        }
    </style>
    <script>
        function togglePanelContent(panel) {
            var content = panel.querySelector('.panel-content');
            if (content.style.display === 'none' || content.style.display === '') {
                content.style.display = 'block';
            } else {
                content.style.display = 'none';
            }
        }
    </script>
</head>
<body>
    <h1>AWS News</h1>
"""
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

    with open("newsBoard.html", "w", encoding="utf-8") as file:
        file.write(html_content)
    print("The news entries have been saved.")
