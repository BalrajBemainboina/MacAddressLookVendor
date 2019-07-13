import json
import urllib2
def FetchAndDisplayMac():
        try:
                MAC_Address =raw_input('Enter the MAC address here :')
                UrltoGet = 'https://api.macaddress.io/v1?apiKey=at_q0Q9nURy5wBf3P3qrfdsyGE1G8yHP&output=json&search=' + MAC_Address
                GetDetails = urllib2.urlopen(UrltoGet)
                Details_Obj = GetDetails.read()
                RawData = json.loads(Details_Obj)
                print('********************************************************')
                print('VendorName : ' + RawData['vendorDetails']['companyName'])
                print('********************************************************')
        except Exception as e:
                print ('Something Went Wrong, Please Note the MAC address format Should be : A1-B2-C3-00-00-00 or A1:B2:C3::00:00:00')
                print str(e)

if __name__ == '__main__':
        FetchAndDisplayMac()