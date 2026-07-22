import os
import time

# ------------------- Vehicle Database -------------------
vehicles = [
    {"id": 1, "name": "Toyota Corolla", "type": "Car",       "price": 50, "status": "Available"},
    {"id": 2, "name": "Honda Civic",    "type": "Car",       "price": 55, "status": "Available"},
    {"id": 3, "name": "Yamaha R15",     "type": "Bike",      "price": 20, "status": "Available"},
    {"id": 4, "name": "Suzuki GSX",     "type": "Bike",      "price": 25, "status": "Available"},
    {"id": 5, "name": "Ford Transit",   "type": "Van",       "price": 80, "status": "Available"},
    {"id": 6, "name": "Bajaj Pulsar",   "type": "Bike",      "price": 18, "status": "Available"},
]


# ------------------- Utility Functions -------------------
def clear_screen():
    """Clear the terminal screen (works on Windows and Linux/Mac)."""
    os.system("cls" if os.name == "nt" else "clear")


def pause():
    """Pause execution until the user presses Enter."""
    input("\nPress Enter to Continue...")


def welcome_screen():
    """Display a beautiful welcome screen at program start."""
    clear_screen()
    print("╔══════════════════════════════════════════╗")
    print("║        🚗  VEHICLE RENTAL SYSTEM  🚗     ║")
    print("║        Welcome! Drive Your Way Out       ║")
    print("╚══════════════════════════════════════════╝")
    time.sleep(1.5)


def main_menu():
    """Display the main menu with a box-style design."""
    clear_screen()
    print("╔══════════════════════════════════════════╗")
    print("║ 🚗  VEHICLE RENTAL SYSTEM - MAIN MENU    ║")
    print("╠══════════════════════════════════════════╣")
    print("║ 1. View Available Vehicles               ║")
    print("║ 2. Rent a Vehicle                        ║")
    print("║ 3. Return a Vehicle                      ║")
    print("║ 4. Exit                                  ║")
    print("╚══════════════════════════════════════════╝")


# ------------------- Core Features -------------------
def view_vehicles():
    """Display all vehicles in a formatted table."""
    clear_screen()
    print("╔══════════════════════════════════════════╗")
    print("║           🚗 AVAILABLE VEHICLES 🚗       ║")
    print("╚══════════════════════════════════════════╝\n")

    print(f"{'ID':<4}{'Name':<18}{'Type':<10}{'Price/Day':<12}{'Status'}")
    print("-" * 55)

    for v in vehicles:
        status_icon = "✅" if v["status"] == "Available" else "❌"
        print(f"{v['id']:<4}{v['name']:<18}{v['type']:<10}"
              f"${v['price']:<11}{status_icon} {v['status']}")

    pause()


def find_vehicle(vehicle_id):
    """Return vehicle dictionary matching the given ID, or None."""
    for v in vehicles:
        if v["id"] == vehicle_id:
            return v
    return None


def rent_vehicle():
    """Rent a vehicle by ID and calculate rental cost."""
    clear_screen()
    print("╔══════════════════════════════════════════╗")
    print("║             🚗 RENT A VEHICLE 🚗         ║")
    print("╚══════════════════════════════════════════╝\n")

    # Show only available vehicles
    available = [v for v in vehicles if v["status"] == "Available"]
    if not available:
        print("ℹ️  No vehicles are currently available for rent.")
        pause()
        return

    for v in available:
        print(f"{v['id']}. {v['name']} ({v['type']}) - ${v['price']}/day")

    try:
        vehicle_id = int(input("\nEnter Vehicle ID to rent: "))
        vehicle = find_vehicle(vehicle_id)

        if vehicle is None:
            print("❌ Invalid Vehicle ID.")
            pause()
            return

        if vehicle["status"] != "Available":
            print("❌ Sorry, this vehicle is already rented.")
            pause()
            return

        days = int(input("Enter number of rental days: "))
        if days <= 0:
            print("❌ Rental days must be a positive number.")
            pause()
            return

        total_cost = vehicle["price"] * days
        vehicle["status"] = "Rented"

        print("\n╔════════════════════════════════════════╗")
        print("║          ✅ RENTAL SUCCESSFUL! ✅        ║")
        print("╠══════════════════════════════════════════╣")
        print(f"  Vehicle : {vehicle['name']}")
        print(f"  Days    : {days}")
        print(f"  Total   : ${total_cost}")
        print("╚══════════════════════════════════════════╝")

    except ValueError:
        print("❌ Invalid input! Please enter numeric values only.")

    pause()


def return_vehicle():
    """Return a rented vehicle by ID."""
    clear_screen()
    print("╔══════════════════════════════════════════╗")
    print("║           🚗 RETURN A VEHICLE 🚗         ║")
    print("╚══════════════════════════════════════════╝\n")

    try:
        vehicle_id = int(input("Enter Vehicle ID to return: "))
        vehicle = find_vehicle(vehicle_id)

        if vehicle is None:
            print("❌ Invalid Vehicle ID.")
        elif vehicle["status"] == "Available":
            print("ℹ️  This vehicle was not rented.")
        else:
            vehicle["status"] = "Available"
            print("\n╔════════════════════════════════════════╗")
            print("║          ✅ RETURN SUCCESSFUL! ✅        ║")
            print("╠══════════════════════════════════════════╣")
            print(f"  {vehicle['name']} is now available again.")
            print("╚══════════════════════════════════════════╝")

    except ValueError:
        print("❌ Invalid input! Please enter a numeric Vehicle ID.")

    pause()


# ------------------- Main Program Loop -------------------
def main():
    """Main entry point running the CLI menu loop."""
    welcome_screen()

    while True:
        main_menu()
        try:
            choice = int(input("\nEnter your choice (1-4): "))

            if choice == 1:
                view_vehicles()
            elif choice == 2:
                rent_vehicle()
            elif choice == 3:
                return_vehicle()
            elif choice == 4:
                clear_screen()
                print("╔══════════════════════════════════════════╗")
                print("║   🚗 Thank you for using our system! 🚗  ║")
                print("║              Goodbye! 👋                 ║")
                print("╚══════════════════════════════════════════╝")
                break
            else:
                print("❌ Invalid choice! Please select between 1-4.")
                pause()

        except ValueError:
            print("❌ Invalid input! Please enter a number (1-4).")
            pause()


if __name__ == "__main__":
    main()
