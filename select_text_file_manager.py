from text_file_manager import TextFileManager, TwoTextFileManager, OneTextFileManager
from pathlib import Path


class SelectTextFileManager:
    @staticmethod
    def select(name: str) -> TextFileManager:
        path_f = Path(f'words/{name}/words_f.txt')
        path_l = Path(f'words/{name}/words_l.txt')
        if path_f.exists() and path_l.exists():
            return TwoTextFileManager(name)

        path_standard = Path(f'words/{name}/words.txt')
        if path_standard.exists():
            return OneTextFileManager(name)

        raise FileNotFoundError(f'{name} does not exist')