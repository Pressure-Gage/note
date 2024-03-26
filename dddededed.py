packages = {
    "1": {
        "name": "McBasic Package",
        "phone_cost": 50,
        "included_storage": "2 GB",
        "storage_options": {},
        "diamonds": "N/A",
        "cloud_backup": False,
        "case_options": {
            "rubber": 20,
            "carbon fibre": 100,
            "no": 0
        },
        "extra_fast_battery_charger": 100,
        "insurance_cost": 1
    },
    "2": {
        "name": "Average Joe Package",
        "phone_cost": 150,
        "included_storage": "8 GB",
        "storage_options": {
            "1": 200,  # Additional 64 GB
            "2": 350   # Additional 128 GB
        },
        "diamonds": "N/A",
        "cloud_backup": True,
        "case_options": {
            "rubber": 20,
            "carbon fibre": 100,
            "no": 0
        },
        "extra_fast_battery_charger": 100,
        "insurance_cost": 5
    },
    "3": {
        "name": "Rich Kid Pro Package",
        "phone_cost": 800,
        "included_storage": "32 GB",
        "storage_options": {
            "1": 200,  # Additional 64 GB
            "2": 350   # Additional 128 GB
        },
        "diamonds": 200,
        "cloud_backup": True,
        "case_options": {
            "rubber": 20,
            "carbon fibre": 100,
            "no": 0
        },
        "extra_fast_battery_charger": 100,
        "insurance_cost": 20
    }
}

data_packages = {
    "pay as you go": 0,
    "1 gb": 10,
    "2 gb": 15,
    "5 gb": 40,
    "20 gb": 150
}

def calculate_cost():
    total_cost = 0
    monthly_cost = 0

    print("Packages:\n1. McBasic Package\n2. Average Joe Package\n3. Rich Kid Pro Package")
    package_choice = input("Choose your package (1/2/3): ")

    if package_choice in packages:
        total_cost += packages[package_choice]["phone_cost"]
        print(f"Selected package: {packages[package_choice]['name']} - ${packages[package_choice]['phone_cost']}")

        # Storage options
        if packages[package_choice]["storage_options"]:
            print("Storage options:")
            for option, cost in packages[package_choice]["storage_options"].items():
                print(f"{option}. Additional {cost} GB")
            storage_option = input("Choose an option (leave blank if none): ")
            if storage_option in packages[package_choice]["storage_options"]:
                total_cost += packages[package_choice]["storage_options"][storage_option]

        # Extra diamonds
        if "diamonds" in packages[package_choice] and packages[package_choice]["diamonds"] != "N/A":
            diamonds_choice = input("Do you want extra diamonds? (yes/no): ").lower()
            if diamonds_choice == "yes":
                total_cost += 200

        # Cloud data backup
        if packages[package_choice]["cloud_backup"]:
            backup_choice = input("Do you want cloud data backup? (yes/no): ").lower()
            if backup_choice == "yes":
                email = input("Please enter your email address: ")
                print("1. 1 year ($20)\n2. 2 years ($35)")
                backup_option = input("Choose an option (1/2): ")
                if backup_option == "1":
                    total_cost += 20
                elif backup_option == "2":
                    total_cost += 35

        # Protective case
        case_choice = input("Do you want a protective case? (rubber/carbon fibre/no): ").lower()
        if case_choice in packages[package_choice]["case_options"]:
            total_cost += packages[package_choice]["case_options"][case_choice]

        # Extra fast battery charger
        charger_choice = input("Do you want an extra fast battery charger? (yes/no): ").lower()
        if charger_choice == "yes":
            total_cost += 100

        # Trade-in discount
        trade_in = input("Do you have an old phone to trade in? (yes/no): ").lower()
        if trade_in == "yes":
            total_cost -= 40

        # Insurance
        insurance_choice = input("Do you want insurance? (yes/no): ").lower()
        if insurance_choice == "yes":
            monthly_cost += packages[package_choice]["insurance_cost"]

        # Data package
        data_choice = input("Choose your data package (Pay as you go, 1 GB, 2 GB, 5 GB, 20 GB): ").lower()
        if data_choice in data_packages:
            monthly_cost += data_packages[data_choice]

        print(f"Total purchase cost: ${total_cost}")
        print(f"Monthly cost: ${monthly_cost}")
    else:
        print("Invalid package choice. Please restart the program and select a valid package.")

calculate_cost()