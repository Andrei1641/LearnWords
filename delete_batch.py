import shutil

from queries.query import Query
from pathlib import Path


class DeleteBatchQuery(Query):
    @staticmethod
    def delete_batch(name):
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
            try:
                DeleteBatchQuery().delete_batch(name)
            except FileNotFoundError as e:
                print(e)