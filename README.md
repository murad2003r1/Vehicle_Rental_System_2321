# 🚗 Vehicle Rental System (CLI)

A clean, beginner-friendly **Vehicle Rental Management System** built entirely with **Python 3**, running as a Command Line Interface (CLI) application. No external libraries required — only Python's built-in modules.

```
╔══════════════════════════════════════════╗
║ 🚗  VEHICLE RENTAL SYSTEM - MAIN MENU     ║
╠══════════════════════════════════════════╣
║ 1. View Available Vehicles                ║
║ 2. Rent a Vehicle                         ║
║ 3. Return a Vehicle                       ║
║ 4. Search Vehicle                         ║
║ 5. Add New Vehicle                        ║
║ 6. Remove Vehicle                         ║
║ 7. View Rental History                    ║
║ 8. View Revenue Report                    ║
║ 9. Save Data to File                      ║
║ 10. Exit                                  ║
╚══════════════════════════════════════════╝
```

---

## 📌 About

This project simulates a real-world vehicle rental service, allowing an admin/user to manage a fleet of vehicles — view availability, rent out vehicles, process returns, track rental history, and generate basic revenue reports, all from a polished terminal interface with Unicode box-style UI.

It was built as a practical exercise combining core Python concepts: data structures, functions, control flow, exception handling, and file I/O — kept simple enough for a university-level project or viva presentation.

---

## ✨ Features

- 🎨 Beautiful welcome screen and box-style main menu
- 🚗 View all vehicles with live availability status
- 💰 Rent a vehicle with automatic cost calculation
- 🔄 Return a rented vehicle
- 🔍 Search vehicles by name or type
- ➕ Add new vehicles to the fleet
- ➖ Remove vehicles (with safety check for currently rented ones)
- 📜 View complete rental transaction history
- 📊 Revenue report with fleet statistics
- 💾 Save all data to a JSON file for persistence
- 🛡️ Robust input validation using `try-except`

---

## 🛠️ Tech Stack

- **Language:** Python 3
- **Interface:** Command Line Interface (CLI)
- **Libraries used:** `os`, `time`, `json`, `datetime` *(all built-in — no installation needed)*

---

## 📂 Project Structure

```
vehicle-rental-system/
│
├── main.py              # Complete application source code
├── vehicle_data.json     # Auto-generated when data is saved
└── README.md             # Project documentation
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.x installed on your system

### Installation

```bash
git clone https://github.com/<your-username>/vehicle-rental-system.git
cd vehicle-rental-system
```

### Run the Application

```bash
python main.py
```
*(On Linux/Mac you may need to use `python3 main.py`)*

---

## 🎮 How to Use

1. Launch the program — a welcome screen appears.
2. The main menu is displayed with numbered options.
3. Enter a number (1–10) and press **Enter** to select an action.
4. Follow the on-screen prompts for renting, returning, searching, or managing vehicles.
5. After each action, press **Enter** to return to the main menu.
6. Select **10. Exit** to close the program.

---

## 🧩 Functions Overview

| Function | Description |
|---|---|
| `clear_screen()` | Clears the terminal screen |
| `pause()` | Waits for user to press Enter before continuing |
| `welcome_screen()` | Displays the startup welcome screen |
| `main_menu()` | Displays the main menu UI |
| `find_vehicle(vehicle_id)` | Finds a vehicle by its ID |
| `next_vehicle_id()` | Generates a unique ID for new vehicles |
| `view_vehicles()` | Displays all vehicles in a formatted table |
| `rent_vehicle()` | Handles the full vehicle rental process |
| `return_vehicle()` | Handles returning a rented vehicle |
| `search_vehicle()` | Searches vehicles by name/type keyword |
| `add_vehicle()` | Adds a new vehicle to the system |
| `remove_vehicle()` | Removes a vehicle from the system |
| `view_rental_history()` | Displays all past rental transactions |
| `view_revenue()` | Displays total revenue and fleet statistics |
| `save_data_to_file()` | Saves vehicles and rental history to a JSON file |
| `main()` | Entry point that runs the main program loop |

---

## 🗃️ Data Model

Each vehicle is stored as a dictionary with the following structure:

```python
{
    "id": 1,
    "name": "Toyota Corolla",
    "type": "Car",
    "price": 50,
    "status": "Available"
}
```

All vehicles are stored in a single list (`vehicles`), and every rental transaction is logged in a separate list (`rental_history`) with vehicle name, days rented, total cost, and timestamp.

---

## 🔮 Future Improvements

- [ ] Load previously saved JSON data on startup
- [ ] Add user authentication (admin vs customer roles)
- [ ] Add due-date tracking and late-return penalties
- [ ] Export rental history/reports to CSV or PDF
- [ ] Convert to a GUI or web-based interface

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---

## 🙋 Author

**Md Murad Hossain**
Digital Marketing Specialist | CSE (Cybersecurity) Student

If you found this project useful, consider giving it a ⭐ on GitHub!
