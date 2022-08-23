import rssi
from rssi import RSSI_Localizer

#ifconfig查看无线网口的名字
interface = 'wlp2s0'
rssi_scanner = rssi.RSSI_Scan(interface)

ssids = ['TP-LINK_FF42','25A802','605'] # wifi名称

ap_info = rssi_scanner.getAPinfo(networks=ssids, sudo=True)
rssi_values = [ap['signal'] for ap in ap_info]

# 至少需要三个wifi节点
accessPoints = [{
     'signalAttenuation': 3, 
     'location': {
         'y': 1, 
         'x': 1
     }, 
     # 暂时没搞懂reference是啥意思
     'reference': {
         'distance': 4, 
         'signal': -50
     }, 
     'name': 'TP-LINK_FF42'
},
{
     'signalAttenuation': 4, 
     'location': {
         'y': 1, 
         'x': 7
     }, 
     'reference': {
         'distance': 3, 
         'signal': -50
     }, 
     'name': '25A802'
},
{
     'signalAttenuation': 5, 
     'location': {
         'y': 7, 
         'x': 1
     }, 
     'reference': {
         'distance': 4, 
         'signal': -50
     }, 
     'name': '605'
}
]

localizer = RSSI_Localizer(accessPoints=accessPoints)

position = localizer.getNodePosition(rssi_values)
print(position)