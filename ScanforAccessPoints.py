import rssi

interface = 'wlp2s0'
rssi_scanner = rssi.RSSI_Scan(interface)

ssids = ['TP-LINK_FF42','25A802']

# sudo argument automatixally gets set for 'false', if the 'true' is not set manually.
# python file will have to be run with sudo privileges.
# ap_info = rssi_scanner.getAPinfo(networks=ssids, sudo=True)

# scan all 
ap_info = rssi_scanner.getAPinfo(sudo=True)

print(ap_info)