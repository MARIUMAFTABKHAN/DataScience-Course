def army_entry():
    height = float(input("Enter your height in feet: "))
    medically_fit = input("Are you medically fit? (yes/no): ").strip().lower()
    is_shooter = input("Are you a trained shooter? (yes/no): ").strip().lower()

    if height >= 6 and medically_fit == 'yes' and is_shooter == 'yes':
        print("You are eligible for the Army.")
    else:
        print("You are not eligible for the Army. Get out.")

def airforce_entry():
    eyesight = input("Is your eyesight 6*6? (yes/no): ").strip().lower()
    if eyesight == 'yes':
        print("You are eligible for the Airforce.")
    else:
        print("You are not eligible for the Airforce. Get out.")

def navy_entry():
    blood_pressure = input("Is your blood pressure normal? (yes/no): ").strip().lower()
    if blood_pressure == 'yes':
        print("You are eligible for the Navy.")
    else:
        print("You are not eligible for the Navy. Get out.")

def civilian_entry():
    print("You are eligible for Civilian departments:")
    print("- Mess Department")
    print("- Accounts Department")
    print("- Procurement Department")

def main():
    try:
        age = int(input("Enter your age: "))

        if age < 18:
            print("You are too young. Get out.")
            return
        elif 18 <= age <= 28:
            print("Welcome to Non-Civilian Department Selection.")
            department = input("Choose your department (army/navy/airforce): ").strip().lower()

            if department == 'army':
                army_entry()
            elif department == 'airforce':
                airforce_entry()
            elif department == 'navy':
                navy_entry()
            else:
                print("Invalid department selected.")
        else:
            print("Welcome to Civilian Department.")
            civilian_entry()

    except ValueError:
        print("Invalid input. Please enter numeric value for age.")

if __name__ == "__main__":
    main()
