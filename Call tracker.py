import phonenumbers
from phonenumbers import geocoder, carrier, timezone
ph = input("Enter the phone number of the person using +91 at the beginning: ")
pho = phonenumbers.parse(ph, "ch")
country = geocoder.description_for_number(pho,'en')
time_z = timezone.time_zones_for_number (pho)
carr = carrier.name_for_number(pho, 'en')

print(country, time_z,carr)
