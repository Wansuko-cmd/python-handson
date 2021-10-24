# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import requests


url = 'https://ktor-chat-app.herokuapp.com/chat'


def get_messages():
    response = requests.get(url)
    print(response.status_code)
    print(response.text)


def create_messages(user_name: str, text: str):
    response = requests.post(url, json={'user_name': user_name, 'text': text})
    print(response.status_code)
    print(response.text)


def update_message(message_id: str, user_name: str, text: str):
    response = requests.put(url, json={'id': message_id, 'user_name': user_name, 'text': text})
    print(response.status_code)
    print(response.text)


def delete_message(message_id: str):
    response = requests.delete(f'{url}/{message_id}')
    print(response.status_code)
    print(response.text)


# Press the green button in the gutter to run the script.
# def main():
if __name__ == '__main__':

    while True:
        command = input('command: ')

        if command == 'get':
            get_messages()

        elif command == 'create':
            user_name = input('user_name: ')
            text = input('text: ')
            create_messages(user_name, text)

        elif command == 'update':
            message_id = input('id: ')
            user_name = input('user_name: ')
            text = input('text: ')
            update_message(message_id, user_name, text)

        elif command == 'delete':
            message_id = input('id: ')
            delete_message(message_id)

        elif command == 'exit':
            break

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
