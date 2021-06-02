#!/usr/bin/env python3

# Created by Malcolm Tompkins
# Created on May 31, 2021
# Converts standard address into mailing address


def address_conversion(user_name, street_number, appartment_number,
                       street_name, city_name, user_province,
                       postal_code, user_appartment):
    user_name = user_name.upper()
    street_name = street_name.upper()
    city_name = city_name.upper()
    user_province = user_province.upper()
    postal_code = postal_code.upper()

    if user_appartment == "n":
        appartment_number = None
        converted_address = (user_name + "\n" + street_number + " " +
                             street_name + "\n" + city_name + " " +
                             user_province + " " + postal_code)
    else:
        converted_address = (user_name + "\n" + appartment_number + "-" + street_number + " "
        + street_name + "\n" + city_name + " "  + user_province + " " + postal_code)
    return converted_address
    
    
def main():
    print("This program converts standard address into mailing address ")
    user_name = input("Enter your full name: ")
    user_appartment = input("Do you live in an appartment? (y,n): ")
    if user_appartment == "y":
        appartment_number = input("Enter your appartment number: ")
    street_number = input("Enter your street number: ")
    street_name = input("Enter the name and type of your street: ")
    city_name = input("Enter the name of your city: ")
    user_province = input("Enter the obreviation of your province(eg: ON): ")
    postal_code = input("Enter your postal code (123 456): ")
    if user_appartment == "n":
        appartment_number = None
        address_conversion(user_name, street_number,appartment_number, street_name, city_name, user_province, postal_code, user_appartment)
        converted_address = address_conversion(user_name, street_number, appartment_number, street_name, city_name, user_province, postal_code, user_appartment)
        print(converted_address)
    else:
        address_conversion(user_name, street_number, appartment_number, street_name, city_name, user_province, postal_code, user_appartment)
        converted_address = address_conversion(user_name, street_number, appartment_number, street_name, city_name, user_province, postal_code, user_appartment)
        print(converted_address)
    
        
if __name__ == "__main__":
      main()
   