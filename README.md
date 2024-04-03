# Web_Scraping and Chrome Automation

This README provides details about a Python script that combines web scraping functionality and Chrome automation. Additionally, it includes information about fetching links from a website and processing them, along with automating the Chrome browser to accept LinkedIn profile connections.

## Setup

### 1. Requirements
- Python 3.x installed on your system
- Required Python packages: `requests`, `beautifulsoup4`
  You can install these packages via pip: `pip install requests beautifulsoup4`
- Ensure Chrome browser is installed on your system.

### 2. Fetching Links
- The function `fetch_links()` fetches links from a specified URL using `requests` and `BeautifulSoup`.
- It recursively fetches links from subsequent pages until no more pages are found.
- The fetched links are stored in a CSV file named `links.csv`.

### 3. Chrome Automation for LinkedIn
- The `main()` function automates actions in Chrome.
- It reads links from the `links.csv` file and sends requests to each URL using a `requests.Session`.
- It extracts the title of each webpage using regular expressions.
- This script can be extended to automate interactions with LinkedIn profiles, such as accepting connection requests.

## Usage
1. Complete the setup steps.
2. Run the script.
3. The web scraping part will fetch links and print titles of the webpages.
4. For Chrome automation, ensure proper setup and installation of required dependencies.

## Notes
- Additional error handling can be implemented as per your requirements.
- For Chrome automation, ensure that the Chrome WebDriver is properly configured and accessible.
- You can extend the Chrome automation part to perform various actions on LinkedIn profiles, such as accepting connection requests, sending messages, etc.
- Feel free to modify the script to suit your needs or integrate additional functionalities.
