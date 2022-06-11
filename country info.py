from countryinfo import CountryInfo
count=input("Enter your country :")
country=CountryInfo(count)
print("Capital is :",country.capital())
print("Currency is  :",country.currencies())
print("Languages are  :",country.languages())
print("Border are :",country.borders())
