import os
import subprocess

from queries.query import Query
from pathlib import Path


class ChangeBatchSettingsQuery(Query):

    def __init__(self, queries: list[Query]):
        self.__queries: list[Query] = queries


    def __change_batch_setting(self, batch_name: str):
        path: Path = Path(f'words/{batch_name}')

        if path.exists():
            change = True
            while change:
                for query in self.__queries:
                    print(query.prompt())

                next_command = input('your request: ')

                for query in self.__queries:
                    query.command_select(next_command, batch_name)

                command: str = input('press enter to continue history changing or q to return in menu: ')
                if command == 'q':
                    change = False
        else:
            print(f'there is no {batch_name}')


    def prompt(self) -> str:
        return 'print cbs to change barch settings'


    def command_select(self, command: str, *args, **kwargs):
        if command == 'cbs':
            batch_name: str = input('print name of batch, you want to work with: ')
            self.__change_batch_setting(batch_name)
            subprocess.run("cls" if os.name == "nt" else "clear", shell=True)
