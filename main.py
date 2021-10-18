# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import requests


def get_messages():
    response = requests.get('https://ktor-chat-app.herokuapp.com/chat')
    print(response.status_code)
    print(response.text)


def create_messages(user_names, texts):
    response = requests.post('https://ktor-chat-app.herokuapp.com/chat', json={'user_name': user_names, 'text': texts})
    print(response.status_code)
    print(response.text)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    while True:
        command = input('command: ')

        if command == 'get':
            get_messages()

        elif command == 'create':
            user_name = input('user_name: ')
            text = input('text: ')
            create_messages(user_name, text)

        elif command == 'exit':
            break

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
