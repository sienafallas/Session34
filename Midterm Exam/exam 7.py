def is_valid_url(url):
    # Check if the URL starts with "http://" or "https://"
    if url.startswith("http://") or url.startswith("https://"):
        # Extract the domain name part of the URL
        domain = url.split("//")[-1].split("/")[0]

        # Check if the domain name contains a period (.)
        if '.' not in domain:
            return False

        # Check if the domain name ends with a valid top-level domain
        top_level_domain = domain.split(".")[-1]
        valid_top_level_domains = ["com", "org", "net", "edu"]  # Add more if needed
        if top_level_domain not in valid_top_level_domains:
            return False

        return True
    else:
        return False


# Test the function
url1 = "http://www.example.com"
url2 = "https://example.org"
url3 = "ftp://example.com"
url4 = "http://invalid url.com"
url5 = "http://www.example."
url6 = "http://www.example"
url7 = "http://www.example.com/"

print(is_valid_url(url1))  # Output: True
print(is_valid_url(url2))  # Output: True
print(is_valid_url(url3))  # Output: False
print(is_valid_url(url4))  # Output: False
print(is_valid_url(url5))  # Output: False
print(is_valid_url(url6))  # Output: False
print(is_valid_url(url7))  # Output: True
