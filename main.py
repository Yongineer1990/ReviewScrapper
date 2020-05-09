from tripadvisor import get_reviews as tripadvisor
# from booking import get_last_pages as booking
from makecsv import save_to_csv as makefile

tripadvisor_review = tripadvisor()
all_review = tripadvisor_review
makefile(all_review)

# booking_review = booking()
# print(booking_review)
