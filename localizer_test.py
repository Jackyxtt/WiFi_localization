from rssi import RSSI_Localizer

accessPoint = {
     'signalAttenuation': 3, 
     'location': {
         'y': 1, 
         'x': 1
     }, 
     'reference': {
         'distance': 4, 
         'signal': -50
     }, 
     'name': 'TP-LINK_FF42'
}
signalStrength = -68

rssi_localizer_instance = RSSI_Localizer(accessPoints=accessPoint)
distance = rssi_localizer_instance.getDistanceFromAP(accessPoint, signalStrength)
print(distance)