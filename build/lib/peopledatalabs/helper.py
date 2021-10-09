import json
from pathlib import Path
import configparser


class helper(object):


    def __init__(self, debug=False):
        self.debug = debug


    def check_if_config_directory_exists(self):
        # Windows WindowsPath('C:/Users/XXX')
        try:
            home = str(Path.home())
            if Path(home+'/.pdl').is_dir():

                if self.debug:
                    print('Found config directory')

                return True
            return False
        except:
            return False

    def check_if_config_file_exists(self):
        # Windows WindowsPath('C:/Users/XXX')
        try:
            home = str(Path.home())
            if Path(home+'/.pdl/config').is_file():
                if self.debug:
                    print('Found config file')
                return True
            return False
        except:
            return False

    def get_api_key(self):
        home = str(Path.home())

        config = configparser.ConfigParser()
        config.read(home+'/.pdl/config')

        if self.debug:
            print('sections: '+str(config.sections()))

        if 'data' in config.sections():
            if self.debug:
                print('found data section')
            if 'api_key' in config['data']:
                return config['data']['api_key']
        return None



    def print_menu(self):  ## Your menu design here
        print(30 * "-", "MENU", 30 * "-")
        print("1. Phone number with 1(example: 15159860271)")
        print("2. Email")
        print("3. Name,Address,City,State,Zip")
        print("4. Exit")
        print(67 * "-")


    def pretty_json(self, input):
        data = {}
        data['likelihood'] = input['likelihood']
        data['birth_year'] = input['data']['birth_year']
        data['birth_date'] = input['data']['birth_date']
        data['facebook_url'] = input['data']['facebook_url']
        data['linkedin_url'] = input['data']['linkedin_url']
        data['personal_emails'] = input['data']['personal_emails']
        data['emails'] = input['data']['emails']
        data['mobile_phone'] = input['data']['mobile_phone']
        data['phone_numbers'] = input['data']['phone_numbers']

        json_formatted_str = json.dumps(data, indent=2)
        print(json_formatted_str)

