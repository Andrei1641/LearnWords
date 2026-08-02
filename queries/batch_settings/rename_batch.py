from queries.query import Query
from pathlib import Path


class RenameBatchQuery(Query):

    @staticmethod
    def __rename_batch(new_name: str, old_name: str):
        path = Path(f'words/{old_name}')
        path.rename(f'words/{new_name}')

    def prompt(self) -> str:
        return 'print rnb to rename batch'

    def command_select(self, command: str, *args, **kwargs):
        if command == 'rnb':
            new_name: str = input('print new name: ')
            RenameBatchQuery.__rename_batch(new_name, args[0])
