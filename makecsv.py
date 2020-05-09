import csv


def save_to_csv(reviews):
    file = open("reviews.csv", mode="w")
    writter = csv.writer(file)
    writter.writerow(["Title", "Detail", "Rating"])
    for review in reviews:
        writter.writerow(list(review.value()))
    return
