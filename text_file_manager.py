from abc import abstractmethod, ABC

class TextFileManager(ABC):

    @abstractmethod
    def create_word_set(self) -> set[tuple[str, str]]:
        ...

    @abstractmethod
    def write_text_file(self, words: set[tuple[str, str]]):
        ...



class OneTextFileManager(TextFileManager):
    def __init__(self, file_names: str):
        self.__file_names = file_names


    def create_word_set(self) -> set[tuple[str, str]]:
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

        words_set: set[tuple[str, str]] = set()
        try:
            words_set = [(f.strip(), l.strip()) for f, l in parts]
        except ValueError:
            raise ValueError(f'the batch {self.__file_names} is empty')

        return words_set


    def write_text_file(self, words: set[tuple[str, str]]):
        word_pars: list[str] = []
        for word in words:
            word_pars.append(f'{word[0]} = {word[1]}')

        raw_text = '\n'.join(word_pars)
        try:
            with open(f'words/{self.__file_names}/words.txt', 'w') as f:
                f.write(raw_text)
        except FileNotFoundError:
            raise FileNotFoundError(f'file {self.__file_names} does not exist')



class TwoTextFileManager(TextFileManager):
    def __init__(self, file_name: str):
        self.__file_name = file_name

    def create_word_set(self) -> set[tuple[str, str]]:
        foreign_words: list[str] = []
        local_words: list[str] = []
        with open(f'words/{self.__file_name}/words_f.txt', 'r') as f:
            raw_foreign_words: str = f.read()
            foreign_words = raw_foreign_words.split('\n')

        with open(f'words/{self.__file_name}/words_l.txt', 'r') as f:
            raw_local_words: str = f.read()
            local_words = raw_local_words.split('\n')

        word_set: set[tuple[str, str]] = set(zip(foreign_words, local_words))
        return word_set

    def write_text_file(self, words: set[tuple[str, str]]):
        foreign_words, local_words = zip(*words)

        raw_foreign_words = '\n'.join(foreign_words)
        raw_local_words = '\n'.join(local_words)

        with open(f'words/{self.__file_name}/words_f.txt', 'w') as f:
            f.write(raw_foreign_words)
        with open(f'words/{self.__file_name}/words_l.txt', 'w') as f:
            f.write(raw_local_words)