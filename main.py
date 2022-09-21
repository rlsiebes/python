import requests
from bs4 import BeautifulSoup

URL = 'https://blue-stack.nl/evenementen/'
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="content")
#print(results.prettify())


name_elements = results.find_all("div", class_="tribe-common-g-row tribe-events-calendar-latest-past__event-row")

for  name in name_elements:
  event_name = name.find("a", class_="tribe-events-calendar-latest-past__event-title-link tribe-common-anchor-thin")

  month = name.find("span", class_="tribe-events-calendar-latest-past__event-date-tag-month")
  day = name.find("span", class_="tribe-events-calendar-latest-past__event-date-tag-daynum")
  year = name.find("span", class_="tribe-events-calendar-latest-past__event-date-tag-year")
  month_upper=month.text.strip()
  events_elements = results.find_all("div", class_="tribe-events-calendar-latest-past__event-date-tag tribe-common-g-col")
  print(f'{month_upper.upper()} {day.text.strip()} {year.text.strip()} {event_name.text.strip()}')

