import os

branches = ["CSE", "IT", "ECE", "EE", "ME", "CE", "AIML", "AI_DS", "Chemical"]
subjects = ["Mathematics-1", "Physics", "Basic Electrical Engineering", "Engineering Graphics", "Communication Skills"]

# Create folders
os.makedirs("website", exist_ok=True)

# Subject Page Template
subject_template = """
<!DOCTYPE html>
<html>
<head>
    <title>{branch} – {subject}</title>
    <link rel="stylesheet" href="../style.css">
</head>
<body>

<h2>{branch} – {subject}</h2>
<p>This page will contain previous year papers and solutions.</p>

<h3>Last 5 Years Question Papers</h3>
<ul>
<li>2021 – <a href="../../pdfs/{branch}/{subject}/2021.pdf">Download</a></li>
<li>2022 – <a href="../../pdfs/{branch}/{subject}/2022.pdf">Download</a></li>
<li>2023 – <a href="../../pdfs/{branch}/{subject}/2023.pdf">Download</a></li>
<li>2024 – <a href="../../pdfs/{branch}/{subject}/2024.pdf">Download</a></li>
<li>2025 – <a href="../../pdfs/{branch}/{subject}/2025.pdf">Download</a></li>
</ul>

</body>
</html>
"""

# Semester page template
semester_template = """
<!DOCTYPE html>
<html>
<head>
    <title>{branch} – Semester 1</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>

<h2>{branch} – Semester 1</h2>
<h3>Select Subject</h3>

<ul>
{links}
</ul>

</body>
</html>
"""

# Loop through each branch
for branch in branches:

    # Create subject folder
    os.makedirs(f"website/{branch}/subjects", exist_ok=True)

    # Create semester page
    subject_links = ""
    for sub in subjects:
        safe_sub = sub.replace(" ", "_")
        subject_links += f'<li><a href="subjects/{safe_sub}.html">{sub} ({branch})</a></li>\n'

    with open(f"website/{branch}/semester1.html", "w") as f:
        f.write(semester_template.format(branch=branch, links=subject_links))

    # Create subject pages
    for sub in subjects:
        safe_sub = sub.replace(" ", "_")
        with open(f"website/{branch}/subjects/{safe_sub}.html", "w") as f:
            f.write(subject_template.format(branch=branch, subject=sub))

print("All Branch, Semester, Subject pages created successfully!")
