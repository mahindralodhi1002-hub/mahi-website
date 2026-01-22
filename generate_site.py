import os

branches = {
    "cse": ["Mathematics-1", "Physics", "Basic Electrical Engineering", "Engineering Graphics", "Communication Skills"],
    "ece": ["Mathematics-1", "Physics", "Basic Electrical Engineering", "Engineering Graphics", "Communication Skills"],
    "ee":  ["Mathematics-1", "Physics", "Basic Electrical Engineering", "Engineering Graphics", "Communication Skills"],
    "me":  ["Mathematics-1", "Physics", "Basic Electrical Engineering", "Engineering Graphics", "Communication Skills"],
    "ce":  ["Mathematics-1", "Physics", "Basic Electrical Engineering", "Engineering Graphics", "Communication Skills"],
}

os.makedirs("css", exist_ok=True)
os.makedirs("js", exist_ok=True)
os.makedirs("branches", exist_ok=True)

# ---------- CSS ----------
with open("css/style.css", "w") as f:
    f.write("""
body{font-family:Arial;background:#f4f6fa;padding:20px}
.box{background:#fff;padding:20px;border-radius:10px;margin-bottom:15px}
button{padding:8px 12px;margin:5px}
.dark{background:#121212;color:white}
""")

with open("js/theme.js", "w") as f:
    f.write("""
function toggleTheme(){document.body.classList.toggle("dark")}
function goHome(){window.location='/'}
""")

# ---------- HOME ----------
with open("index.html", "w") as f:
    f.write("<h1>B.Tech Branches</h1>")
    for b in branches:
        f.write(f'<a href="branches/{b}/semester1/index.html"><button>{b.upper()}</button></a>')

# ---------- GENERATE PAGES ----------
for branch, subjects in branches.items():
    for sem in range(1, 9):
        sem_path = f"branches/{branch}/semester{sem}"
        os.makedirs(sem_path + "/pdfs/questions", exist_ok=True)
        os.makedirs(sem_path + "/pdfs/solutions", exist_ok=True)

        with open(f"{sem_path}/index.html", "w") as f:
            f.write(f"""
<h2>{branch.upper()} Branch - Semester {sem}</h2>
<button onclick="goHome()">Home</button>
<button onclick="toggleTheme()">Dark</button>
""")
            for sub in subjects:
                name = sub.lower().replace(" ", "_")
                f.write(f'<div class="box"><a href="{name}.html">{sub}</a></div>')

        for sub in subjects:
            name = sub.lower().replace(" ", "_")
            with open(f"{sem_path}/{name}.html", "w") as f:
                f.write(f"""
<h2>{branch.upper()} Branch</h2>
<h3>Semester {sem}</h3>
<h1>{sub}</h1>

<button onclick="goHome()">Home</button>
<button onclick="history.back()">Back</button>
<button onclick="toggleTheme()">Dark</button>

<p>Last 5 Years Question Papers</p>
<p>Last 5 Years Solutions</p>
""")

print("✅ Website Generated Successfully")
