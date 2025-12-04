# Linked list of student records

student1 = {
    "name": "Lisa Monica",
    "adm_no": "CIM/00089/024",
    "subjects": {
        "Data structures": "B",
        "Algorithms": "A",
        "Databases": "B"
    },
    "next": None
}

student2 = {
    "name": "Henry Heavens",
    "adm_no": "CIM/00090/024",
    "subjects": {
        "Data structures": "A",
        "Algorithms": "C",
        "Databases": "A"
    },
    "next": None
}

student3 = {
    "name": "Angel Pauls",
    "adm_no": "CIM/00091/024",
    "subjects": {
        "Data structures": "B",
        "Algorithms": "A",
        "Databases": "C"
    },
    "next": None
}

# Linking the nodes to form a linked list
student1["next"] = student2
student2["next"] = student3

# Traversing the linked list
head = student1
current = head

while current is not None:
    print("Name:", current["name"])
    print("Admission Number:", current["adm_no"])
    print("Subjects and Grades:")
    for subject, grade in current["subjects"].items():
        print("   ", subject, ":", grade)
    print()  # Blank line for readability
    current = current["next"]
