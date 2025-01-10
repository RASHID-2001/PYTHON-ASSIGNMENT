"""
GET A NAME OF DAY FROM THE USER AND PRINT WHETHER THEN GIVE DAY IS WEEK DAY OR WEEKEND
""""
day = input("Enter a day of the week: ").lower()  # Convert to lowercase for case-insensitive matching
match day:
    case "monday" | "tuesday" | "wednesday" | "thursday" | "friday":
        print(f"{day.capitalize()} is a weekday.")
    case "saturday" | "sunday":
        print(f"{day.capitalize()} is a weekend.")
    case _:
        print("Invalid day. Please enter a valid day of the week.")
