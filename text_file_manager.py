from abc import abstractmethod, ABC

class TextFileManager(ABC):

    @abstractmethod
    def create_word_lists(self) -> tuple[list[str], list[str]]:
        ...

    @abstractmethod
    def write_text_file(self, foreign_words: list[str], local_words: list[str]):
        ...



class OneTextFileManager(TextFileManager):
    def __init__(self, file_names: str):
        self.__file_names = file_names


    def create_word_lists(self) -> tuple[list[str], list[str]]:
        raw_text: str = ''

        try:
            with open(f'words/{self.__file_names}/words.txt', 'r') as f:
                raw_text = f.read()
        except FileNotFoundError:
            raise FileNotFoundError(f'file {self.__file_names} does not exist')

        word_pars = raw_text.split('\n')
        parts: list[list[str]] = []
        for word_par in word_pars:
            parts.append(word_par.split('='))

        foreign_words = []
        local_words = []
        try:
            foreign_words = [f.strip() for f, l in parts]
            local_words = [l.strip() for f,l in parts]
        except ValueError:
            raise ValueError(f'the batch {self.__file_names} is empty')

        return foreign_words, local_words


    def write_text_file(self, foreign_words: list[str], local_words: list[str]):
        word_pars: list[str] = []
        for i in range(len(foreign_words)):
            word_pars.append(f'{foreign_words[i]} = {local_words[i]}')

        raw_text = '\n'.join(word_pars)

        with open(f'words/{self.__file_names}/words.txt', 'w') as f:
            f.write(raw_text)




class TwoTextFileManager(TextFileManager):
    def __init__(self, file_addresses: list[str]):
        self.__file_addresses = file_addresses

    def create_word_lists(self) -> tuple[list[str], list[str]]:
        ...

    def write_text_file(self, foreign_words: list[str], local_words: list[str]):
        ...