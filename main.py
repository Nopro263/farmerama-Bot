import farmerama
import random

user = input("All users should start with ... (blank for random): ")
user_len = int(input("Length of the Usernames: "))
email = input("Email (blank for random): ")
password_len = int(input("Length of Password: "))
newsletter = input("Newsletter? (y/n)").lower() == "y"

amount = int(input("How many bots:"))

with open("acc.txt", "a") as f:
    for i in range(amount):
        _user = farmerama.randomUsername(user_len, user)
        _password = farmerama.randomPassword(password_len)
        if email:
            _email = email
        else:
            _email = f"{farmerama.randomUsername(random.randint(3, 10))}@" \
                     f"{farmerama.randomUsername(random.randint(5, 15))}." \
                     f"{farmerama.randomUsername(random.randint(2, 4))}"

        try:
            farmerama.create_account(_user, _password, _email, newsletter)
        except Exception as e:
            print(f"ERROR: {e}")
        else:
            f.write(f"{_user} {_password}\n")
            print(f"User {i + 1} done")
