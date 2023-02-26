def get_names_from_url(url=""):
    parts = url.split("/")
    clean_parts = []
    for part in parts:
        new_part = ""
        for dn in part.split("."):
            new_part += dn.capitalize()
        if new_part == "":
            new_part = part
        if part != "":
            clean_parts.append(
                ''.join(c for c in new_part if c.isalnum())[:15]
            )
    return clean_parts[1:]


print(get_names_from_url(
    "https://finance.yahoo.com/?guccounter=1&guce_referrer=aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8&guce_referrer_sig=AQAAAFtqSeNfJLpJ916YN0alaOJvdbwRK8ws1y5EAUiLmYVu71uIU66KuPoVhn_prCSjUdpU7_KKiRxc5VHfLfrSe4pkxT7Mfv7zn7Pvv-b8v7HqGEnWFRqb_ewJ0zSFBji-cuHwlIPHHxp6coxHrX11o9PJHq5_JIOd8JZYiHv-0-w2"))
