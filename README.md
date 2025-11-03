# Job-Recommendation-System
real-time Job Recommendation System built using **Streamlit** and **Python**, which recommends the most relevant jobs to users based on:

✅ Skills Match  
✅ Years of Experience  
✅ Expected Salary  
✅ Real-time Job Filtering & Ranking  

This project helps job seekers find suitable job opportunities efficiently using a rule-based recommendation model.

---

## 🚀 Features

- 🔍 Skill-based filtering using text analysis
- 🎓 Minimum experience eligibility check
- 💰 Salary alignment with candidate expectations
- 📊 Ranking of jobs by match score
- 🖥️ Clean UI using Streamlit
- 📥 Option to download recommendation results as CSV
- ⚡ Fast & Lightweight - No heavy ML models required

---

## 🛠️ Tech Stack

| Component | Technology |
|----------|------------|
| Frontend | Streamlit |
| Backend | Python |
| Data Processing | Pandas |
| Storage | CSV files (can be upgraded to MySQL) |

---

## 📌 System Workflow

1️⃣ User enters:
- Skills (comma-separated)
- Years of experience
- Expected Salary (in LPA)

2️⃣ System runs filters based on:
- Required skills
- Minimum experience
- Salary range

3️⃣ Results get **ranked by skill match score**

4️⃣ User sees best matched jobs and can download csv file containing matching jobs
