"""
Group No : App13-Group-180
Student Name : Rohith Ravindran, Keerthi Basvaraju
Created Date : 04 - 05 - 2023
Last Modified Date : 08 - 05 - 2023
"""
from user import User
from user_student import UserStudent
from user_teacher import UserTeacher


class UserAdmin(User):
    def __init__(
        self,
        user_id=0000,
        user_name="",
        user_password="",
        user_role="AD",
        user_status="enabled",
    ):
        """
        Inhertis from User Class
        :param user_id: int default
        :param user_name: string
        :param user_password: string (encrypted)
        :param user_role: role of user here 'AD'
        :param user_status: Enabled/disabled default enabled
        """
        super().__init__(user_id, user_name, user_password, user_role, user_status)

    def __str__(self):
        """

        :return: Object to String conversion
        """
        return super().__str__()

    def admin_menu(self):
        """
        No Return Type Prints Menu
        """
        print(
            "_________________________________\nPLEASE SELECT THE DESIRED OPERATION:\n_________________________________"
        )
        print("[1]. Search user")
        print("[2]. List all users")
        print("[3]. List all units")
        print("[4]. Enable/Disable user")
        print("[5]. Add user")
        print("[6]. Delete user")
        print("[7]. Log out")
        print("_________________________________\n")

    """ Searching the user and printing if found """

    def search_user(self, user_name):
        """

        :param user_name: String user_name
        Search user and prints if found else prompt message
        """
        with open(self.user_file, "r") as file:
            for line in file:
                if user_name == line.split(", ")[1].strip():
                    print("_________________________________")
                    print(line)
                    print("_________________________________")
                    break
            else:
                print("_________________________________")
                print(f"No user found with name {user_name}")
                print("_________________________________")

    def list_all_users(self):
        """
        listing all users
        no return type
        prints all users available
        """
        with open(self.user_file, "r") as file:
            print(
                "____________________________________________________________________________________________________________________________________\n"
            )
            print(file.read())
            print(
                "____________________________________________________________________________________________________________________________________\n"
            )

    def list_all_units(self):
        """
        Listing all the units available
        no return type
        prints units
        """
        with open(self.unit_file, "r") as lu:
            print(
                "____________________________________________________________________________________________________________________________________\n"
            )
            print(lu.read())
            print(
                "____________________________________________________________________________________________________________________________________\n"
            )

    def enable_disable_user(self, user_name):
        """

        :param user_name: String
        enabled if user is disabled disables if enables
        """
        with open(self.user_file, "r") as edu:
            user_info = edu.read().splitlines()
        with open(self.user_file, "w") as edu:
            for each_user in user_info:
                user_details = each_user.strip().split(", ")
                if user_details[1] == user_name:
                    if user_details[4] == "enabled":
                        user_details[4] = "disabled"
                        print("\nUSER SUCCESSFULLY DISABLED")
                    else:
                        user_details[4] = "enabled"
                        print("\n USER SUCCESSFULLY ENABLED")
                edu.write(", ".join(user_details) + "\n")

    def add_user(self, user_obj):
        """

        :param user_obj: class object
        adding user to user.txt
        """
        print("\n Adding User to the file\n")
        new_user = str(user_obj)

        with open(self.user_file, "a") as f:
            f.write(new_user + "\n")

        print(f"user name '{user_obj.user_name} has been added.")

    def delete_user(self, user_name):
        """

        :param user_name: String
        delete a user from user.txt
        """
        with open(self.user_file, "r") as edu:
            user_info = edu.read().splitlines()

        with open(self.user_file, "w") as delete_record:
            for each_user in user_info:
                user_details = each_user.strip().split(", ")
                if user_details[1] == user_name:
                    continue  # skip writing the line for the user to delete
                delete_record.write(", ".join(user_details) + "\n")
                print("\nUser successfully deleted")
