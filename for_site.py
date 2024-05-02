import webbrowser
import time

def open_google_search(domains_file):

    with open(domains_file, 'r') as file:
        for domain in file:
            domain = domain.strip()  # Remove any extra whitespace or newlines
            if domain: 
                url = f"https://www.google.com/search?q=site:{domain}"
                webbrowser.open_new_tab(url)
                time.sleep(1) 

domains_file = 'wildcards.txt'


open_google_search(domains_file)
