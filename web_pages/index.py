html = """<!doctype html>
<html>
  <head>
    <title>page title</title>
    <link rel="stylesheet" href="/css/style.css" />
  </head>
  <body>
    <h1>My first heading</h1>
    <p>My first paragraph.</p>
    <p>My second paragraph.</p>
    <p>My second paragraph.</p>
    <div>
      <h2>My third heading</h2>
      <h2>New second-level title</h2>
    </div>
  </body>
</html>
"""

# Print to stdout
print(html)

# Optionally write back to HTML file
output_path = r"c:\Users\nikit\first_project\web_pages\index.html"
with open(output_path, "w", encoding="utf-8") as f:
    f.write(html)