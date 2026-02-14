import psutil

def is_connected():
    try:
        # Get all network interfaces
        interfaces = psutil.net_if_stats()
        # Check each interface for an active Wi-Fi connection
        for interface, stats in interfaces.items():
            if stats.isup and "Wi-Fi" in interface:
                return True
        return False
    except Exception as e:
        print("Error:", e)
        return False

# Check if Wi-Fi is connected
if is_connected():
    print("Connected to Wi-Fi")
else:
    print("Not connected to Wi-Fi")
