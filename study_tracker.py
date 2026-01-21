# Smart Study Companion

from datetime import datetime

DATA_FILE = "data.txt"

def save_to_file(session):
    with open("data.txt", "a") as file:
        file.write(f"{session['subject']} , {session['duration']}\n")

def load_from_file():
    data = []
    try:
        with open("data.txt", "r")as file:
            for line in file: 
                subject,duration = line.strip().split(",")
                data.append({
                    "subject":subject,
                    "duration":int(duration)
                    })
    except FileNotFoundError:
        pass
    return data

#----------------- Analytics ---------------------
def view_all_sessions(data):
    if not data:
        print("No study sessions recorded yet.")
        return
    
    print("\n All Study Sessions: ")
    for s in data:
        date = s.get("date", "N/A")
        print(f" Date: {date} | Subject:{s['subject']} | Duration:{s['duration']} minutes")

def study_summary(data):
    if not data:
        print("No study data available.")
        return

    summary = {}
    total_time = 0

    for s in data:
        subject = s["subject"]
        duration = s["duration"]

        summary[subject] = summary.get(subject, 0) + duration
        total_time += duration

    print("\n Study Summary: ")
    for subject, minutes in summary.items():
        print(f"{subject}: {minutes} minutes")

    print(f"\n Total Study Time: {total_time} minutes")

    weakest_subject = min(summary, key=summary.get)
    print(f"Focus More On: {weakest_subject}")

#-------------- Menu ------------------
def show_menu():
    print("\n--- Smart Study Companion ---")
    print("1. Add Study Session")
    print("2. View All Session")
    print("3. View Study Summary")
    print("4. Exit")

#-------------- Main ------------------
study_data = load_from_file()

while True:
    show_menu()
    choice = input("Enter your choice: ").strip()

    if choice == "1":
        subject = input("Enter subject name: ").strip()
        try:
            duration = int(input("Enter study duration (in minutes): "))
        except ValueError:
            print("Please eter a valid number for duration.")
            continue

        session = {
            "date":datetime.now().strftime("%Y-%m-%d"),
            "subject": subject,
            "duration": duration
            }
        
        study_data.append(session)
        save_to_file(session)
        print("Study session added successfully!")

    elif choice == "2":
        view_all_sessions(study_data)
    
    elif choice == "3":
        study_summary(study_data)

    elif choice == "4":
        print("Goodbye! keep studying")
        break

    else:
        print("Invalid choice. Try again.")

