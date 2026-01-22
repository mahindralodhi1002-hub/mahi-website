import os

college = "Sagar Institute of Science and Technology"

branches = ["CSE","ECE","EE","ME","CE","IT","AIML","AIDS","CHEMICAL"]
subjects = [
  "Mathematics-1",
  "Physics",
  "Basic Electrical Engineering",
  "Engineering Graphics",
  "Communication Skills"
]


def page(title, body):
    return f"""<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>{title}</title>
<link rel="stylesheet" href="/mahi-website/css/style.css">
<script src="/mahi-website/js/app.js"></script>
</head>
<body>

<div class="nav">
  <b>Sagar Institute of Science and Technology</b>
  <div>
    <button onclick="goHome()">Home</button>
    <button onclick="goBack()">Back</button>
    <button onclick="toggleDark()">🌙</button>
  </div>
</div>

<div class="container">
{body}
</div>

<div class="footer">© 2026 Mahindra Lodhi</div>
</body>
</html>"""
