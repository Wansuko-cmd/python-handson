# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import requests


def get_messages():
    response = requests.get('https://www.example.com')
    print(response.status_code)
    print(response.text)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    while True:
        command = input()
        if command == 'get':
            get_messages()
        elif command == 'exit':
            break

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
