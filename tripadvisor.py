import requests
from bs4 import BeautifulSoup

page = 0
resort = "The_Sun_Siyam_Iru_Fushi_Maldives-Iru_fushi"
URL = f"https://www.tripadvisor.co.kr/Hotel_Review-g4473389-d929150-Reviews-or{page}-{resort}.html#REVIEWS"


def get_last_pages():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    pagenum = soup.find("div", {"class": "pageNumbers"}).find_all("a")
    pages = []
    for i in pagenum:
        pages.append(int(i.string))
    max_page = pages[-1]
    return max_page


def extract_review(html):
    title = html.find("div", {
        "data-test-target": "review-title"
    }).find("span").string
    text = html.find("div", {"class": "cPQsENeY"}).find("span").string
    rating = html.find("div", {
        "data-test-target": "review-rating"
    }).find("span")["class"]
    if rating[-1] == "bubble_50":
        star = 5.0
    elif rating[-1] == "bubble_40":
        star = 4.0
    elif rating[-1] == "bubble_30":
        star = 3.0
    elif rating[-1] == "bubble_20":
        star = 2.0
    else:
        star = 1.0
    print(f"title : {title}")
    print(f"review : {text}")
    print(f"star : {star}")
    return {"title": title, "text": text, "star": star}


def extract_reviews(last_page):
    increase_page = 5
    reviews = []
    for i in range(last_page):
        print(f"Scrapping review on Tripadvisor {i+1}")
        if i == 0:
            result = requests.get(URL)
        else:
            increase_page = i * 5
            replace_url = URL.replace("or0", f"or{increase_page}")
            result = requests.get(replace_url)
        soup = BeautifulSoup(result.text, "html.parser")
        reviewContainer = soup.find_all(
            "div", {
                "class":
                "location-review-review-list-parts-SingleReview__mainCol--1hApa"
            })
        for result in reviewContainer:
            review = extract_review(result)
            reviews.append(review)
    return reviewContainer


def get_reviews():
    last_page = get_last_pages()
    reviews = extract_reviews(last_page)
    return reviews
