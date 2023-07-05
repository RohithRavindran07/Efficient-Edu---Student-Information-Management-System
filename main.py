"""
Group No : App13-Group-180
Student Name : Rohith Ravindran, Keerthi Basvaraju
Created Date : 04 - 05 - 2023
Last Modified Date : 08 - 05 - 2023
"""
import random
import unit
from user import User
from unit import Unit
from user_admin import UserAdmin
from user_teacher import UserTeacher
from user_student import UserStudent


##The Function Which welcomes user
def main_menu():
    """
    main menu for welcome screen
    """
    print(
        "\n_________________________________\n!!![STUDENT MANAGEMENT SYSTEM]!!!\n_________________________________\n"
    )
    print(
        '_________________________________"\n[1] "LOGIN" \n[X] "EXIT" \n_________________________________\n'
    )


def generate_test_data():
    """
    generate Test Data Where 1 admin 3 teachers and 10 student data is populated
    """
    unit1 = Unit(1111111, "FIT1111", "System Analysis", 500)
    unit2 = Unit(2222222, "FIT2222", "Python", 500)
    unit3 = Unit(3333333, "FIT3333", "Java", 500)
    unit_str = str(unit1) + "\n" + str(unit2) + "\n" + str(unit3) + "\n"
    with open("data/unit.txt", "w") as file:
        file.write(unit_str)

    # generate one admin user
    admin_user = UserAdmin(11111, "admin", "^^^Y!J#2$2%6&X(1)M*$$$", "AD", "enabled")
    admin_usr = str(admin_user) + "\n"

    with open("data/user.txt", "w") as file:
        file.write(admin_usr)

    # three teachers:
    teacher1 = UserTeacher(
        22222, "ta0", "^^^Y!J#2$2%6&X(1)M*$$$", "TA", "enabled", ["FIT1111"]
    )
    teacher2 = UserTeacher(
        33333, "ta1", "^^^Y!J#2$2%6&X(1)M*$$$", "TA", "enabled", ["FIT2222"]
    )
    teacher3 = UserTeacher(
        44444, "ta2", "^^^Y!J#2$2%6&X(1)M*$$$", "TA", "enabled", ["FIT3333"]
    )
    teacher1.save_user()
    teacher2.save_user()
    teacher3.save_user()

    # 10 Students
    # ten students
    student_1 = UserStudent(
        36252,
        "st0",
        "^^^Y!J#2$2%6&X(1)M*$$$",
        "ST",
        "enabled",
        [("FIT1111", -1), ("FIT2222", -1), ("FIT3333", -1)],
    )
    student_2 = UserStudent(
        21220,
        "st1",
        "^^^Y!J#2$2%6&X(1)M*$$$",
        "ST",
        "enabled",
        [("FIT1111", -1), ("FIT2222", -1), ("FIT3333", -1)],
    )
    student_3 = UserStudent(
        21221,
        "st2",
        "^^^Y!J#2$2%6&X(1)M*$$$",
        "ST",
        "enabled",
        [("FIT1111", -1), ("FIT2222", -1)],
    )
    student_4 = UserStudent(
        21222,
        "st3",
        "^^^Y!J#2$2%6&X(1)M*$$$",
        "ST",
        "enabled",
        [("FIT1111", -1), ("FIT2222", -1), ("FIT3333", -1)],
    )
    student_5 = UserStudent(
        21223, "st4", "^^^Y!J#2$2%6&X(1)M*$$$", "ST", "enabled", [("FIT1111", -1)]
    )
    student_6 = UserStudent(
        21224,
        "st5",
        "^^^Y!J#2$2%6&X(1)M*$$$",
        "ST",
        "enabled",
        [("FIT1111", -1), ("FIT2222", -1), ("FIT3333", -1)],
    )
    student_7 = UserStudent(
        21225,
        "st6",
        "^^^Y!J#2$2%6&X(1)M*$$$",
        "ST",
        "enabled",
        [("FIT1111", -1), ("FIT2222", -1)],
    )
    student_8 = UserStudent(
        21226,
        "st7",
        "^^^Y!J#2$2%6&X(1)M*$$$",
        "ST",
        "enabled",
        [("FIT1111", -1), ("FIT2222", -1), ("FIT3333", -1)],
    )
    student_9 = UserStudent(
        21227,
        "st8",
        "^^^Y!J#2$2%6&X(1)M*$$$",
        "ST",
        "enabled",
        [("FIT1111", -1), ("FIT2222", -1), ("FIT3333", -1)],
    )
    student_10 = UserStudent(
        21228,
        "st9",
        "^^^Y!J#2$2%6&X(1)M*$$$",
        "ST",
        "enabled",
        [("FIT1111", -1), ("FIT2222", -1), ("FIT3333", -1)],
    )

    student_1.save_user()
    student_2.save_user()
    student_3.save_user()
    student_4.save_user()
    student_5.save_user()
    student_6.save_user()
    student_7.save_user()
    student_8.save_user()
    student_9.save_user()
    student_10.save_user()


def read_file_list(file_name):
    """

    :param file_name: String
    :return: file read as list
    """
    with open(file_name) as fl:
        return fl.readlines()


def write_file(file_name, mode, data):
    """
    Function to Write File
    :param file_name: String
    :param mode: Mode of file to be opened
    :param data: file data to be written
    """
    with open(file_name, mode) as fl:
        fl.write(", ".join(data))


# def generate_user_enrolled(enrolled_units):
#     unit_enrolled_list = []
#     enroled_tpl_list = enrolled_units
#     for idx, tpl in enumerate(enroled_tpl_list):
#         unit_enrolled_list.append(tpl[0])
#     return unit_enrolled_list


def validate_login(usr_name, passwd):
    """
    To validate Login Credential Strings
    :param usr_name: username
    :param passwd: password
    :return: boolean
    """
    if usr_name is None:
        print("User name cannot be empty: Please check")
        return False
    if passwd is None:
        print("Password cannot be empty: Please check")
        return False

    user = User()
    user.user_name = usr_name
    user.user_password = user.encrypt(passwd)
    flag = user.login(user.user_name, user.user_password)
    if flag is None:
        print("Bad credentials")
        return False
    if flag.split(", ")[4] == user.disabled:
        return False
    else:
        return flag


def create_creds(usr_str):
    #print("ussr_str", usr_str)
    creds = dict()
    usr_details = usr_str.strip().split(", ")
    # print(usr_details)
    creds["user_id"] = usr_details[0]
    creds["user_name"] = usr_details[1]
    creds["user_password"] = usr_details[2]
    creds["user_role"] = usr_details[3]
    creds["user_status"] = usr_details[4]
    if usr_details[3] == "TA":
        try:
            creds["teach_units"] = eval(usr_details[5])
            print(creds["teach_units"])
        except:
            pass
    if usr_details[3] == "ST":
        try:
            creds["enrolled_units"] = eval(usr_details[5])
            print(creds["enrolled_units"])
        except:
            pass
    print("creds", creds)
    return creds


# ADMIN FUNCTIONALITY FUNCTION WHICH HAS ALL FUNCTIONALITIES OF USER ADMIN:


def basic_checks(basic_str):
    """

    :param basic_str: String
    :return: Boolean
    To check whether the string is none or not
    """
    if basic_str is None:
        return True
    else:
        return False


def admin_functionalities(creds):
    """
    ADMIN FUNCTIONALITY
    1. Search User
    2.List All users
    3.List All Units
    4.Enable Disable Users
    5.Adding Users
    6.Delete Users
    7.Log Out
    :param creds:
    """
    admin_obj = UserAdmin(**creds)
    user_obj = User()
    while True:
        admin_obj.admin_menu()
        admin_choice = input("\nENTER YOUR CHOICE : ")
        if basic_checks(admin_choice) is not True:
            if admin_choice == "1":
                print("\n Search User Selected")
                user_name = input("\nPlease Enter user to search: ")
                if basic_checks(
                    user_name
                ) is not True and user_obj.check_username_exist(user_name):
                    admin_obj.search_user(user_name)
                    continue
                else:
                    print("Invalid User Name")
                    continue

            elif admin_choice == "2":
                print("\n Listing all users selected")
                admin_obj.list_all_users()
                continue

            elif admin_choice == "3":
                print("\n Listing all Units selected")
                admin_obj.list_all_units()
                continue

            elif admin_choice == "4":
                user_name = input("\nPlease Enter the user name: ")
                if basic_checks(
                    user_name
                ) is not True and user_obj.check_username_exist(user_name):
                    admin_obj.enable_disable_user(user_name)
                    continue
                else:
                    print("Invalid UserName")
                    continue

            elif admin_choice == "5":
                user_id = user_obj.generate_user_id()
                if user_obj.check_user_id_uniqness(user_id) is not True:
                    print("User Id :", user_id)
                    pass
                else:
                    print("\nUser Id already exists Try Again")
                    continue

                user_name = input("\nEnter user name : ")
                if user_obj.check_username_exist(user_name) is not True:
                    print("\n User Name:", user_name)
                    pass
                else:
                    print("\n User name already exists")
                    continue

                user_password = input("\nEnter Password: ")
                encrypted_password = user_obj.encrypt(user_password)

                user_status = input("\nenter the user status: ")
                if user_status not in ["enabled", "disabled"]:
                    print("Invalid Status")
                    continue
                else:
                    pass

                user_role = input("\n Enter user role: ")
                if user_role not in ["TA", "AD", "ST"]:
                    print("Invalid Role")
                    continue
                else:
                    pass

                user_obj.user_id = user_id
                user_obj.user_name = user_name
                user_obj.user_password = encrypted_password
                user_obj.user_status = user_status
                user_obj.user_role = user_role
                admin_obj.add_user(user_obj)
                continue

            elif admin_choice == "6":
                user_name = input("\nEnter username to be deleted: ")
                if user_obj.check_username_exist(user_name):
                    admin_obj.delete_user(user_name)
                else:
                    print("\ncannot be deleted user does not exist")

            elif admin_choice == "7":
                print("\nSuccessfully Logged Out")
                break
            else:
                print("\n Invalid Input")
                continue


def teacher_functionality(creds):
    """
    Teacher Functionality Function
    1.List Teaching Units
    2.Add Teaching Units
    3.Delete Teaching Units
    4.List enroll students
    5.show avg max min scores
    7.Log Out
    :param creds:
    """
    teacher_obj = UserTeacher(**creds)
    # print(teacher_obj.__dict__)
    teacher_obj.teacher_menu()
    unit_obj = Unit()
    while True:
        teacher_obj.teacher_menu()
        teacher_choice = input("Please Enter Your Choice: ")
        if basic_checks(teacher_choice) is not True:
            if teacher_choice == "1":
                print("\nListing all Teaching Units....")
                teacher_obj.list_teach_units()
                continue

            elif teacher_choice == "2":
                print("\n Adding teach Units")
                unit_id = unit_obj.generate_id()
                if unit_obj.check_unit_id_uniqness(unit_id):
                    print("\nUnit id already exists")
                    continue
                else:
                    print("Unit Id", unit_id)
                    pass

                unit_code = input("Enter unit Code: ")
                if basic_checks(unit_code):
                    print("\n Invalid Input or Unit ")
                    continue
                else:
                    print("unit code: ", unit_code)
                    pass

                unit_name = input("Enter Unit Name: ")
                if basic_checks(unit_name) or unit_obj.check_unit_exist(unit_name):
                    print("\n Invalid Input or Unit name already exists")
                    continue
                else:
                    print("unit name: ", unit_name)
                    pass
                try:
                    unit_capacity = int(input("Enter unit Capacity: "))
                except:
                    print("Invalid Input")
                    continue
                unit_obj.unit_id = unit_id
                unit_obj.unit_code = unit_code
                unit_obj.unit_name = unit_name
                unit_obj.unit_capacity = unit_capacity
                teacher_obj.add_teach_unit(unit_obj)

            elif teacher_choice == "3":
                curr_list = teacher_obj.teach_units
                print(curr_list)
                unit_code = input("\nPlease Enter the unit to be deleted: ").upper()
                if basic_checks(unit_code) is True or unit_code not in curr_list:
                    print("\n Invalid Input or Unit name doesn not exists")
                    continue
                else:
                    teacher_obj.delete_teach_unit(unit_code)
                    print("\n Deleted Successfully")

            elif teacher_choice == "4":
                unit_code = input("\n Please Enter The unit Code: ")
                if basic_checks(unit_code) is not True:
                    teacher_obj.list_enrol_students(unit_code)
                    continue
                else:
                    print("\n Please Re-Enter the Unit Code")
                    continue

            elif teacher_choice == "5":
                unit_code = input("\n Please Enter the unit code ")
                if basic_checks(unit_code) is not True:
                    teacher_obj.show_unit_avg_max_min_score(unit_code)
                    continue
                else:
                    print("Please Re-Enter the Unit Code ")
                    continue
            elif teacher_choice == "7":
                print("\nLogged out")
                break

            else:
                print("Invalid Choice")
                continue
        else:
            print("Invalid Input")
            continue


def student_functionalities(creds):
    """
    1.List Available Units
    2.List Enrolled Units
    3.enroll units
    4.delete units
    5.check score
    6. generate Score
    7. log out
    :param creds:
    """
    stud_obj = UserStudent(**creds)
    stud_obj.student_menu()
    unit_obj = Unit()
    while True:
        stud_obj.student_menu()
        student_choice = input("\n Enter the choice of the student: ")
        if student_choice == "1":
            stud_obj.list_available_units()
        elif student_choice == "2":
            stud_obj.list_enrolled_units()
            pass
        elif student_choice == "3":
            unit_code = input("\nEnter the unit code: ").upper()
            if basic_checks(unit_code) is not True:
                enroled_list = stud_obj.enrolled_units
                if (
                    len(enroled_list) < 3
                    and unit_obj.check_unit_code(unit_code)
                    and unit_code not in [unit[0] for unit in enroled_list]
                ):
                    stud_obj.enrol_unit(unit_code)
                else:
                    print("Cannot be enrolled")
            else:
                print("Invalid unit code")
                continue

        elif student_choice == "4":
            unit_code = input("\nEnter the unit code: ").upper()

            if basic_checks(unit_code) is not True:
                enroled_list = stud_obj.enrolled_units
                if unit_code in [unit[0] for unit in enroled_list]:
                    stud_obj.drop_unit(unit_code)
                else:
                    print("\n Cannot be deleted")
            else:
                print("\n Invalid Input")
                continue

        elif student_choice == "5":
            unit_code = input("\nEnter the unit code: ").upper()
            if basic_checks(unit_code) is not True:
                enroled_list = stud_obj.enrolled_units
                if unit_code in [unit[0] for unit in enroled_list]:
                    stud_obj.check_score(unit_code)
                else:
                    print("Scores Not Available")
                    continue

        elif student_choice == "6":
            unit_code = input("\nEnter the unit code: ").upper()
            if basic_checks(unit_code) is not True:
                enroled_list = stud_obj.enrolled_units
                if unit_code in [unit[0] for unit in enroled_list]:
                    stud_obj.generate_score(unit_code)
                else:
                    print("Scores Not generated check if you have enrolled in it")
                    continue

        elif student_choice == "7":
            print("\n Successfully Logged Out")
            break
        else:
            print("\n Invalid Input Given Please Recheck your input")
            continue


def main():
    """
    the main function where all the functionality is called and input is obtained it runs till user wishes to exit
    """
    generate_test_data()
    while True:
        # welcome screen
        main_menu()
        input_choice = input("ENTER THE CHOICE: ")
        if input_choice == "1":
            usr_name = input("ENTER YOUR USERNAME: ")
            passwd = input("ENTER YOUR PASSWORD: ")
            validator = validate_login(usr_name, passwd)
            if validator:
                creds = create_creds(validator)
                input_role = validator.split(", ")[3]
                if input_role == "AD":
                    admin_functionalities(creds)
                    continue
                elif input_role == "TA":
                    teacher_functionality(creds)
                    continue
                elif input_role == "ST":
                    student_functionalities(creds)
                    continue
            else:
                print("\nEnter Valid User Name and Password")
                continue
        if input_choice.lower() == "x":
            break
        else:
            print("\n Invalid Input")
            continue


if __name__ == "__main__":
    main()
