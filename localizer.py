from rssi import RSSI_Localizer
rssi_localizer_instance = RSSI_Localizer()

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
     'name': 'dd-wrt'
}
signalStrength = -69

distance = rssi_localizer_instance.getDistanceFromAP(accessPoint, signalStrength)
print(distance)

