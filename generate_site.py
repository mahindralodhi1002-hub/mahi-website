import os

branches = {
    "CSE": ["Mathematics-1", "Physics", "Basic Electrical", "Engineering Graphics", "Communication Skills"],
    "ECE": ["Mathematics-1", "Physics", "Basic Electrical", "Engineering Graphics", "Communication Skills"],
    "EE":  ["Mathematics-1", "Physics", "Basic Electrical", "Engineering Graphics", "Communication Skills"],
    "ME":  ["Mathematics-1", "Physics", "Basic Electrical", "Engineering Graphics", "Communication Skills"],
    "CE":  ["Mathematics-1", "Physics", "Basic Electrical", "Engineering Graphics", "Communication Skills"],
    "IT":  ["Mathematics-1", "Physics", "Basic Electrical", "Engineering Graphics", "Communication Skills"],
    "AIML":["Mathematics-1", "Physics", "Basic Electrical", "Engineering Graphics", "Communication Skills"],
    "AIDS":["Mathematics-1", "Physics", "Basic Electrical", "Engineering Graphics", "Communication Skills"],
    "CHEMICAL":["Mathematics-1", "Physics", "Basic Electrical", "Engineering Graphics", "Communication Skills"],
}

def page(title, body):
    return f"""<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>{title}</title>
<link rel="stylesheet" href="../css/style.css">
<script src="../js/app.js"></script>
</head>
<body>
<div class="nav">
  <b>{title}</b>
  <button onclick="toggleDark()">🌙</button>
</div>
<div class="container">
{body}
</div>
<div class="footer">© 2026 Mahindra Lodhi</div>
</body>
</html>"""

os.makedirs("css", exist_ok=True)
os.makedirs("js", exist_ok=True)
os.makedirs("branches", exist_ok=True)

# CSS
open("css/style.css","w").write("""
body{font-family:Arial;background:#f4f7fb;margin:0}
body.dark{background:#0f172a;color:#e5e7eb}
.nav{background:#2563eb;color:white;padding:15px;display:flex;justify-content:space-between}
.container{padding:20px;max-width:1100px;margin:auto}
.card{background:white;padding:15px;border-radius:12px;margin:10px 0}
body.dark .card{background:#1e293b}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:15px}
a{text-decoration:none;color:inherit}
.footer{text-align:center;padding:15px;opacity:.7}
""")

# JS
open("js/app.js","w").write("""
function toggleDark(){
  document.body.classList.toggle("dark");
  localStorage.setItem("dark",document.body.classList.contains("dark"));
}
if(localStorage.getItem("dark")==="true"){
  document.body.classList.add("dark");
}
""")

# HOME
home_cards=""
for b in branches:
    home_cards+=f'<a href="branches/{b}/index.html"><div class="card">{b}</div></a>'

open("index.html","w").write(page("Home",f"<div class='grid'>{home_cards}</div>"))

# GENERATE STRUCTURE
for branch, subjects in branches.items():
    branch_path=f"branches/{branch}"
    os.makedirs(branch_path,exist_ok=True)

    sem_cards=""
    for sem in range(1,9):
        sem_cards+=f'<a href="semester{sem}/index.html"><div class="card">Semester {sem}</div></a>'

        sem_path=f"{branch_path}/semester{sem}"
        os.makedirs(sem_path,exist_ok=True)

        subject_cards=""
        for sub in subjects:
            sub_file=sub.replace(" ","_")+".html"
            subject_cards+=f'<a href="{sub_file}"><div class="card">{sub}</div></a>'

            # PDF folders
            os.makedirs(f"{sem_path}/pdfs/{sub}/questions",exist_ok=True)
            os.makedirs(f"{sem_path}/pdfs/{sub}/solutions",exist_ok=True)

            open(f"{sem_path}/{sub_file}","w").write(
                page(
                    f"{branch} - {sub}",
                    f"<h2>{branch} Branch</h2><h3>{sub}</h3>"
                    "<div class='card'>Last 5 Years Question Papers</div>"
                    "<div class='card'>Last 5 Years Solutions</div>"
                )
            )

        open(f"{sem_path}/index.html","w").write(
            page(f"{branch} Semester {sem}",f"<div class='grid'>{subject_cards}</div>")
        )

    open(f"{branch_path}/index.html","w").write(
        page(f"{branch} Branch",f"<div class='grid'>{sem_cards}</div>")
    )

print("✅ Full website + PDF folders generated")
