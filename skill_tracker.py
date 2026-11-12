# Personal Skill Tracker

skills = []

# Add new skill
def add_skill():
    print("\n--- Add New Skill ---")

    name = input("Enter skill name: ")
    level = input("Enter skill level (Beginner/Intermediate/Advanced): ")
    progress = int(input("Enter progress percentage (0-100): "))

    if progress < 0 or progress > 100:
        print("Invalid progress percentage!")
        return

    skill = {
        "name": name,
        "level": level,
        "progress": progress
    }

    skills.append(skill)

    print("Skill added successfully!")


# View all skills
def view_skills():
    print("\n--- My Skills ---")

    if len(skills) == 0:
        print("No skills available.")

    else:
        for i in range(len(skills)):
            print("\nSkill Number:", i + 1)
            print("Skill Name:", skills[i]["name"])
            print("Level:", skills[i]["level"])
            print("Progress:", skills[i]["progress"], "%")


# Update skill progress
def update_progress():
    name = input("Enter skill name to update: ")

    found = False

    for skill in skills:
        if skill["name"].lower() == name.lower():

            progress = int(input("Enter new progress (0-100): "))

            if progress >= 0 and progress <= 100:
                skill["progress"] = progress
                print("Progress updated successfully!")
            else:
                print("Invalid progress percentage!")

            found = True
            break

    if found == False:
        print("Skill not found.")


# Search for a skill
def search_skill():
    name = input("Enter skill name to search: ")

    found = False

    for skill in skills:
        if skill["name"].lower() == name.lower():

            print("\nSkill Found!")
            print("Name:", skill["name"])
            print("Level:", skill["level"])
            print("Progress:", skill["progress"], "%")

            found = True
            break

    if found == False:
        print("Skill not found.")


# View completed skills
def completed_skills():
    print("\n--- Completed Skills ---")

    found = False

    for skill in skills:
        if skill["progress"] == 100:
            print(skill["name"])
            found = True

    if found == False:
        print("No completed skills yet.")


# Calculate overall progress
def overall_progress():
    if len(skills) == 0:
        print("No skills available.")
    else:
        total = 0

        for skill in skills:
            total = total + skill["progress"]

        average = total / len(skills)

        print("Overall Learning Progress:", average, "%")


# Main menu
while True:

    print("\n===== PERSONAL SKILL TRACKER =====")
    print("1. Add Skill")
    print("2. View All Skills")
    print("3. Update Progress")
    print("4. Search Skill")
    print("5. View Completed Skills")
    print("6. Overall Progress")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_skill()

    elif choice == "2":
        view_skills()

    elif choice == "3":
        update_progress()

    elif choice == "4":
        search_skill()

    elif choice == "5":
        completed_skills()

    elif choice == "6":
        overall_progress()

    elif choice == "7":
        print("Thank you for using Personal Skill Tracker!")
        break

    else:
        print("Invalid choice! Try again.")