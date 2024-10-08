import requests

# URL for the issues in the pandas repository
url = "https://api.github.com/repos/pandas-dev/pandas/issues"

# Make a GET request to the GitHub API
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    issues = response.json()
    # Extract the html_url for each issue
    html_urls = [issue['html_url'] for issue in issues]
    
    # Print the list of html_urls
    for url in html_urls:
        print(url)
else:
    print("Failed to retrieve issues:", response.status_code)
