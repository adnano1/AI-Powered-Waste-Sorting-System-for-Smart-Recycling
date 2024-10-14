def sort_waste(waste_type):
    if waste_type == "plastic":
        print("Sorting plastic into the plastic bin.")
    elif waste_type == "metal":
        print("Sorting metal into the metal bin.")
    elif waste_type == "paper":
        print("Sorting paper into the paper bin.")
    elif waste_type == "organic":
        print("Sorting organic waste.")

# Example usage: based on detected waste type
sort_waste("plastic")
