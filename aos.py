import requests
import json
import xml.etree.ElementTree as eTree

storeListUrl = 'https://www.apple.com/autopush/hk/retail/storelist/stores.xml'
storesXml = requests.get(storeListUrl)
storesXmlTree = eTree.fromstring(storesXml.content)
storeList = {}
for store in storesXmlTree.find('country').findall('store'):
    storeList[store.find('appleid').text] = store.find('name').text
# print(storeList)

stores = ','.join(storeList.keys())
# print(stores)

partNumber = 'MQA62ZP/A'
productLocatorUrl = 'https://mobileapp.apple.com/mnm/p/hk/product-locator/quotes?stores=' + stores + '&pn=' + partNumber
productLocatorHeaders = {
    'X-DeviceConfiguration': 'ss=3.00;dim=1125x2436;m=iPhone;v=iPhone10,3;vv=5.1;sv=11.4.1',
    'x-ma-pcmh': 'REL-5.1.0'
}

pickupMessageUrl = 'https://www.apple.com/hk-zh/shop/retail/pickup-message?parts.0=' + partNumber

pickupResponse = requests.get(productLocatorUrl, headers=productLocatorHeaders)
pickupMessageResponse = requests.get(pickupMessageUrl)

pickupMessage = json.loads(pickupMessageResponse.content)
pickupPartNumber = json.loads(pickupResponse.content)['partNumber']
productName = pickupMessage['body']['content']['pickupEligibility'][partNumber]['storePickupProductTitle']

isPickupBuyable = json.loads(pickupResponse.content)['buyable']

print(productName + ' - Buyable : ' + str(isPickupBuyable))

