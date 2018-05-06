import utility

def main():
    SESSION_ID = open('session.txt').read()
    for i in range(100):
        username = "team%03d" % i
        utility.do(utility.addUser, SESSION_ID, username, username)

if __name__ == '__main__':
    main()