import random

"""
Group No : App13-Group-180
Student Name : Rohith Ravindran, Keerthi Basvaraju
Created Date : 04 - 05 - 2023
Last Modified Date : 08 - 05 - 2023
"""


class Unit:
    # Constructor to declare initial state  of Unit Class
    def __init__(
        self,
        init_unit_id=0000000,
        init_unit_code="",
        init_unit_name="",
        init_unit_capacity=0,
    ):
        """

        :param init_unit_id: unit id generated
        :param init_unit_code: unit code unique subject code
        :param init_unit_name: unit name
        :param init_unit_capacity: maximum enrolment
        """
        self.unit_id = init_unit_id
        self.unit_code = init_unit_code
        self.unit_name = init_unit_name
        self.unit_capacity = init_unit_capacity

    def __str__(self):
        return "{}, {}, {}, {}".format(
            self.unit_id, self.unit_code, self.unit_name, self.unit_capacity
        )

    def generate_id(self):
        """

        :return: int
        """
        return random.randint(1111111, 9999999)

    def check_unit_id_uniqness(self, new_unit_id):
        """

        :param new_unit_id: generated Int
        :return: boolean
        """
        with open("data/unit.txt", "r") as uni:
            unit_details = uni.readlines()
            for each_unit in unit_details:
                check_list = each_unit.split(", ")
                if check_list[0] == new_unit_id:
                    return True

            return False

    def check_unit_exist(self, new_unit_name):
        """

        :param new_unit_name:
        :return: boolean (True if exists else False)
        """
        with open("data/unit.txt", "r") as cue:
            unit_details = cue.readlines()
            for each_unit in unit_details:
                check_list = each_unit.split(", ")
                # print(check_list[2])
                if check_list[2] == new_unit_name:
                    return True
            return False

    def check_unit_code(self, new_unit_code):
        """

        :param new_unit_code:
        :return: boolean True if exists else False
        """
        with open("data/unit.txt", "r") as cue:
            unit_details = cue.readlines()
            for each_unit in unit_details:
                check_list = each_unit.split(", ")
                # print(check_list[2])
                if check_list[1] == new_unit_code:
                    return True
            return False
