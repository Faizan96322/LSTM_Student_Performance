import pandas as pd

# Read data from CSV file
data = pd.read_csv('input_data.csv')


# Define a function to calculate performance categories for each row
def calculate_performance(row):
    # Calculate semester grades
    semester_grades = [row['1-1 percentage'], row['1-2 percentage'], row['2-1 percentage'],
                       row['2-2 percentage'], row['3-1 percentage'], row['3-2 percentage']]

    # Calculate dropout category
    dropout = 1 if min(semester_grades) < 35 and row['Attendance_Percentage '] < 30 else 0

    # Calculate good performance category
    good_performance = 1 if all(grade > 60 for grade in semester_grades) else 0

    # Calculate poor performance category
    poor_performance = 1 if max(semester_grades) < 40 else 0

    # Calculate support required category
    support_required = 1 if any(40 <= grade < 60 for grade in semester_grades) else 0

    # Calculate eligibility for placement category
    eligible_for_placement = 1 if all(grade > 65 for grade in semester_grades) and (
                row['Coding_Skills '] or row['Academic_awards_and_achievements '] or row[
            'Extracurricular_Activities ']) else 0

    # Return the results as a dictionary
    return {
        'Dropout': dropout,
        'Good performance': good_performance,
        'Poor performance': poor_performance,
        'Support required': support_required,
        'Eligible for placement': eligible_for_placement
    }


# Apply the function to each row in the dataset to calculate performance categories
performance_data = data.apply(calculate_performance, axis=1, result_type='expand')

# Concatenate the original data with the performance categories data
result_data = pd.concat([data, performance_data], axis=1)

# Write the results to a new CSV file
result_data.to_csv('output_data.csv', index=False)
print(data.columns)