from bs4 import BeautifulSoup
import requests


def main():
    url = "https://www.wunderground.com/history/airport/KNYC/2015/1/11/MonthlyHistory.html"
    result = requests.get(url)
    data = result.text
    soup = BeautifulSoup(data, "lxml")
    table = soup.find("table", attrs={"id": "obsTable"})

    table_bodys = table.find_all("tbody")
    day_num = 1
    for table_body in table_bodys[1:]:
        td = table_body.find_all("td")
        get_temp = lambda x: td[x].find("span").text
        high = get_temp(1)
        average = get_temp(2)
        low = get_temp(3)
        print("January {} temperature - High: {}, Average: {}, Low: {}".format(day_num, high, average, low))
        day_num += 1

if __name__ == "__main__":
    main()
