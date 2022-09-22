#get started
class System:

    def __int__(self, database, username, password, password1):

        pass

    @staticmethod
    def register():
        database = open('database.txt', 'r')
        username = input('create a username: ')
        password = input('create password: ')
        password1 = input('confirm password: ')

        d = []
        f = []

        for i in database:
            a, b = i.split(', ')

            b = b.strip()
            d.append(a)
            f.append(b)
        data = dict(zip(d, f))
        # print(data)

        if password != password1:
            print('password do not match, restart')
            c = System()
            c.register()

        else:
            if len(password) <= 6:
                print('password too short, restart')
                c = System()
                c.register()

            elif username in d:
                print('username exist')
                c = System()
                c.register()

            else:

                database = open('database.txt', 'a')
                database.write(username+', '+password+'\n')
                print('success')

    @staticmethod
    def access():
        database = open('database.txt', 'r')
        username = input('Enter username: ')
        password = input('Enter  password: ')

        if not len(username or password) < 1:
            d = []
            f = []

            for i in database:
                a, b = i.split(', ')

                b = b.strip()
                d.append(a)
                f.append(b)
            data = dict(zip(d, f))
            # print(data)

            try:

                if data[username]:

                    try:
                        if password == data[username]:

                            print('Login success')
                            print(f'HI, {username}')
                        else:
                            print('password or username incorrect')
                    except:
                        print('incorrect password')
                else:
                    print('username does not exit')
            except:

                print('details not found')

        else:
            print('enter a value')

    @staticmethod
    def home():
        option = input('login / Sign up: ')

        if option == 'Login':
            a = System()
            a.access()
        elif option == 'Sign up':
                c = System()
                c.register()
        else:
            print('enter right option')


h = System()
h.home()


