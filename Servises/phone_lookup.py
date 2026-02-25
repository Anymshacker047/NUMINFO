import requests
import os

API_KEY = os.getenv("ABSTRACT_API_KEY")

def phone_lookup(number):
    if not API_KEY:
        return "No API key provided."

    url = f"https://phonevalidation.abstractapi.com/v1/?api_key={API_KEY}&phone={number}"
    res = requests.get(url).json()

    return f"""
Number: {number}
Valid: {res.get('valid')}
Country: {res.get('country', {}).get('name')}
Carrier: {res.get('carrier')}
Line Type: {res.get('type')}
"""
