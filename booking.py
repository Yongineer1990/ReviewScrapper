import requests
from bs4 import BeautifulSoup
from selenium import webdriver

page = 0
resort = "iru-fushi-beach-amp-spa-maldives"
URL = f"https://www.booking.com/reviewlist.ko.html?aid=1288395&label=metagha-link-localuniversalKR-hotel-883643_dev-desktop_los-1_bw-23_dow-Monday_defdate-1_room-0_lang-ko_curr-KRW_gstadt-2_rateid-0_aud-0_cid-_gacid-6641365084_mcid-10&sid=3d1cd13b4a8d929e2081b9e34a9eeec9&cc1=mv&dist=1&pagename={resort}&srpvid=f8d18c17720d0034&type=total&rows=10&_=1588967809233&offset={page};rows=10"
print(URL)


def get_last_pages():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    pagenum = soup.find(
        "div", {"class": "bui-pagination__list"}).find("div")
    return pagenum
    # pages = []
    # for i in pagenum:
    #     pages.append(int(i.string))
    # max_page = pages[-1]
    # return max_page

    # def extract_review(html):
    #     title = html.find("div", {
    #         "data-test-target": "review-title"
    #     }).find("span").string
    #     text = html.find("div", {"class": "cPQsENeY"}).find("span").string
    #     rating = html.find("div", {
    #         "data-test-target": "review-rating"
    #     }).find("span")["class"]
    #     if rating[-1] == "bubble_50":
    #         star = 5.0
    #     elif rating[-1] == "bubble_40":
    #         star = 4.0
    #     elif rating[-1] == "bubble_30":
    #         star = 3.0
    #     elif rating[-1] == "bubble_20":
    #         star = 2.0
    #     else:
    #         star = 1.0
    #     return {"title": title, "text": text, "star": star}

    # def extract_reviews(last_page):
    #     increase_page = 5
    #     reviews = []
    #     for i in range(last_page):
    #         print(f"Scrapping review on Tripadvisor {i+1}")
    #         if i == 0:
    #             result = requests.get(URL)
    #         else:
    #             increase_page = i * 5
    #             replace_url = URL.replace("or0", f"or{increase_page}")
    #             result = requests.get(replace_url)
    #         soup = BeautifulSoup(result.text, "html.parser")
    #         reviewContainer = soup.find_all(
    #             "div", {
    #                 "class":
    #                 "location-review-review-list-parts-SingleReview__mainCol--1hApa"
    #             })
    #         for result in reviewContainer:
    #             review = extract_review(result)
    #             reviews.append(review)
    #     return reviewContainer
    # def get_reviews():
    #     last_page = get_last_pages()
    #     reviews = extract_reviews(last_page)
    #     return reviews
