import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

employees_df = pd.read_csv("employees_final.csv")
jobs_df = pd.read_csv("jobs.csv")


def recommend_jobs(employee_id, top_n=5):
    # Get single employee data
    employee = employees_df[employees_df['employee_id'] == employee_id].iloc[0]
    
    # Extract fields
    emp_skills = employee['skillset']
    emp_exp = employee['years_exp']
    emp_expected_salary = employee['expected_salary']
    emp_city = employee['city']
    
    # TF-IDF vectorization on job required skills
    tfidf = TfidfVectorizer(stop_words='english')
    job_skill_matrix = tfidf.fit_transform(jobs_df['required_skills'])
    
    # Convert employee skills to same vector space
    emp_vector = tfidf.transform([emp_skills])
    
    # Skill similarity score
    skill_similarity = cosine_similarity(emp_vector, job_skill_matrix).flatten()
    
    # Adding score to job dataframe
    jobs_df['skill_score'] = skill_similarity
    
    # Experience Match (penalty if not enough)
    jobs_df['exp_score'] = jobs_df['min_exp'].apply(
        lambda x: 1 if emp_exp >= x else emp_exp / x
    )

    # Salary Match (0 if job doesn't meet expectation)
    jobs_df['salary_score'] = jobs_df.apply(
        lambda row: 1 if emp_expected_salary <= row['salary_range_high'] else 0,
        axis=1
    )
    
    # Final Weighted Score
    jobs_df['final_score'] = (
        0.65 * jobs_df['skill_score'] +
        0.2 * jobs_df['exp_score'] +
        0.15 * jobs_df['salary_score']
    )
    
    # Recommend top jobs
    recommendations = jobs_df.sort_values(by='final_score', ascending=False).head(top_n)
    
    return recommendations[['job_id', 'company_name', 'role', 'city', 'required_skills', 'final_score']]

# Example usage:
print(recommend_jobs("E0001"))