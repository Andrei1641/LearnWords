from queries.query import Query
from pathlib import Path


class RenameBatchQuery(Query):
    def prompt(self) -> str:
        return 'print rnb to rename batch'

    def command_select(self, command: str, *args, **kwargs):
        if command == 'rnb':
            path = Path(f'words/{args[0]}')
            new_name: str = input('print new name: ')
            path.rename(f'words/{new_name}')