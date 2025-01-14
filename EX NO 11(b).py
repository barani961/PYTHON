
import pandas as pd
data = {'EmployeeID': [1, 2, 3, 4, 5],'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emma'],'Department': ['HR', 'IT', 'HR', 'IT', 'Finance'],'Salary': [50000, 60000, 55000, 65000, 70000],'YearsExperience': [3, 5, 2, 7, 4],'PerformanceRating': [4, 3, 5, 3, 4]
}
df = pd.DataFrame(data)
avg_salary_by_department = df.pivot_table(values='Salary', index='Department', aggfunc='mean')
print("Average Salary by Department:")
print(avg_salary_by_department)
performance_by_experience = df.pivot_table(values='PerformanceRating', index='YearsExperience', aggfunc='mean')
print("\nDistribution of Performance Ratings based on Years of Experience:")
print(performance_by_experience)
