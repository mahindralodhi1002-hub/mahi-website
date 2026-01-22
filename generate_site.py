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

def page(title, body, depth=".."):
    return f"""<!DOCTYPE html>
<html>
<head>
<title>{title}</title>
<link rel="stylesheet" href="{depth}/css/style.css">
<script src="{depth}/js/app.js"></script>
</head>
<body>
<div class="nav">
  <b>{college}</b>
  <div>
    <button onclick="goHome()">Home</button>
    <button onclick="goBack()">Back</button>
    <button onclick="toggleDark()">🌙</button>
  </div>
</div>
<div class="container">{body}</div>
<div class="footer">© 2026 Mahindra Lodhi</div>
</body>
</html>"""

for b in branches:
    branch_path = f"branches/{b}"
    os.makedirs(branch_path, exist_ok=True)

    sem_cards = ""
    for s in range(1,9):
        sem_cards += f'<a href="semester{s}/index.html"><div class="card">Semester {s}</div></a>'

        sem_path = f"{branch_path}/semester{s}"
        os.makedirs(sem_path, exist_ok=True)

        subject_cards = ""
        for sub in subjects:
            fname = sub.replace(" ","_") + ".html"
            subject_cards += f'<a href="{fname}"><div class="card">{sub}</div></a>'

            os.makedirs(f"{sem_path}/pdfs/{sub}/questions", exist_ok=True)
            os.makedirs(f"{sem_path}/pdfs/{sub}/solutions", exist_ok=True)

            open(f"{sem_path}/{fname}", "w").write(
                page(
                    f"{b} – {sub}",
                    f"""
<h2>{b} Branch</h2>
<h3>{sub}</h3>
<div class="card">Last 5 Years Question Papers</div>
<div class="card">Last 5 Years Solutions</div>
""",
                    "../.."
                )
            )

        open(f"{sem_path}/index.html","w").write(
            page(f"{b} Semester {s}", f"<div class='grid'>{subject_cards}</div>", "..")
        )

    open(f"{branch_path}/index.html","w").write(
        page(f"{b} Branch", f"<div class='grid'>{sem_cards}</div>")
    )

print("✅ Website generated successfully")
