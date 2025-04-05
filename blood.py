class BloodDonation:
    def __init__(self):
        self.donor_list = []

    def add_donor(self, name, blood_group, age, donation_date):
        donor = {
            "Name": name,
            "Blood Group": blood_group,
            "Age": age,
            "Donation Date": donation_date,
        }
        self.donor_list.append(donor)
        print(f"Donor {name} added successfully!")

    def total_donations(self):
        return len(self.donor_list)

    def display_donors(self):
        if not self.donor_list:
            print("No donors available.")
            return
        print("Donor List:")
        for idx, donor in enumerate(self.donor_list, start=1):
            print(f"{idx}. {donor['Name']} | Blood Group: {donor['Blood Group']} | Age: {donor['Age']} | Donation Date: {donor['Donation Date']}")


if __name__ == "__main__":
    donation_tracker = BloodDonation()

    while True:
        print("\nBlood Donation Tracker")
        print("1. Add Donor")
        print("2. View Total Donations")
        print("3. Display Donor List")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter donor name: ")
            blood_group = input("Enter blood group (e.g.,AB+, A+, B-, O+):")
            age = int(input("Enter donor age: "))
            donation_date = input("Enter donation date (YYYY-MM-DD): ")
            donation_tracker.add_donor(name, blood_group, age, donation_date)
        elif choice == "2":
            print(f"Total Donations: {donation_tracker.total_donations()}")
        elif choice == "3":
            donation_tracker.display_donors()
        elif choice == "4":
            print("Exiting program. Stay healthy!")
            break
        else:
            print("Invalid choice. Please try again.")
