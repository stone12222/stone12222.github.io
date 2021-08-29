countryname_income={}

rawdata=open('rawdata.txt','r')
lines=rawdata.readlines()
for line in lines:
    l=line.split("\t")
    country=l[1]
    income=l[2].strip("\n")
    countryname_income[country.upper()]=income

country_index={"A":set()}
for country_name in countryname_income.keys():
    first_letter=country_name[0]
    if first_letter not in country_index:
        country_index[first_letter]={country_name}
    else:
        country_index[first_letter].add(country_name)

def get_user_input():
    user_input = input("Enter a country name or the first letter of the country name: ")
    user_input=user_input.strip(" ").upper()
    return user_input

user_input=get_user_input()
while(user_input!="QUIT"):
    if len(user_input)==1:
        countries=country_index[user_input]
        print(countries)
    elif len(user_input)>1:
        if user_input.upper() in countryname_income:
            print(countryname_income[user_input])
        else:
            print("Does not exist")
    user_input=get_user_input()