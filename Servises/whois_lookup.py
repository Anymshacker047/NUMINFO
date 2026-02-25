import whois

def whois_lookup(domain):
    try:
        data = whois.whois(domain)
        return f"""
Domain: {domain}
Registrar: {data.registrar}
Creation Date: {data.creation_date}
Expiry Date: {data.expiration_date}
"""
    except:
        return "Invalid domain or error fetching WHOIS"
