# Exercise 2: Lists in Logistics Management (Supply Chain Sector)

# 1. Create a list of 10 delivery routes
routes = [
    "Nairobi-Westlands",
    "Mombasa-Port",
    "Nakuru-CBD",
    "Kisumu-Airport",
    "Nyeri-Town",
    "Nanyuki-Base",
    "Eldoret-Market",
    "Naivasha-Lakeview",
    "Thika-Road",
    "Kericho-Greens"
]

# 2. Append a new route and remove a discontinued one
routes.append("Malindi-Beach")
routes.remove("Thika-Road")  # discontinued route

# 3. Sort alphabetically and reverse
routes.sort()
routes.reverse()

# 4. Count routes starting with 'N'
count_N = sum(1 for r in routes if r.startswith("N"))

# 5. List comprehension for routes longer than 10 characters
long_routes = [r for r in routes if len(r) > 10]

# Display results
print("Final Route List:", routes)
print("Number of routes starting with 'N':", count_N)
print("Routes longer than 10 characters:", long_routes)
