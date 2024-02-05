import pandas

user_input = int(input("what you want to do\nenter 1 for login and enter 2 for registration: "))

try:
    registered_user = pandas.read_csv("user_data.csv")
except (FileNotFoundError, pandas.errors.EmptyDataError):
    file_header = pandas.DataFrame(columns=["mail_id", "password"])
    file_header.to_csv("user_data.csv", index=False)
    registered_user = pandas.read_csv("user_data.csv")


# print(registered_user)


def user_detail():
    user_email = input("enter your email: ")
    user_pass = str(input("enter your password: "))
    return user_email, user_pass


if user_input == 1:
    print("enter your login detail ⬇️")
    login_details = user_detail()

    if login_details[0] in registered_user["mail_id"].values:
        mail_index = registered_user[registered_user["mail_id"] == login_details[0]].index[0]
        user_password = registered_user["password"].loc[mail_index]
        # print(user_password, type(user_password))

        if str(user_password) == login_details[1]:
            print(f"Successfully logged in.\nWelcome {login_details[0].split('@')[0].title()}")
        else:
            print("Password is incorrect")
    else:
        print("No record found with this email")

elif user_input == 2:
    print("enter your registration detail ⬇️")
    registration_detail = user_detail()

    if "@" in registration_detail[0]:
        if registration_detail[0] not in registered_user["mail_id"].values:
            new_data = {
                "mail_id": [registration_detail[0].strip()],
                "password": [registration_detail[1].strip()]
            }
            dataframe = pandas.DataFrame(new_data)
            dataframe.to_csv("user_data.csv", mode="a", index=False, header=False, )

            print("successfully registered")
        else:
            print("already registered with this email")
    else:
        print("@ is missing, please provide valid email id.")
else:
    print("incorrect choice")
