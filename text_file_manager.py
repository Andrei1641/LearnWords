from abc import abstractmethod, ABC

class TextFileManager(ABC):
    def __init__(self, name):
        self._name = name

    @abstractmethod
    def create_word_set(self) -> set[tuple[str, str]]:
        ...

    @abstractmethod
    def write_text_file(self, words: set[tuple[str, str]]):
        ...



class OneTextFileManager(TextFileManager):

    def create_word_set(self) -> set[tuple[str, str]]:
        raw_text: str = ''

        try:
            with open(f'words/{self._name}/words.txt', 'r') as f:
                raw_text = f.read()
        except FileNotFoundError:
            raise FileNotFoundError(f'file {self._name} does not exist')


        parts: list[list[str]] = [word_par.split() for word_par in raw_text.splitlines()]

        words_set: set[tuple[str, str]] = set()
        try:
            words_set = {(f.strip(), l.strip()) for f, l in parts}
        except ValueError:
            raise ValueError(f'the batch {self._name} is empty')

        return words_set


    def write_text_file(self, words: set[tuple[str, str]]):
        word_pairs = ['\n'.join(f'{f} = {l}') for f, l in words]

        raw_text: str = '\n'.join(word_pairs)
        try:
            with open(f'words/{self._name}/words.txt', 'w') as f:
                f.write(raw_text)
        except FileNotFoundError:
            raise FileNotFoundError(f'file {self._name} does not exist')


class TwoTextFileManager(TextFileManager):

    def create_word_set(self) -> set[tuple[str, str]]:
        foreign_words: list[str] = []
        local_words: list[str] = []
        with open(f'words/{self._name}/words_f.txt', 'r') as f:
            foreign_words = f.read().splitlines()

        with open(f'words/{self._name}/words_l.txt', 'r') as f:
            local_words = f.read().splitlines()

        word_set: set[tuple[str, str]] = set(zip(foreign_words, local_words))
        return word_set


    def write_text_file(self, words: set[tuple[str, str]]):
        foreign_words, local_words = zip(*words)

        raw_foreign_words = '\n'.join(foreign_words)
        raw_local_words = '\n'.join(local_words)

        with open(f'words/{self._name}/words_f.txt', 'w') as f:
            f.write(raw_foreign_words)
        with open(f'words/{self._name}/words_l.txt', 'w') as f:
            f.write(raw_local_words)