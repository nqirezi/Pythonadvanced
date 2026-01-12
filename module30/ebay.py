import requests
url ='https://www.ebay.com/itm/326721900007?epid=5049289868&itmmeta=01KESPDZB0VCKN18F8Y5B21C65&hash=item4c12248de7:g:vnMAAOSwaMZkCeUu&itmprp=enc%3AAQAKAAAA4NHOg0D50eDiCdi%2FfP0r02voSlhZGC6j5esus%2BNN8206elmfySnbFhpdUopbO8L%2BJG1wN%2BxpK5uaRoYEGNyY6RU8kWw3CeAYqGERT3eV%2FZ11jO6YRSvFqKXK%2BeOBXOpikktScDXZgNPGygb85bKX4kFN3gY0apUJeI3XNroPVeri%2B8dphmKUuiKwoWx8YeZ0MB%2BBwClVy1U8cWCl7bVOKqP3hana6Cs28Hi2dVZ%2BYOha4UilR9wktawOgmZIeYY43Jp1dozC91iAPBOVMXr2VDr70GwpTBvo4TgnTjcMaHbV%7Ctkp%3ABFBM1PW3tvZm&var=515734623323'

response = requests.get(url)

if response.status_code == 200:
    print(response.text)
else:
    print(f"Failed to retrive the webpage:Status code{url}")
    