from GodaddyProject.UsernamePassword.Users import Users


class Credentials():
    with open(Users.path, 'r') as file:
        credentials = file.readlines()
        username = credentials[0]
        password = credentials[1]
