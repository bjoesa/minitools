from bs4 import BeautifulSoup
import urllib3
import certifi

http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
url = input('Type your URL: ')
website = http.urlopen('GET', url)
soup = BeautifulSoup(website.data, "lxml")

print('-------------------')
sitestatus = website.status
if sitestatus == 200:
    print('Website status OK (', sitestatus,')')
elif sitestatus == 401:
    print('Website status: ', sitestatus,' (unauthorized)')
else:
    print('Website status: ', sitestatus,' (sth. is strange `O.o´)')

''' 
    processing  : 102
    ok          : 200
    unauthorized: 401
    not_found   : 404 
'''
print('-------------------')
print('Link list and connection test: ')

for link in soup.findAll('a'):
    print(link.get('href'))
    try:
        r = http.request('GET', link.get('href'))
        print('status: ', r.status)
    except:
        # if Exception is raised
        print('no connection test...')
        pass

print('\n---- FINISH ----')
