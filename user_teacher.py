from unit import Unit
from user import User
import re
from user_student import UserStudent

"""
Group No : App13-Group-180
Student Name : Rohith Ravindran, Keerthi Basvaraju
Created Date : 04 - 05 - 2023
Last Modified Date : 08 - 05 - 2023
"""


def read_file_list(file_name):
    """

    :param file_name: file buffer
    :return:  return files read in list as lines
    """
    with open(file_name) as fl:
        return fl.readlines()


def write_file(file_name, mode, data):
    """

    :param file_name: location
    :param mode: write mode
    :param data: to write
    """
    with open(file_name, mode) as fl:
        for line in data:
            print(line)
            fl.write(f"{line.strip()}\n")


def update_data(data, user_name, enrolled_list):
    """
    used to update enrolled list
    :param data:
    :param user_name:
    :param enrolled_list: list of tuples
    :return: no retuen
    """
    users = data
    for i, user in enumerate(users):
        user_splits = user.strip().split(", ")
        if user_splits[1] == user_name:
            lfind = user.find("[")
            user_broke = user[0:lfind].strip()
            user_updated = f"{user_broke} {enrolled_list}"
            print(user_updated)
            users[i] = user_updated
        else:
            continue
    return users


class UserTeacher(User):
    def __init__(
        self,
        user_id=00000,
        user_name="",
        user_password="",
        user_role="TA",
        user_status="enabled",
        teach_units=[],
    ):
        super().__init__(user_id, user_name, user_password, user_role, user_status)
        self.teach_units = teach_units

    def __str__(self):
        enrolled_list = re.sub(r"\s+", "", str(self.teach_units))
        return f"{super().__str__()}, {enrolled_list}"

    def teacher_menu(self):
        """
        Teacher Menu Display
        """
        print(
            "_________________________________\nPLEASE SELECT THE DESIRED OPERATION:\n_________________________________"
        )
        print("[1]. List all teaching units information")
        print("[2]. Add a unit")
        print("[3]. Delete a unit")
        print("[4]. List all info and scores of enrolled unit")
        print("[5]. Show the avg/max/min score of one unit")
        print("[7]. Log out")
        print("_________________________________\n")

    def list_teach_units(self):
        """
        List Teaching Units
        No return type
        prints teaching unit of a specific teacher
        """
        ltu = []
        units_curr = self.teach_units
        units = read_file_list(self.unit_file)
        for unit in units:
            unit_split = unit.strip().split(", ")
            if unit_split[1] in units_curr:
                ltu.append(
                    "Unit Code: {} Unit Name: {}".format(unit_split[0], unit_split[1])
                )
        if len(ltu) > 0:
            print(ltu)
        else:
            print("\n No Teaching Units Found")

    def add_teach_unit(self, unit_obj):
        """

        :param unit_obj: object of unit class
        used to add teach unit in both user and unit
        """
        update_unit = unit_obj.__str__()
        # print(update_unit)
        units = read_file_list(self.unit_file)
        units.append(update_unit)
        write_file(self.unit_file, "w", units)
        self.teach_units.append(unit_obj.unit_code)
        enrolled_list = re.sub(r"\s+", "", str(self.teach_units))
        users = read_file_list(self.user_file)
        updated_users = update_data(users, self.user_name, enrolled_list)
        write_file(self.user_file, "w", updated_users)

    def delete_teach_unit(self, unit_code):
        """

        :param unit_code: String Unit Code
        used to delete unit
        """
        updated_student = []
        units = read_file_list(self.unit_file)
        for i, unit in enumerate(units):
            print(f"unit: {unit}")
            if unit.split(", ")[1] == unit_code:
                units.remove(unit)
            else:
                continue
        write_file(self.unit_file, "w", units)
        unit_list = self.teach_units
        unit_list.remove(unit_code)
        enrolled_list = re.sub(r"\s+", "", str(self.teach_units))
        users = read_file_list(self.user_file)
        updated_users = update_data(users, self.user_name, enrolled_list)
        write_file(self.user_file, "w", updated_users)
        users = read_file_list(self.user_file)
        # to delete from students
        for i, user in enumerate(users):
            if user.split(", ")[3] == "ST":
                user_list = user.split(", ")[-1]
                #print(user)
                #print(type(user_list), user_list)
                # print(type(user_list[0]),user_list[0])
                if unit_code in user_list:
                    student_details = user.split(", ")
                    stud_temp_obj = UserStudent(
                        student_details[0],
                        student_details[1],
                        student_details[2],
                        student_details[4],
                        student_details[5],
                    )
                    # print(stud_temp_obj.__dict__)
                    stud_temp_obj.drop_unit(unit_code)

    def list_enrol_students(self, unit_code):
        """

        :param unit_code: String
        used to enroll to a specific subject
        """
        final_enrol = []
        users = read_file_list(self.user_file)
        for each_user in users:
            if each_user.split(", ")[3] == "ST":
                enroll_list_str = each_user.split(", ")[-1]
                enroll_list = eval(enroll_list_str)
                for unit_code_in_enroll, value in enroll_list:
                    if unit_code_in_enroll == unit_code:
                        # Retrieve user details or perform desired actions
                        final_enrol.append(
                            (
                                each_user.split(", ")[0],
                                each_user.split(",")[1],
                                unit_code_in_enroll,
                                value,
                            )
                        )
        if len(final_enrol) > 0:
            print("The Details of students enrolled in this unit are : ", final_enrol)
        else:
            print("No Student is found for this Unit")

    def show_unit_avg_max_min_score(self, unit_code):
        """

        :param unit_code: String
        shows mean minimum and max of a unit
        """
        users = read_file_list(self.user_file)
        marks_list = []
        for each_user in users:
            if each_user.split(", ")[3] == "ST":
                enroll_list_str = each_user.split(", ")[-1]
                enroll_list = eval(enroll_list_str)
                for unit_code_in_enroll, value in enroll_list:
                    if unit_code_in_enroll == unit_code:
                        marks_list.append(value)

        if marks_list:
            avg_score = sum(marks_list) / len(marks_list)
            max_score = max(marks_list)
            min_score = min(marks_list)

            print("UNIT:", unit_code)
            print("Average Score:", avg_score)
            print("Maximum Score:", max_score)
            print("Minimum Score:", min_score)
        else:
            print("No users found for the unit:", unit_code)
