from requests import get
from bs4 import BeautifulSoup
import csv
import time
from random import randint

names, url, author, price, ratings, avgrat = [], [], [], [], [], []

for j in range(1, 6):
    urlxx = "https://www.amazon.in/gp/bestsellers/books/ref=zg_bs_pg_{0}?ie=UTF8&pg={0}".format(
        j)
    response = get(urlxx)
    html_soup = BeautifulSoup(response.text, 'html.parser')
    book_containers = html_soup.find_all('div', class_='zg_itemImmersion')

    time.sleep(randint(1, 3))

    for i in range(len(book_containers)):
        x = book_containers[i].find(
            'div', attrs={'class': 'p13n-sc-truncate'})
        if x:
            names.append(x.text.strip())
        else:
            names.append("Not available")

        x = book_containers[i].find(
            'div', attrs={'class': 'a-row a-size-small'})
        if x:
            p = x.get_text().strip()
            if(p == 'Paperback' or p == 'Hardcover'):
                author.append("Not available")
            else:
                author.append(x.get_text().strip())
        else:
            author.append("Not available")

        x = book_containers[i].find('span', attrs={'class': 'p13n-sc-price'})
        if x:
            y = "\u20B9" + x.text.strip()
            price.append(y)
        else:
            price.append("Not available")

        x = book_containers[i].find(
            'a', attrs={'class': 'a-size-small a-link-normal'})
        if x:
            ratings.append(x.text.strip())
        else:
            ratings.append("Not available")

        x = book_containers[i].find(
            'a', attrs={'class': 'a-link-normal'})
        if x:
            y = "https://www.amazon.in" + x["href"]
            url.append(y)
        else:
            url.append("Not available")

        x = book_containers[i].find('i', attrs={'class': 'a-icon-star'})
        if x:
            avgrat.append(x.text.strip())
        else:
            avgrat.append("Not available")

with open('in_book.csv', 'w') as output:
    writer = csv.writer(output, delimiter=';')
    writer.writerow(["Name", "URL", "Author", "Price",
                     "Number of Ratings", "Average Rating"])
    for i in range(100):
        writer.writerow([names[i], url[i], author[i],
                         price[i], ratings[i], avgrat[i]])
