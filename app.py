from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

PORTFOLIO = {
    "name": "PATHUMANITHI S",
    "title": "Data Scientist & Web Developer",
    "about": (
    "I'm a fresher passionate about Data Science and Web Development. "
    "I have built 3 real-world projects and have hands-on knowledge "
    "of 5 technologies including Python, Data Analysis, Machine Learning, "
    "Flask, and Web Development."
),
    "skills": {
        "Data Science": ["Python", "Machine Learning", "Data Analysis", "Power BI"],
        "Web Development": ["HTML", "CSS", "JavaScript", "Flask"],
        "Tools": ["Git", "Jupyter Notebook", "SQL"],
    },
    "projects": [
        {
            "title": "Closet Organizer",
            "description": "A web application to help users organize their clothing items.",
            "tech": ["HTML", "CSS", "JavaScript"],
            "github": "https://github.com/pathumanithi22/closet_organizer",
        },
        {
            "title": "Smart FYP",
            "description": "A centralized web application to monitor and track college final year project reviews for students and guides.",
            "tech": ["Python", "Flask", "SQL"],
           
        },
        {
            "title": "Ecommerce Data Analysis",
            "description": "A data analysis project on Ecommerce data.",
            "tech": ["Python", "Pandas", "Matplotlib"],
            
        },
    ],
    "contact": {
        "email": "pathumanithis03@gmail.com",
        "github": "https://github.com/yourusername",
        "linkedin": "https://linkedin.com/in/yourusername",
    },
}

@app.route("/")
def home():
    return render_template("index.html", data=PORTFOLIO)

@app.route("/api/projects")
def get_projects():
    return jsonify(PORTFOLIO["projects"])

@app.route("/contact", methods=["POST"])
def contact():
    payload = request.get_json()
    name    = payload.get("name")
    email   = payload.get("email")
    message = payload.get("message")
    print(f"Message from {name}: {message}")
    return jsonify({"status": "success", "message": "Message received!"})

if __name__ == "__main__":
    app.run(debug=True)