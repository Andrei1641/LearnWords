import json
import os
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
                command = input('press enter to return in menu or print 1 to create another one')
                if not command:
                    ex = True