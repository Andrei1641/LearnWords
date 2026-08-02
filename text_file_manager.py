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

        word_pars = raw_text.split('\n')
        parts: list[list[str]] = []
        for word_par in word_pars:
            parts.append(word_par.split('='))

        words_set: set[tuple[str, str]] = set()
        try:
            words_set = [(f.strip(), l.strip()) for f, l in parts]
        except ValueError:
            raise ValueError(f'the batch {self._name} is empty')

        return words_set


    def write_text_file(self, words: set[tuple[str, str]]):
        word_pars: list[str] = []
        for word in words:
            word_pars.append(f'{word[0]} = {word[1]}')

        raw_text = '\n'.join(word_pars)
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
            raw_foreign_words: str = f.read()
            foreign_words = raw_foreign_words.split('\n')

        with open(f'words/{self._name}/words_l.txt', 'r') as f:
            raw_local_words: str = f.read()
            local_words = raw_local_words.split('\n')

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