import vk
import getpass


APP_ID = 6323784


def get_user_login():
    return input('Enter phone or email: ')


def get_user_password():
    return getpass.getpass('Enter password: ')


def get_online_friends(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
        scope='friends',
    )
    api = vk.API(session)

    return api.users.get(user_ids=api.friends.getOnline())


def output_friends_to_console(friends_online):
    for friend in friends_online:
        print(friend['first_name'], friend['last_name'])


if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    friends_online = get_online_friends(login, password)
    output_friends_to_console(friends_online)
