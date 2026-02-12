# Name: Pujitha
# Project: Personal Information Manager
# Description: Thi program stores and displays perssonal information
# using variables, user input, validation, and formatted output.

# ----------------------
# Step:2 Store static information
# ----------------------
name="Pujitha"
age=22
city="Vijayawada"
hobby="Reading"

# -----------------
# Step 3:Get user input
# -----------------

print("Welcome to the Personal Information Manager!\n")

# Ask for favourite food with validation
favorite_food=input("Enter your favorite food: ").strip()
while favorite_food=="":
    print("Food cannot be empty. Please try again.")
    favorite_food=input("Enter your favorite food: ").strip()

# Ask for favorite color with validation
fav_color=input("Enter your favorite color: ").strip()
while fav_color=="":
    print("Color cannot be empty. Please try again.")
    fav_color=input("Enter your favorite color: ").strip()

# ---------------------
# step 4: Display Information
# ---------------------

# Convert name and city to title case
formatted_name=name.title()
formatted_city=city.title()

# Calculate age in months
age_in_mnths=age*12

print("\n" + "="*40)
print("     PERSONAL INFORMATION")
print("="*40)

print(f"Name           : {formatted_name}")
print(f"Age            : {age} years")
print(f"Age in months  : {age_in_mnths} months")
print(f"City           : {formatted_city}")
print(f"Hobby          : {hobby.title()}")

print("-" * 40)
print("FAVORITES")
print("-" * 40)

print(f"Favorite Food  : {favorite_food.title()}")
print(f"Favorite Color : {fav_color.title()}")

print("=" * 40)

# -------------------------------
# Step 6: Goodbye message
# -------------------------------
print("\nThank you for using the Personal Information Manager!")
print("Have a great day!")