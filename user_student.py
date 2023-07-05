from user import User
import re
import random

"""
Group No : App13-Group-180
Student Name : Rohith Ravindran, Keerthi Basvaraju
Created Date : 04 - 05 - 2023
Last Modified Date : 08 - 05 - 2023
"""


def read_file_list(file_name):
    """

    :param file_name:
    :return: readfile
    """
    with open(file_name) as fl:
        return fl.readlines()


def write_file(file_name, mode, data):
    """

    :param file_name:
    :param mode: file mode
    :param data: location
    writing file
    """
    with open(file_name, mode) as fl:
        for line in data:
            fl.write(f"{line.strip()}\n")


class UserStudent(User):
    def __init__(
        self,
        user_id=100,
        user_name="default_user_001",
        user_password="default_password_001",
        user_role="ST",
        user_status="disabled",
        enrolled_units=[("FIT3333", -1)],
    ):
        super().__init__(user_id, user_name, user_password, user_role, user_status)
        self.enrolled_units = enrolled_units

    def __str__(self):
        enrolled_list = re.sub(r"\s+", "", str(self.enrolled_units))
        # print(enrolled_list)
        return f"{super().__str__()}, {enrolled_list}"

    def student_menu(self):
        """
        Display Student menu
        """
        print(
            "_________________________________\nPLEASE SELECT THE DESIRED OPERATION:\n_________________________________"
        )
        print("[1]. List Available Units")
        print("[2]. List Enrolled Units")
        print("[3]. Enroll a unit")
        print("[4]. Drop Unit")
        print("[5]. Check Scores")
        print("[6]. Generate Score")
        print("[7]. Log out")
        print("_________________________________\n")

    def list_available_units(self):
        """
        Display all thr available units
        """
        units = read_file_list(self.unit_file)
        print("Available Units are:")
        for unit in units:
            unit_details = unit.split(", ")
            if int(unit_details[3]) > 0:
                print(
                    f"Unit Code: {unit_details[1]}, Unit Name: {unit_details[2]}, Remaining Capacity; {unit_details[3]}"
                )
            else:
                continue

    def list_enrolled_units(self):
        """
        Display all the enrolled units
        """
        print("Your current enrolled units are:")
        units_list = self.enrolled_units
        unit_enrolled_list = list()
        if len(units_list) > 0:
            for idx, tpl in enumerate(units_list):
                unit_enrolled_list.append(tpl[0])
            units = read_file_list(self.unit_file)
            for unit in units:
                unit_details = unit.strip().split(", ")
                if unit_details[1] in unit_enrolled_list:
                    print(
                        f"Unit Code: {unit_details[1]}, Unit Name: {unit_details[2]}, \
                      Remaining Capacity; {unit_details[3]}"
                    )
        else:
            print("\nNo Units available")

    def enrol_unit(self, unit_code):
        """

        :param unit_code: String
        enroll a particular unit
        """
        curr_enroll = self.enrolled_units
        curr_enroll.append((unit_code, "-1"))
        self.enrolled_units = curr_enroll
        enrolled_list = re.sub(r"\s+", "", str(self.enrolled_units))
        users = read_file_list(self.user_file)
        for i, user in enumerate(users):
            user_splits = user.strip().split(", ")
            if user_splits[1] == self.user_name:
                lfind = user.find("[")
                user_broke = user[0:lfind].strip()
                user_updated = f"{user_broke} {enrolled_list}"
                print(user_updated)
                users[i] = user_updated
            else:
                continue
        write_file(self.user_file, "w", users)
        print("\nUnit Enrolled")

    def drop_unit(self, unit_code):
        """

        :param unit_code: String
        drops a enrolled unit
        """
        curr_enroll = self.enrolled_units
        for i, unit in enumerate(curr_enroll):
            if unit[0] == unit_code:
                curr_enroll.remove(unit)
        self.enrolled_units = curr_enroll
        enrolled_list = re.sub(r"\s+", "", str(self.enrolled_units))
        users = read_file_list(self.user_file)
        for i, user in enumerate(users):
            user_splits = user.strip().split(", ")
            if user_splits[1] == self.user_name:
                lfind = user.find("[")
                user_broke = user[0:lfind].strip()
                user_updated = f"{user_broke} {enrolled_list}"
                print(user_updated)
                users[i] = user_updated
            else:
                continue
        write_file(self.user_file, "w", users)
        print("\nSuccessfully deleted")

    def check_score(self, unit_code):
        """

        :param unit_code: String
        Checking Score of a particular subject
        """
        units_list = self.enrolled_units
        unit_enrolled_dict = dict(units_list)
        for key, val in unit_enrolled_dict.items():
            if str(val) == "-1":
                unit_enrolled_dict[key] = 0

        if unit_code == "all":
            print("Displaying scores of all three units")
            for key, val in unit_enrolled_dict.items():
                print(f"Score of {key}:{val}")
        else:
            print(f"Displaying scores of {unit_code}")
            for key, val in unit_enrolled_dict.items():
                if key == unit_code:
                    print(f"Score of {key}:{val}")

    def generate_score(self, unit_code):
        """

        :param unit_code: String
        Generates marks for a subject
        """
        score = random.randint(0, 100)
        print(f"Your Score: {score}")
        curr_enroll = self.enrolled_units
        for i, unit in enumerate(curr_enroll):
            if unit[0] == unit_code:
                tuple = (unit[0], score)
                curr_enroll[i] = tuple
        self.enrolled_units = curr_enroll
        enrolled_list = re.sub(r"\s+", "", str(self.enrolled_units))
        users = read_file_list(self.user_file)
        for i, user in enumerate(users):
            user_splits = user.strip().split(", ")
            if user_splits[1] == self.user_name:
                lfind = user.find("[")
                user_broke = user[0:lfind].strip()
                user_updated = f"{user_broke} {enrolled_list}"
                print(user_updated)
                users[i] = user_updated
            else:
                continue
        write_file(self.user_file, "w", users)
