import os
import time
import json
from datetime import datetime

# ------------------- Vehicle Database -------------------
vehicles = [
    {"id": 1, "name": "Toyota Corolla", "type": "Car",  "price": 50, "status": "Available"},
    {"id": 2, "name": "Honda Civic",    "type": "Car",  "price": 55, "status": "Available"},
    {"id": 3, "name": "Yamaha R15",     "type": "Bike", "price": 20, "status": "Available"},
    {"id": 4, "name": "Suzuki GSX",     "type": "Bike", "price": 25, "status": "Available"},
    {"id": 5, "name": "Ford Transit",   "type": "Van",  "price": 80, "status": "Available"},
    {"id": 6, "name": "Bajaj Pulsar",   "type": "Bike", "price": 18, "status": "Available"},
]

# Stores every completed/active rental transaction for history & revenue reports
rental_history = []

DATA_FILE = "vehicle_data.json"


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
    print("║ 4. Search Vehicle                        ║")
    print("║ 5. Add New Vehicle                       ║")
    print("║ 6. Remove Vehicle                        ║")
    print("║ 7. View Rental History                   ║")
    print("║ 8. View Revenue Report                   ║")
    print("║ 9. Save Data to File                     ║")
    print("║ 10. Exit                                 ║")
    print("╚══════════════════════════════════════════╝")


def find_vehicle(vehicle_id):
    """Return vehicle dictionary matching the given ID, or None."""
    for v in vehicles:
        if v["id"] == vehicle_id:
            return v
    return None


def next_vehicle_id():
    """Generate the next unique vehicle ID."""
    if not vehicles:
        return 1
    return max(v["id"] for v in vehicles) + 1


# ------------------- Core Features -------------------
def view_vehicles():
    """Display all vehicles in a formatted table."""
    clear_screen()
    print("╔══════════════════════════════════════════╗")
    print("║           🚗 AVAILABLE VEHICLES 🚗       ║")
    print("╚══════════════════════════════════════════╝\n")

    if not vehicles:
        print("ℹ️  No vehicles in the system.")
        pause()
        return

    print(f"{'ID':<4}{'Name':<18}{'Type':<10}{'Price/Day':<12}{'Status'}")
    print("-" * 55)

    for v in vehicles:
        status_icon = "✅" if v["status"] == "Available" else "❌"
        print(f"{v['id']:<4}{v['name']:<18}{v['type']:<10}"
              f"${v['price']:<11}{status_icon} {v['status']}")

    pause()


def rent_vehicle():
    """Rent a vehicle by ID and calculate rental cost."""
    clear_screen()
    print("╔══════════════════════════════════════════╗")
    print("║             🚗 RENT A VEHICLE 🚗         ║")
    print("╚══════════════════════════════════════════╝\n")

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

        # Log this transaction into rental history
        rental_history.append({
            "vehicle_id": vehicle["id"],
            "name": vehicle["name"],
            "days": days,
            "total_cost": total_cost,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M")
        })

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


# ------------------- New Extra Features -------------------
def search_vehicle():
    """Search for vehicles by name keyword or vehicle type."""
    clear_screen()
    print("╔══════════════════════════════════════════╗")
    print("║             🔍 SEARCH VEHICLE 🔍         ║")
    print("╚══════════════════════════════════════════╝\n")

    keyword = input("Enter vehicle name or type to search: ").strip().lower()

    results = [
        v for v in vehicles
        if keyword in v["name"].lower() or keyword in v["type"].lower()
    ]

    if not results:
        print("ℹ️  No matching vehicles found.")
    else:
        print(f"\n{'ID':<4}{'Name':<18}{'Type':<10}{'Price/Day':<12}{'Status'}")
        print("-" * 55)
        for v in results:
            status_icon = "✅" if v["status"] == "Available" else "❌"
            print(f"{v['id']:<4}{v['name']:<18}{v['type']:<10}"
                  f"${v['price']:<11}{status_icon} {v['status']}")

    pause()


def add_vehicle():
    """Add a new vehicle to the system (admin feature)."""
    clear_screen()
    print("╔══════════════════════════════════════════╗")
    print("║             ➕ ADD NEW VEHICLE ➕        ║")
    print("╚══════════════════════════════════════════╝\n")

    try:
        name = input("Enter vehicle name: ").strip()
        vtype = input("Enter vehicle type (Car/Bike/Van): ").strip()
        price = float(input("Enter price per day: "))

        if not name or not vtype:
            print("❌ Vehicle name and type cannot be empty.")
            pause()
            return

        if price <= 0:
            print("❌ Price must be greater than zero.")
            pause()
            return

        new_vehicle = {
            "id": next_vehicle_id(),
            "name": name,
            "type": vtype,
            "price": price,
            "status": "Available"
        }
        vehicles.append(new_vehicle)

        print(f"\n✅ '{name}' added successfully with ID {new_vehicle['id']}!")

    except ValueError:
        print("❌ Invalid input! Price must be a number.")

    pause()


def remove_vehicle():
    """Remove a vehicle from the system by ID (admin feature)."""
    clear_screen()
    print("╔══════════════════════════════════════════╗")
    print("║            ➖ REMOVE VEHICLE ➖          ║")
    print("╚══════════════════════════════════════════╝\n")

    try:
        vehicle_id = int(input("Enter Vehicle ID to remove: "))
        vehicle = find_vehicle(vehicle_id)

        if vehicle is None:
            print("❌ Invalid Vehicle ID.")
        elif vehicle["status"] == "Rented":
            print("❌ Cannot remove a vehicle that is currently rented.")
        else:
            vehicles.remove(vehicle)
            print(f"✅ '{vehicle['name']}' has been removed from the system.")

    except ValueError:
        print("❌ Invalid input! Please enter a numeric Vehicle ID.")

    pause()


def view_rental_history():
    """Display a log of all rental transactions made so far."""
    clear_screen()
    print("╔══════════════════════════════════════════╗")
    print("║           📜 RENTAL HISTORY 📜           ║")
    print("╚══════════════════════════════════════════╝\n")

    if not rental_history:
        print("ℹ️  No rental transactions yet.")
    else:
        print(f"{'Vehicle':<18}{'Days':<6}{'Total':<10}{'Date'}")
        print("-" * 55)
        for record in rental_history:
            print(f"{record['name']:<18}{record['days']:<6}"
                  f"${record['total_cost']:<9}{record['date']}")

    pause()


def view_revenue():
    """Display total revenue earned and basic fleet statistics."""
    clear_screen()
    print("╔══════════════════════════════════════════╗")
    print("║          💰 REVENUE REPORT 💰            ║")
    print("╚══════════════════════════════════════════╝\n")

    total_revenue = sum(record["total_cost"] for record in rental_history)
    total_vehicles = len(vehicles)
    rented_count = len([v for v in vehicles if v["status"] == "Rented"])
    available_count = total_vehicles - rented_count

    print(f"  Total Vehicles     : {total_vehicles}")
    print(f"  Currently Rented   : {rented_count}")
    print(f"  Currently Available: {available_count}")
    print(f"  Total Transactions : {len(rental_history)}")
    print(f"  Total Revenue      : ${total_revenue}")

    pause()


def save_data_to_file():
    """Save current vehicle list and rental history to a JSON file."""
    clear_screen()
    print("╔══════════════════════════════════════════╗")
    print("║            💾 SAVE DATA TO FILE 💾       ║")
    print("╚══════════════════════════════════════════╝\n")

    try:
        data = {
            "vehicles": vehicles,
            "rental_history": rental_history
        }
        with open(DATA_FILE, "w") as f:
            json.dump(data, f, indent=4)
        print(f"✅ Data saved successfully to '{DATA_FILE}'.")

    except OSError:
        print("❌ Error: Could not write to file.")

    pause()


# ------------------- Main Program Loop -------------------
def main():
    """Main entry point running the CLI menu loop."""
    welcome_screen()

    while True:
        main_menu()
        try:
            choice = int(input("\nEnter your choice (1-10): "))

            if choice == 1:
                view_vehicles()
            elif choice == 2:
                rent_vehicle()
            elif choice == 3:
                return_vehicle()
            elif choice == 4:
                search_vehicle()
            elif choice == 5:
                add_vehicle()
            elif choice == 6:
                remove_vehicle()
            elif choice == 7:
                view_rental_history()
            elif choice == 8:
                view_revenue()
            elif choice == 9:
                save_data_to_file()
            elif choice == 10:
                clear_screen()
                print("╔══════════════════════════════════════════╗")
                print("║   🚗 Thank you for using our system! 🚗  ║")
                print("║              Goodbye! 👋                 ║")
                print("╚══════════════════════════════════════════╝")
                break
            else:
                print("❌ Invalid choice! Please select between 1-10.")
                pause()

        except ValueError:
            print("❌ Invalid input! Please enter a number (1-10).")
            pause()


if __name__ == "__main__":
    main()
