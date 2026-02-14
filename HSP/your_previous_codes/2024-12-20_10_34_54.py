import os
import subprocess

def is_network_available(ssid):
    try:
        result = subprocess.check_output("netsh wlan show networks", shell=True, encoding="utf-8", errors="replace")
        if ssid in result:
            print(f"Network '{ssid}' is available.")
            return True
        else:
            print(f"Network '{ssid}' is NOT available.")
            return False
    except Exception as e:
        print(f"An error occurred while checking for the network: {e}")
        return False
def connect_to_wifi(ssid, password):
    if not is_network_available(ssid):
        print("Please ensure your hotspot is turned on and try again.")
        return
    try:
        wifi_profile = f"""
        <?xml version="1.0"?>
        <WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1">
            <name>{ssid}</name>
            <SSIDConfig>
                <SSID>
                    <name>{ssid}</name>
                </SSID>
            </SSIDConfig>
            <connectionType>ESS</connectionType>
            <connectionMode>auto</connectionMode>
            <MSM>
                <security>
                    <authEncryption>
                        <authentication>WPA2PSK</authentication>
                        <encryption>AES</encryption>
                        <useOneX>false</useOneX>
                    </authEncryption>
                    <sharedKey>
                        <keyType>passPhrase</keyType>
                        <protected>false</protected>
                        <keyMaterial>{password}</keyMaterial>
                    </sharedKey>
                </security>
            </MSM>
        </WLANProfile>
        """
        profile_path = f"{ssid}_profile.xml"
        with open(profile_path, "w") as file:
            file.write(wifi_profile)
        os.system(f'netsh wlan add profile filename="{profile_path}"')
        print(f"Connecting to {ssid}...")
        os.system(f'netsh wlan connect name="{ssid}"')
        os.remove(profile_path)
        print(f"Connection attempt to {ssid} completed.")
    except Exception as e:
        print(f"An error occurred: {e}")
connect_to_wifi("Redmi Note 7 Pro", "11111111")
