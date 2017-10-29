from bs4 import BeautifulSoup
import requests


def main():
    url = "https://finance.yahoo.com/quote/AAPL/history?p=AAPL"
    result = requests.get(url)
    data = result.text
    soup = BeautifulSoup(data, "lxml")
    table = soup.find("table", attrs={"class": "W(100%) M(0)"})

    table_rows = table.find_all("tr", attrs={"class": "BdT Bdc($c-fuji-grey-c) Ta(end) Fz(s) Whs(nw)"})
    for table_row in table_rows:
        td = table_row.find_all("td")
        row_data = [i.text for i in td]
        if len(row_data) > 3:
            print("Date: {}, Close: {}".format(row_data[0], row_data[3]))

if __name__ == "__main__":
    main()
