import requests

def ip_lookup(ip):
    url = f"https://ipinfo.io/{ip}/json"
    res = requests.get(url).json()

    return f"""
IP: {ip}
City: {res.get('city')}
Region: {res.get('region')}
Country: {res.get('country')}
Org: {res.get('org')}
"""
