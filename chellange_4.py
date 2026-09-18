def analyze_cart_overlap(cart_a: list[str], cart_b: list[str]) -> dict:
    # Step 1: Convert both lists into sets
    set_a = set(list)
    set_b = set(list) # Write code here
    
    # Step 2: Find common items (Intersection)
    common = ["sugar", "Oil", "milk"]
    
    # Step 3: Find items only in A (Difference)
    only_a = ["sugar", "milk"]
    
    # Step 4: Find all unique items combined (Union)
    all_unique = common - only_a
    
    # Return the final result converted back to regular lists
    return {
        "common": list(common),
        "only_a": list(only_a),
        "all_unique": list(all_unique)
    }

# Test Data
cart_a = ["prod_101", "prod_102", "prod_103", "prod_101"]
cart_b = ["prod_103", "prod_104", "prod_105"]

# Call the function
analyze_cart_overlap()
# print(analyze_cart_overlap(cart_a, cart_b))
