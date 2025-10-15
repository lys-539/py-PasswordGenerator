import hashlib
import json
import os
import pyperclip as pclip



def _generate_password(base: str, tail: str) -> str:
    s_ = hashlib.sha256(base.encode('utf-8')).hexdigest() + hashlib.sha512(tail.encode('utf-8')).hexdigest()
    s_ = hashlib.md5(s_.encode('utf-8')).hexdigest()
    s_ = s_[:6] + 'L!' + s_[-6:]
    return s_


def _update_history(history: dict) -> None:
    with open('history.json', 'w') as file:
        json.dump(history, file, indent=4)


def main() -> None:
    os.system('color')

    if not os.path.exists('config.json'):
        base_ = input('Enter base string for password generation: ')
        with open('config.json', 'w') as file:
            json.dump({'base': base_}, file)

    with open('config.json', 'r') as file:
        try:
            config = json.load(file)
        except:
            config = {}

    if not os.path.exists('history.json'):
        with open('history.json', 'w') as file:
            json.dump({}, file)
    
    with open('history.json', 'r') as file:
        try:
            history_ = json.load(file)
        except:
            history_ = {}
    
    try:
        while True:
            tail_ = input('\nEnter unique string for password generation (e.g. <Website Name>): ')
            print('')
            if tail_ in history_:
                print('\033[33mAlready Generated Password:\033[36m', history_[tail_], '\033[0m Auto-copied to clipboard!')
            else:
                history_[tail_] = _generate_password(config['base'], tail_)
                _update_history(history_)
                print('\033[32mGenerated Password:\033[36m', history_[tail_], '\033[0m Auto-copied to clipboard!')
            pclip.copy(history_[tail_])
    except KeyboardInterrupt:
        print('\nExiting...')
        exit(0)

if __name__ == '__main__':
    main()