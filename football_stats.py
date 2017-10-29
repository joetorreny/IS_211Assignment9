from bs4 import BeautifulSoup
import requests


def main():
    url = "https://www.cbssports.com/nfl/stats/playersort/nfl/year-2017-season-regular-category-touchdowns"
    result = requests.get(url)
    data = result.text
    soup = BeautifulSoup(data, "lxml")
    table = soup.find("table", attrs={"class": "data"})
    table_rows = table.find_all("tr")
    for table_row in table_rows:
        if "id" in table_row.attrs:
            td = table_row.find_all("td")
            row_data = [i.text for i in td]
            print("Player: {}, Position: {}, Team: {}, Touchdowns: {}".format(row_data[0], row_data[1], row_data[2],
                                                                              row_data[6]))

if __name__ == "__main__":
    main()
