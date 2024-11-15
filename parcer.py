import requests
from bs4 import BeautifulSoup

def print_cityweather(city,temperature):
    res = city + " : " + temperature
    return res
def parse_website(url):
    # Send HTTP-request
    response = requests.get(url)

    # Check if the request was successful (code 200)
    if response.status_code == 200:
        # Using BeautifulSoup for parcing HTML-code
        soup = BeautifulSoup(response.text, 'html.parser')

        # Search  <td> with class "today-temp"
        td_tag = soup.find('p', class_='today-temp')

        # Get the text
        if td_tag:
            value = td_tag.text
            complete = value
            return complete
        else:
            return None
    else:
        print(f"Не вдалося здійснити запит. Код помилки: {response.status_code}")
        return None


def get_current_weather(url):
    # Sends a GET request to the specified URL to retrieve the webpage content.
    response = requests.get(url)
    # Checks if the request was successful (status code 200).
    if response.status_code == 200:
        # Parses the HTML content of the page using BeautifulSoup.
        soup = BeautifulSoup(response.text, 'html.parser')
        # Finds all 'div' elements with the class 'description'.
        description_tags = soup.find_all('div', class_='description')
        # If no 'description' tag is found, returns "N/A".
        return description_tags[0].get_text(strip=True) if description_tags else "N/A"
    else:
        # If the request fails, prints an error message with the status code.
        print(f"Не вдалося здійснити запит. Код помилки: {response.status_code}")
        return None




