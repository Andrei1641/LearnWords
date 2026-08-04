import os
import subprocess

from lists_manager import ListsManager
from queries.query import Query
from select_text_file_manager import SelectTextFileManager


class ChangeBatchWordsQuery(Query):

    @staticmethod
    def __change_batch_words(batch_name: str):
        change = True
        text_manager = None
        words_set: set[tuple[str, str]] = set()
        try:
            select_t_m = SelectTextFileManager()
            text_manager = select_t_m.select(batch_name)
            words_set = text_manager.create_word_set()
        except FileNotFoundError as e:
            print(e)
            change = False
        except ValueError:
            pass

        lists_manager = ListsManager(words_set)

        while change:
            select_change_mode = input('select change mode(del, add): ')
            if select_change_mode not in ('del', 'add'):
                continue

            change_mode: bool = True
            while change_mode:

                w_s: set[tuple[str, str]] = lists_manager.words_set
                for word_pair in w_s:
                    print(f'{word_pair[0]} = {word_pair[1]}')
                print(f'(there are {len(w_s)} word pairs)')

                print_words: str = input('print words(foreign, local): ')
                words: list[str] = [word.strip() for word in print_words.split(',')]

                try:
                    if select_change_mode == 'del':
                        lists_manager.delete_word(words[0], words[1])
                    elif select_change_mode == 'add':
                        lists_manager.add_word(words[0], words[1])
                except IndexError:
                    print('false form')

                    try:
                        text_manager.write_text_file(lists_manager.words_set)
                    except (FileNotFoundError, AttributeError):
                        pass

                command: str = input(f'press enter to continue {select_change_mode}, or q to exit: ')
                subprocess.run("cls" if os.name == "nt" else "clear", shell=True)
                if command == 'q':
                    change_mode = False

            command = input('press enter to continue batch word changing or q to return in menu: ')
            subprocess.run("cls" if os.name == "nt" else "clear", shell=True)
            if command == 'q':
                change = False

        try:
            text_manager.write_text_file(lists_manager.words_set)
        except (FileNotFoundError, AttributeError):
            pass


    def prompt(self) -> str:
        return 'print cbw to change batch words'

    def command_select(self, command: str, *args, **kwargs):
        if command == 'cbw':
            batch_name: str = input('select batch: ')

            ChangeBatchWordsQuery.__change_batch_words(batch_name)
            subprocess.run("cls" if os.name == "nt" else "clear", shell=True)