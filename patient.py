def search_disease(patients, disease):
    result = []
    for p in patients:
        if p["Disease"].lower() == disease.lower():
            result.append(p["Name"])
    return result

# Example
patients = [
    {"Name": "Alice", "Age": 30, "Disease": "Flu"},
    {"Name": "Bob", "Age": 45, "Disease": "Diabetes"},
    {"Name": "Charlie", "Age": 35, "Disease": "Flu"}
]

print("Patients with Flu:", search_disease(patients, "Flu"))