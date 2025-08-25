import scapy.all as scapy
import os
import sys
import platform
from pyfiglet import Figlet



def is_admin():
    if platform.system() == "Windows":
        try:
            import ctypes
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False
    else:
        return os.geteuid() == 0

def require_admin():
    if not is_admin():
        if platform.system() == "Windows":
            import ctypes
            ctypes.windll.shell32.ShellExecuteW(
                None, "runas", sys.executable, " ".join(sys.argv), None, 1
            )
            sys.exit(0)
        else:
            print("⚠️ This script requires root privileges. Run with: sudo python3 " + sys.argv[0])
            sys.exit(1)

def arp_scan(ip_range):
    arp_request = scapy.ARP(pdst=ip_range)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    
    devices = []
    for sent, received in answered_list:
        devices.append({"ip": received.psrc, "mac": received.hwsrc})
    
    return devices

def print_devices(devices):
    print("\nDiscovered devices:")
    print("IP Address\t\tMAC Address")
    print("-" * 40)
    for device in devices:
        print(f"{device['ip']}\t\t{device['mac']}")

def print_banner():
    f = Figlet(font='doom')
    print(f.renderText('SIFWG - OMER'))

def main():
    print_banner()
    require_admin()
    ip_range = "192.168.1.0/24"
    
    try:
        devices = arp_scan(ip_range)
        if devices:
            print_devices(devices)
        else:
            print("No devices found on the network.")
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Ensure you have the necessary permissions and Scapy is installed.")
    
    input("\n✅ Scan complete. Press Enter to exit...")

if __name__ == "__main__":
    main()
