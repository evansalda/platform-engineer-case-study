import argparse
import urllib.request
import re
import time

# Arguments parsing
parser = argparse.ArgumentParser()
parser.add_argument('-u', action='append', nargs='+', required=True)
parser.add_argument('-o', choices=['stdout', 'json'], required=True)
args = parser.parse_args()
urls_args = args.u # List of URLs
output_args = args.o

# Returns a JSON with each URL as key and a list of its links as value
def get_links(urls):
    result = {}
    for url in urls:
        str_url = url[0] # str_url is a value list
        content = urllib.request.urlopen(str_url).read().decode('latin-1')
        pattern = r'"' + str_url + r'[^"]*"' # Used the following link to write the regex : https://www.regextester.com/3269
        str_url_links = re.findall(pattern, content)
        result[str_url] = str_url_links # appending the current url as key and the associated links as value
    return(result)

# Prints each link (absolute URL) found on each URL provided in the arguments
def print_links_stdout(links_dict):
    for url in links_dict:
        for link in links_dict[url]:
            print(link)

# Creates a JSON with each URL of as key and a list of relative paths extracted from the URL as value
def print_links_json(links_dict):
    pretty_links_dict = {}
    for url in links_dict:
        # Trailing "/" handling + adding double quotes to the dictionary keys
        if url[:-1] == "/":
            quoted_url = '"' + url[:-1] + '"'
        else:
            quoted_url = '"' + url + '"'
        paths = []
        for link in links_dict[url]:
            if link != quoted_url: # Avoiding having empty paths in the value (when a link in a page is the page's URL itself)
                path = link.replace(url, '')
                paths.append(path)
        pretty_links_dict[quoted_url] = paths
    print(pretty_links_dict)

def main(urls, output):
    dict = get_links(urls)
    match output:
        case 'stdout':
            print_links_stdout(dict)
            while True:
                time.sleep(1)
        case 'json':
            print_links_json(dict)
            while True:
                time.sleep(1)

main(urls_args, output_args)