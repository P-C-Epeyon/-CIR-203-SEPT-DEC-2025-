# Exercise 3: Tuples in Medical Records (Healthcare Sector)

# 1. Create a patient tuple
patient = ("John Doe", 45, "120/80", 72)

# 2. Access and print the patient’s age and heart rate
print("Age:", patient[1])
print("Heart Rate:", patient[3])

# 3. Explanation:
# Tuples are suitable because:
# - They are immutable, preventing accidental modification of important medical data.
# - They are faster and more memory‑efficient than lists.
# - They provide a fixed structure ideal for patient vital records.

# 4. Convert tuple to list, update heart rate, convert back to tuple
patient_list = list(patient)
patient_list[3] = 80  # updated heart rate
updated_patient = tuple(patient_list)
print("Updated Patient:", updated_patient)

# 5. Tuple of 5 patients and extracting all names
patients = (
    ("John Doe", 45, "120/80", 72),
    ("Alice Smith", 30, "110/70", 68),
    ("Bob Lee", 55, "130/85", 75),
    ("Maria Khan", 40, "115/78", 70),
    ("David Chen", 60, "140/90", 80)
)

names = [patient[0] for patient in patients]
print("Patient Names:", names)
