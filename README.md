# Job-Recommendation-System
real-time Job Recommendation System built using **Streamlit** and **Python**, which recommends the most relevant jobs to users based on:

✅ Skills Match  
✅ Years of Experience  
✅ Expected Salary  
✅ Real-time Job Filtering & Ranking  

This project helps job seekers find suitable job opportunities efficiently using a rule-based recommendation model.
## 🧠 Machine Learning Approach

This project implements a **Content-Based Recommendation System** using:

### ✅ Cosine Similarity (Scikit-Learn)
- Converts candidate skills & job required skills into numerical vectors using `CountVectorizer`
- Measures closeness between skills using `cosine_similarity`
- Ranks job recommendations by highest similarity score

### ✅ Why Cosine Similarity?
| Feature | Benefit |
|--------|---------|
| Handles partial skill overlaps | Better job fit |
| Vector-based comparison | ML powered approach |
| Scales well with large datasets | Production ready |
| Used by modern job platforms | LinkedIn, Indeed, Naukri |

---

### 🔍 Algorithm Workflow

1️⃣ Convert all skills into lowercase text  
2️⃣ Transform skills into vector form using **Bag-of-Words (CountVectorizer)**  
3️⃣ Apply **Cosine Similarity** to compute how close user skills match job skills  
4️⃣ Filter by experience & salary criteria  
5️⃣ Sort jobs by similarity score (higher = better match)

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
