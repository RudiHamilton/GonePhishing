from hostapdModule import HostapdConfig
def hostapd_module():
    hostapd = HostapdConfig()
    while True:
        print("""
           ==== Hostapd Configuration ====
           1. Change SSID
           2. Enable Password
           3. Disable Password
           4. Change Channel
           5. Set AP Mode
           6. Toggle Hidden SSID
           7. Change Country Code
           8. Restart Hostapd
           0. Back to Main Menu
           """)
        choice = input("Enter choice: ").strip()
        if choice == "0":
            break
        try:
            if choice == "1":
                ssid = input("Enter new SSID: ").strip()
                hostapd.change_ssid(ssid)
            elif choice == "2":
                password = input("Enter password (8-63 characters): ").strip()
                hostapd.enable_password(password)
            elif choice == "3":
                hostapd.disable_password()
            elif choice == "4":
                channel = int(input("Enter channel number: ").strip())
                hostapd.change_channel(channel)
            elif choice == "5":
                mode = input("Enter mode (g for 2.4GHz, a for 5GHz): ").strip()
                hostapd.set_ap_mode(mode)
            elif choice == "6":
                hidden = input("Hide SSID? (yes/no): ").strip().lower() == "yes"
                hostapd.toggle_hidden(hidden)
            elif choice == "7":
                country_code = input("Enter country code (e.g., US): ").strip()
                hostapd.change_country_code(country_code)
            elif choice == "8":
                hostapd.restart_hostapd()
            else:
                print("Invalid choice, please try again.")
        except Exception as e:
            print(f"Error: {e}")
def dnsmasq_module():
    print("Dnsmasq configuration module here...")

def internet_sharing_module():
    print("Internet Sharing module here...")

def security_module():
    print("Security module here...")

def monitoring_module():
    print("Monitoring module here...")

def utilities_module():
    print("Utilities here...")

menu_actions = {
    "1": hostapd_module,
    "2": dnsmasq_module,
    "3": internet_sharing_module,
    "4": security_module,
    "5": monitoring_module,
    "6": utilities_module
}

while True:
    print("""
    ==== Main Menu ====
    1. Hostapd configuration module 
    2. Dnsmasq configuration module 
    3. Internet Sharing module
    4. Security module
    5. Monitoring module
    6. Utilities 
    0. Exit
    """)
    choice = input("Enter choice: ").strip()
    if choice == "0":
        print("Exiting...")
        break
    action = menu_actions.get(choice)
    if action:
        action()
    else:
        print("Invalid choice, please try again.")
