import os

# ---------- CONFIG ----------
SITE_TITLE = "Sagar Institute of Science and Technology"
OWNER = "Mahindra Lodhi"
YEAR = "2026"

BRANCHES = {
    "CSE": "Computer Science & Engineering",
    "ECE": "Electronics & Communication Engineering",
    "EE": "Electrical Engineering",
    "ME": "Mechanical Engineering",
    "CE": "Civil Engineering",
    "IT": "Information Technology",
    "AIML": "Artificial Intelligence & ML",
    "AIDS": "AI & Data Science",
    "CHEMICAL": "Chemical Engineering"
}

SEMESTERS = [1,2,3,4,5,6,7,8]

COMMON_SUBJECTS = [
    "Mathematics-1",
    "Physics",
    "Basic Electrical",
    "Engineering Graphics",
    "Communication Skills"
]

# ---------- HELPERS ----------
def write(path, content):
    folder = os.path.dirname(path)
    if folder != "":
        os.makedirs(folder, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
def header(title):
    return f"""<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>{title} | {SITE_TITLE}</title>
<link rel="stylesheet" href="/style.css">
</head>
<body>
<div class="top">
<a href="/index.html">🏠 Home</a>
</div>
"""

def footer():
    return f"""
<footer>© {YEAR} {OWNER}</footer>
</body>
</html>
"""

# ---------- STYLE ----------
write("style.css", """
body{font-family:Arial;background:#f4f6fb;margin:0}
.top{background:#0b5ed7;padding:10px}
.top a{color:#fff;text-decoration:none;font-weight:bold}
.card{background:#fff;padding:20px;margin:20px;border-radius:10px}
.btn{display:inline-block;padding:10px 15px;background:#0b5ed7;color:#fff;border-radius:6px;text-decoration:none}
footer{text-align:center;padding:20px;color:#555}
""")

# ---------- HOME ----------
home = header("Home") + f"""
<div class="card">
<h1>{SITE_TITLE}</h1>
<p>Learn with {OWNER}</p>
<h2>B.Tech Branches</h2>
"""
for b in BRANCHES:
    home += f'<p><a class="btn" href="/branches/{b}.html">{b}</a></p>'
home += "</div>" + footer()
write("index.html", home)

# ---------- BRANCH + SEMESTER ----------
for b, full in BRANCHES.items():
    content = header(f"{b} Branch") + f"""
<div class="card">
<h2>{b} Branch</h2>
"""
    for s in SEMESTERS:
        content += f'<p><a class="btn" href="/branches/{b}/sem{s}.html">Semester {s}</a></p>'
    content += "</div>" + footer()
    write(f"branches/{b}.html", content)

    for s in SEMESTERS:
        sem = header(f"{b} Semester {s}") + f"""
<div class="card">
<h2>{b} – Semester {s}</h2>
"""
        for sub in COMMON_SUBJECTS:
            fname = sub.replace(" ", "_").replace("-", "")
            sem += f'<p><a class="btn" href="/subjects/{b}_sem{s}_{fname}.html">{sub}</a></p>'
        sem += "</div>" + footer()
        write(f"branches/{b}/sem{s}.html", sem)

        for sub in COMMON_SUBJECTS:
            fname = sub.replace(" ", "_").replace("-", "")
            page = header(sub) + f"""
<div class="card">
<h2>{sub}</h2>
<p>This page contains notes, previous year papers and solutions.</p>

<h3>Last 5 Years Question Papers</h3>
<ul>
<li>2021</li><li>2022</li><li>2023</li><li>2024</li><li>2025</li>
</ul>

<h3>Last 5 Years Solutions</h3>
<ul>
<li>2021</li><li>2022</li><li>2023</li><li>2024</li><li>2025</li>
</ul>
</div>
""" + footer()
            write(f"subjects/{b}_sem{s}_{fname}.html", page)

print("✅ Website generated successfully")
