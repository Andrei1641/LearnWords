import json
import os
import subprocess
from datetime import date

from queries.query import Query



class CreateBatchQuery(Query):

    @staticmethod
    def __create_word_batch(name: str):

        template = {"refresh_time" : [],
                    "refresh_history" : [],
                    "creation_date" : f"{date.today()}"}

        os.makedirs(f'words/{name}', exist_ok=True)
        with open(f'words/{name}/local_settings.json', 'x') as f:
            json.dump(template,f, indent=5)

        open(f'words/{name}/words.txt', 'x').close()


    def prompt(self) -> str:
        return 'print crb to create batch'

    def command_select(self, command: str, *args, **kwargs):
        if command == 'crb':
            ex = False
            while not ex:
                name = input('write name of new word batch: ')
                CreateBatchQuery.__create_word_batch(name)
                command = input('press q to return in menu or enter to create another one: ')
                subprocess.run("cls" if os.name == "nt" else "clear", shell=True)
                if command == 'q':
                    ex = True