import pandas

try:
    registered_user = pandas.read_csv("user_data.csv")
except (FileNotFoundError, pandas.errors.EmptyDataError):
    file_header = pandas.DataFrame(columns=["mail_id", "password"])
    file_header.to_csv("user_data.csv", index=False)
    registered_user = pandas.read_csv("user_data.csv")


class UserDetail:
    def __init__(self, email, password):
        self.__user_email = email
        self.__user_pass = str(password)
        self.get_detail()

    def get_detail(self):
        return self.__user_email, self.__user_pass


class LogIn(UserDetail):
    def __init__(self, user_mail, user_pass):
        super().__init__(user_mail, user_pass)
        self.login_details = self.get_detail()
        # print(self.login_details)
        self.__login_verification()

    def __login_verification(self):
        if self.login_details[0] in registered_user["mail_id"].values:
            mail_index = registered_user[registered_user["mail_id"] == self.login_details[0]].index[0]
            user_password = registered_user["password"].loc[mail_index]

            if str(user_password) == self.login_details[1]:
                print(f"Successfully logged in.\nWelcome {self.login_details[0].split('@')[0].title()}")
            else:
                print("Password is incorrect")
        else:
            print("No record found with this email")


class Registration(UserDetail):
    def __init__(self, user_mail, user_pass):
        super().__init__(user_mail, user_pass)
        self.registration_detail = self.get_detail()
        self.__registration_verification()

    def __registration_verification(self):
        if "@" in self.registration_detail[0]:
            if self.registration_detail[0] not in registered_user["mail_id"].values:
                new_data = {
                    "mail_id": [self.registration_detail[0].strip()],
                    "password": [self.registration_detail[1].strip()]
                }
                dataframe = pandas.DataFrame(new_data)
                dataframe.to_csv("user_data.csv", mode="a", index=False, header=False, )

                print("successfully registered")
            else:
                print("already registered with this email")
        else:
            print("@ is missing, please provide valid email id.")
