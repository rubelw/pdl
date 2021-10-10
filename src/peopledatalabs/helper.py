from pathlib import Path
from peopledatalabs.__init__ import __version__
import subprocess
import sys
import os
import json
import inspect
import urllib.request as urllib2


def lineno():
    """Returns the current line number in our program."""
    return " - helper - "+str(inspect.currentframe().f_back.f_lineno)


class helper(object):


    def __init__(self, debug=False):
        """
        Instantiate object
        :param debug:
        """
        self.debug = debug


    def get_version(self):
        """
        Get the installed version
        :return:
        """
        if self.debug:
            print('get_version'+lineno())

        return __version__


    def get_latest_version_from_list(self, data):

        major_versions = []
        minor_versions = []
        patch_versions = []

        version_data = {}
        for d in data:
            (major, minor, patch) = d.split('.')

            version_data[d] = {}
            version_data[d]['major'] = int(major)
            version_data[d]['minor'] = int(minor)
            version_data[d]['patch'] = int(patch)

            major_versions.append(int(major))

        major_versions = list(dict.fromkeys(major_versions))
        target_major_version = max(major_versions)

        for d in version_data:
            if version_data[d]['major'] == target_major_version:
                minor_versions.append(version_data[d]['minor'])

        minor_versions = list(dict.fromkeys(minor_versions))
        target_minor_version = max(minor_versions)


        for d in version_data:
            if version_data[d]['major'] == target_major_version:
                if version_data[d]['minor'] == target_minor_version:
                    patch_versions.append(version_data[d]['patch'])

        patch_versions = list(dict.fromkeys(patch_versions))

        target_patch_version = max(patch_versions)

        for d in version_data:
            if version_data[d]['major'] == target_major_version:
                if version_data[d]['minor'] == target_minor_version:
                    if version_data[d]['patch'] == target_patch_version:
                        latest_version = d

        if self.debug:
            print('latest version: ' + str(latest_version)+lineno())

        return latest_version

    def check_package(self):
        """
        Check if the installed package is the most current version
        :return:
        """
        if self.debug:
            print("Checking for current version of pdl"+lineno())

        version = self.get_version()

        if self.debug:
            print('Current version: '+str(version)+lineno())

        url = "https://pypi.org/pypi/%s/json" % ('peopledatalabs',)
        data = json.load(urllib2.urlopen(urllib2.Request(url)))
        versions = list(data["releases"].keys())

        if self.debug:
            print(str(versions)+lineno())

        latest_version = self.get_latest_version_from_list(versions)

        if self.debug:
            print('latest version: '+str(latest_version)+lineno())

        if latest_version != version.strip():
            if self.debug:
                print('Need to install new version of pdl'+lineno())
                print('Latest version: '+str(latest_version)+lineno())
                print('Current version: '+str(version)+lineno())
            self.upgrade_pdl()
            print('###############################################################')
            print('###############################################################')
            print('### Just updated to the most current version - please restart')
            print('###############################################################')
            print('###############################################################')
            sys.exit(1)
        else:
            if self.debug:
                print('Version is up-to-date'+lineno())


    def upgrade_pdl(self):
        """
        Upgrade pdl to most current version
        :return:
        """

        if self.debug:
            print('upgrading pdl'+lineno())

        wd = os.getcwd()
        home = str(Path.home())
        os.chdir(home)
        reqs = subprocess.check_output([sys.executable, '-m', 'pip', 'install', 'peopledatalabs','--upgrade'])
        os.chdir(wd)

        if self.debug:
            print(str(reqs.decode("utf-8"))+lineno())


    def check_if_config_directory_exists(self):
        """
        Check if config directory exists in home directory
        :return:
        """
        # Windows WindowsPath('C:/Users/XXX')

        if self.debug:
            print('check if config directory exists'+lineno())

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
        """
        Check if config file exists
        :return:
        """
        # Windows WindowsPath('C:/Users/XXX')

        if self.debug:
            print('check if config file exists'+lineno())

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
        """
        Get api key from config file
        :return:
        """
        if self.debug:
            print('get api key'+lineno())

        home = str(Path.home())

        if sys.platform == 'win32':
            file = open(home+'/.pdl/config','r', encoding='cp1252')
            content = file.readlines()
        else:
            file = open(home+'/.pdl/config')
            content = file.readlines()


        for line in content:
            if self.debug:
                print('line: '+str(line)+lineno())

            if 'api_key' in line:
                (key_name, key_value) = line.split('=')
                if self.debug:
                    print('name: '+str(key_name)+lineno())
                    print('value: '+str(key_value)+lineno())

                return key_value.strip()



    def yes_or_no(self, question):
        """
        Prompt user for yes/no questions
        :param question:
        :return:
        """

        answer = input(question + "(y/n): ").lower().strip()
        print("")
        while not (answer == "y" or answer == "yes" or \
                   answer == "n" or answer == "no"):
            print("Input yes or no")
            answer = input(question + "(y/n):").lower().strip()
            print("")
        if answer[0] == "y":
            return True
        else:
            return False


    def print_menu(self):  ## Your menu design here
        """
        Print user menu
        :return:
        """
        print(30 * "-", "MENU", 30 * "-")
        print("1. Phone number with 1(example: 1515986xxxx)")
        print("2. Email")
        print("3. Name,Address,City,State,Zip")
        print("4. Name, City, State")
        print("5. Name, State")
        print("6. Exit")
        print(67 * "-")


    def pretty_json(self, input, full_output=False):
        """
        Output in json format
        :param input:
        :param full_output:
        :return:
        """


        if self.debug:
            print(json.dumps(input, indent=2))

        if not full_output and 'likelihood' in input:
            data = {}
            data['full_name'] = input['data']['full_name']
            data['first_name'] = input['data']['first_name']
            data['middle_initial'] = input['data']['middle_initial']
            data['middle_name'] = input['data']['middle_name']
            data['last_name'] = input['data']['last_name']
            data['gender'] = input['data']['gender']


            data["location_name"] = input['data']['location_name']
            data["location_locality"] = input['data']['location_locality']
            data["location_region"] = input['data']['location_region']
            data["location_country"] = input['data']['location_country']

            data["location_street_address"] = input['data']['location_street_address']
            data["location_address_line_2"] = input['data']['location_address_line_2']

            data["location_postal_code"] = input['data']['location_postal_code']
            data["location_last_updated"] = input['data']['location_last_updated']


            data['birth_year'] = input['data']['birth_year']
            data['birth_date'] = input['data']['birth_date']
            data['facebook_url'] = input['data']['facebook_url']
            data['linkedin_url'] = input['data']['linkedin_url']
            data['work_email'] = input['data']['work_email']
            data['personal_emails'] = input['data']['personal_emails']
            data['emails'] = input['data']['emails']
            data['mobile_phone'] = input['data']['mobile_phone']
            data['phone_numbers'] = input['data']['phone_numbers']

            json_formatted_str = json.dumps(data, indent=2)
            print(json_formatted_str)
        else:
            json_formatted_str = json.dumps(input, indent=2)
            print(json_formatted_str)
