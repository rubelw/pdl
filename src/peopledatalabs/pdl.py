#!/usr/bin/env python3

import requests
import argparse
from peopledatalabs.helper import helper





def main() -> None:

    # Create the parser
    my_parser = argparse.ArgumentParser(prog='pdl',formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    # Add the arguments
    my_parser.add_argument('--debug', action='store_true', help='Turn on debugging')

    # Execute parse_args()
    args = my_parser.parse_args()


    loop = True

    myhelper = helper(args.debug)

    myhelper.get_version()
    myhelper.check_package()


    if myhelper.check_if_config_directory_exists():
        if myhelper. check_if_config_file_exists():
            api_key = myhelper.get_api_key()

            if args.debug:
                print('api_key: '+str(api_key))

            if api_key:

                pdl_version = "v5"
                pdl_url = "https://api.peopledatalabs.com/" + pdl_version + "/person/enrich"


            while loop:  ## While loop which will keep going until loop = False
                myhelper.print_menu()  ## Displays menu
                choice = input("Enter your choice [1-5]: ")

                if choice == "1":
                    phone = input("Enter phone number with 1(example: 1515986xxxx): ")
                    params = {
                        "api_key": api_key,
                        "phone": phone
                    }

                    json_response = requests.get(pdl_url, params=params).json()
                    myhelper.pretty_json(json_response)

                ## You can add your code or functions here
                elif choice == "2":
                    email = input("Enter email: ")
                    params = {
                        "api_key": api_key,
                        "email": email
                    }

                    json_response = requests.get(pdl_url, params=params).json()
                    myhelper.pretty_json(json_response)


                ## You can add your code or functions here
                elif choice == "3":
                    name = input("Enter name(example: Fred Flinstone): ")
                    address = input("Enter address(example: 604 SW RubbleRock Drive): ")
                    locality = input("Enter city(example: Bedrock): ")
                    region = input("Enter state(example: IA): ")
                    zip = input("Enter zipcode(example: 50111: ")

                    params = {
                        "api_key": api_key,
                        "name": name,
                        "street_address": address,
                        "locality": locality,
                        "region": region,
                        "postal_code": "zip"
                    }

                    json_response = requests.get(pdl_url, params=params).json()
                    myhelper.pretty_json(json_response)


                ## You can add your code or functions here
                elif choice == "4":
                    name = input("Enter name(example: Will Rubel): ")
                    locality = input("Enter city(example: grimes): ")
                    region = input("Enter State(example: IA): ")
                    full_output = myhelper.yes_or_no("Do you want full output: ")

                    params = {
                        "api_key": api_key,
                        "name": name,
                        "locality": locality,
                        "region": region
                    }

                    json_response = requests.get(pdl_url, params=params).json()
                    myhelper.pretty_json(json_response, full_output)

                ## You can add your code or functions here
                elif choice == "5":
                    name = input("Enter name(example: Fred Flinstone): ")
                    region = input("Enter State(example: IA): ")
                    full_output = myhelper.yes_or_no("Do you want full output: ")

                    params = {
                        "api_key": api_key,
                        "name": name,
                        "region": region
                    }

                    json_response = requests.get(pdl_url, params=params).json()
                    myhelper.pretty_json(json_response, full_output)

                ## You can add your code or functions here
                elif choice == "6":
                    print("Bye")
                    ## You can add your code or functions here
                    loop = False  # This will make the while loop to end as not value of loop is set to False
                else:
                    # Any integer inputs other than values 1-5 we print an error message
                    input("Wrong option selection. Enter any key to try again..")

if __name__ == '__main__':


    main()


