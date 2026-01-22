branches = ["CSE","IT","ECE","EE","ME","CE","AIML","AI_DS","CHEMICAL"]

semesters = range(1,9)

subjects = {
  1:["Mathematics-1","Physics","Basic Electrical Engineering","Engineering Graphics","Communication Skills"]
}

def page(title, body):
  return f"""<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>{title}</title>
<link rel="stylesheet" href="css/style.css">
<script src="js/app.js"></script>
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

# HOME PAGE
home=""
for b in branches:
  home += f'<a href="{b}.html"><div class="card">{b}</div></a>'

open("index.html","w").write(
  page("Home",f"<div class='grid'>{home}</div>")
)

# BRANCH → SEMESTER
for b in branches:
  sem=""
  for s in semesters:
    sem += f'<a href="{b}_sem{s}.html"><div class="card">Semester {s}</div></a>'

  open(f"{b}.html","w").write(
    page(f"{b} Branch",f"<div class='grid'>{sem}</div>")
  )

# SEMESTER → SUBJECT
for b in branches:
  for s in semesters:
    sub_cards=""
    for sub in subjects.get(s,[]):
      fname=f"{b}_sem{s}_{sub.replace(' ','_')}.html"
      sub_cards+=f'<a href="{fname}"><div class="card">{sub}</div></a>'

      open(fname,"w").write(
        page(
          f"{b} - {sub}",
          """
<div class="card">About Subject</div>
<div class="card">Last 5 Years Question Papers</div>
<div class="card">Last 5 Years Solutions</div>
"""
        )
      )

    open(f"{b}_sem{s}.html","w").write(
      page(f"{b} Semester {s}",f"<div class='grid'>{sub_cards}</div>")
    )

