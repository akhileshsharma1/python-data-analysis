import phonenumbers
from phonenumbers import geocoder
phonenumber_1 = phonenumbers.parse("+977-9803062084")

print(geocoder.description_for_number(phonenumber_1,"en"))