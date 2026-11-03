import pandas as pd

# Student data
data = {
    "Student": ["Sara", "Mona", "Nora", "Lama", "Huda"],
    "Math": [90, 85, 78, 92, 88],
    "Science": [95, 80, 85, 89, 91],
    "English": [88, 90, 82, 95, 87]
}

# Create DataFrame
df = pd.DataFrame(data)

# Calculate average grades
df["Average"] = df[["Math", "Science", "English"]].mean(axis=1)

# Display results
print(df)

# Find the highest-performing student
top_student = df.loc[df["Average"].idxmax()]

print("\nTop Student:")
print(top_student)
