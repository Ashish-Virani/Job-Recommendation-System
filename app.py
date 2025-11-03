import streamlit as st
import pandas as pd

@st.cache_data
def load_jobs():
    return pd.read_csv("jobs.csv")

jobs_df = load_jobs()

st.title("🎯 Smart Job Recommendation System")

st.write("Enter your profile to get personalized job recommendations!")

# Inputs
user_skill_input = st.text_area(
    "Enter your skills (comma-separated):",
    placeholder="e.g. Python, C++, Deep Learning"
)

years_exp = st.number_input(
    "Years of Experience:",
    min_value=0, max_value=20, value=1
)

desired_salary = st.number_input(
    "Expected Salary (LPA):",
    min_value=1.0, max_value=100.0, value=5.0
)

if st.button("🚀 Recommend Jobs"):
    if user_skill_input.strip() == "":
        st.warning("Please enter at least one skill.")
    else:
        user_skills = [s.strip().lower() for s in user_skill_input.split(",")]

        # Skill match
        def skill_match(required_skills):
            job_skills = [s.strip().lower() for s in required_skills.split(",")]
            return len(set(user_skills) & set(job_skills))

        jobs_df["Skill Match"] = jobs_df["required_skills"].apply(skill_match)

        # Filter by exp & salary
        filtered_jobs = jobs_df[
            (jobs_df["min_exp"] <= years_exp) &
            (jobs_df["salary_range_low"] <= desired_salary) &
            (jobs_df["salary_range_high"] >= desired_salary)
        ]

        filtered_jobs = filtered_jobs[filtered_jobs["Skill Match"] > 0]
        filtered_jobs = filtered_jobs.sort_values(by="Skill Match", ascending=False)

        if filtered_jobs.empty:
            st.error("❌ No matching jobs found. Try modifying your input.")
        else:
            st.success(f"✅ {len(filtered_jobs)} Matching Jobs Found!")

            st.dataframe(
                filtered_jobs[[
                    "job_id", "company_name", "role", "city",
                    "required_skills", "min_exp",
                    "salary_range_low", "salary_range_high",
                    "Skill Match"
                ]]
            )

            csv = filtered_jobs.to_csv(index=False)
            st.download_button("📥 Download as CSV", csv, "job_recommendations.csv")
