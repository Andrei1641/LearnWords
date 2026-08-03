import os
import shutil
import subprocess

from queries.query import Query
from pathlib import Path


class DeleteBatchQuery(Query):
    @staticmethod
    def __delete_batch(name: str):
        path = Path(f'words/{name}')
        if path.exists():
            shutil.rmtree(path)
        else:
            raise FileNotFoundError(f'file: {name} does not exist')


    def prompt(self) -> str:
        return 'print dlb to delete batch'

    def command_select(self, command: str, *args, **kwargs):
        if command == 'dlb':
            name = input('write name of a word batch, you want to delete: ')
            subprocess.run("cls" if os.name == "nt" else "clear", shell=True)
            try:
                DeleteBatchQuery().__delete_batch(name)
            except FileNotFoundError as e:
                print(e)