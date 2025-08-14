import os
import shutil
import subprocess

class HostapdConfig:
    def __init__(self, config_path="/etc/hostapd/hostapd.conf", backup_path="/etc/hostapd/hostapd.conf.bak"):
        self.config_path = config_path
        self.backup_path = backup_path
        self.config_data = self._load_config()

    def _load_config(self):
        """Load the current hostapd config into memory."""
        if not os.path.exists(self.config_path):
            raise FileNotFoundError(f"{self.config_path} not found!")
        with open(self.config_path, "r") as f:
            return f.readlines()

    def _save_config(self):
        """Backup and save config changes."""
        shutil.copy2(self.config_path, self.backup_path)
        with open(self.config_path, "w") as f:
            f.writelines(self.config_data)

    def _update_line(self, key, value):
        """Find and replace a config line by key."""
        found = False
        for i, line in enumerate(self.config_data):
            if line.strip().startswith(f"{key}="):
                self.config_data[i] = f"{key}={value}\n"
                found = True
                break
        if not found:
            self.config_data.append(f"{key}={value}\n")

    def change_ssid(self, ssid):
        self._update_line("ssid", ssid)
        self._save_config()

    def enable_password(self, password):
        if not (8 <= len(password) <= 63):
            raise ValueError("Password must be 8-63 characters")
        self._update_line("wpa", "2")
        self._update_line("wpa_passphrase", password)
        self._save_config()

    def disable_password(self):
        self.config_data = [line for line in self.config_data if not line.strip().startswith(("wpa=", "wpa_passphrase"))]
        self._update_line("auth_algs", "1")
        self._save_config()

    def change_channel(self, channel):
        self._update_line("channel", str(channel))
        self._save_config()

    def set_ap_mode(self, mode="g"):
        """g = 2.4GHz, a = 5GHz (if supported)."""
        self._update_line("hw_mode", mode)
        self._save_config()

    def toggle_hidden(self, hidden=True):
        self._update_line("ignore_broadcast_ssid", "1" if hidden else "0")
        self._save_config()

    def change_country_code(self, code):
        self._update_line("country_code", code.upper())
        self._save_config()

    def restart_hostapd(self):
        """Restart the hostapd service."""
        subprocess.run(["sudo", "systemctl", "restart", "hostapd"], check=True)
        subprocess.run(["sudo", "systemctl", "status", "hostapd", "--no-pager"])

