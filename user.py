import random

"""
Group No : App13-Group-180
Student Name : Rohith Ravindran, Keerthi Basvaraju
Created Date : 04 - 05 - 2023
Last Modified Date : 08 - 05 - 2023
"""


class User:
    def __init__(
        self,
        init_user_id=0000,
        init_user_name="",
        init_user_paswd="",
        init_user_role="",
        init_user_status="enabled",
    ):
        """

        :param init_user_id: int
        :param init_user_name: string
        :param init_user_paswd: string
        :param init_user_role: string TA ST AD
        :param init_user_status: string enabled/disabled
        """
        self.user_id = init_user_id
        self.user_name = init_user_name
        self.user_password = init_user_paswd
        self.user_role = init_user_role
        self.user_status = init_user_status
        self.user_file = "data/user.txt"
        self.unit_file = "data/unit.txt"
        self.enabled = "enabled"
        self.disabled = "disabled"

    def __str__(self):
        """

        :return: object to string
        """
        return "{}, {}, {}, {}, {}".format(
            self.user_id,
            self.user_name,
            self.user_password,
            self.user_role,
            self.user_status,
        )

    def generate_user_id(self):
        """

        :return: int user id
        """
        generated_user_id = random.randint(11111, 99999)
        return generated_user_id

    """checking if username exists in the file """

    def check_username_exist(self, uname):
        """

        :param uname: username
        :return: Boolean True if exists False if not exists
        """
        with open(self.user_file, "r") as cu:
            user_details = cu.readlines()

            for each_user in user_details:
                check_list = each_user.split(", ")
                if check_list[1] == uname:
                    return True

            return False

    """ENCRYPTING PASSWORD """

    def encrypt(self, user_passwd):
        """

        :param user_passwd: String to encrypt
        :return: encypted password String
        """
        encrypted_password = ""
        str_1 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
        str_2 = "!#$%&()*+-./:;<=>?@\\^_`{|}~"
        for index_of_each_letter, each_letter in enumerate(user_passwd):
            get_ascii = ord(each_letter)
            get_ascii_index = get_ascii % len(str_1)
            get_char_str_1 = str_1[get_ascii_index]
            get_index_str_2 = index_of_each_letter % len(str_2)
            get_char_str_2 = str_2[get_index_str_2]
            encrypted_word = get_char_str_1 + get_char_str_2
            encrypted_password += encrypted_word
        return "^^^" + encrypted_password + "$$$"

    """ lOGING IN USER"""
    # to do return data string

    def login(self, user_name, password):
        """

        :param user_name: String
        :param password: String
        :return: each_user String if true else None
        """
        with open(self.user_file, "r") as log:
            user_details = log.readlines()
            for each_user in user_details:
                # print(each_user)
                check_list = each_user.split(", ")
                # print(check_list)
                if (check_list[1] == user_name) and (check_list[2] == password):
                    return each_user
            else:
                return None

    def save_user(self):
        """
        to  save to a file
        """
        with open(self.user_file, "a+") as fl:
            fl.write(f"{self.__str__()}\n")
            print("Saved Successfully")

    def check_user_id_uniqness(self, new_user_id):
        """
        to chech if user id is unique
        :param new_user_id: String
        :return: boolean
        """
        with open(self.user_file, "r") as cui:
            user_details = cui.readlines()
            for each_user in user_details:
                check_list = each_user.split(", ")
                if check_list[0] == new_user_id:
                    return True

            return False
