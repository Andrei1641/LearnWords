from queries.batch_settings.history_add import HistoryAddQuery
from queries.query import Query
from random_select import RandomLearn
from select_text_file_manager import SelectTextFileManager



class LearnWordsQuery(Query):
    @staticmethod
    def __get_word_lists(batch_names: list[str]) -> tuple[list[str], list[str]]:
        foreign_words: list[str] = []
        local_words: list[str] = []

        for batch_name in batch_names:
            select_t_m = SelectTextFileManager()
            text_manager = select_t_m.select(batch_name)
            words_set: set[tuple[str, str]] = set()
            try:
                words_set = text_manager.create_word_set()
            except (ValueError, FileNotFoundError) as e:
                print(e)
                continue

            foreign_words_tmp, local_words_tmp = zip(*words_set)
            foreign_words += foreign_words_tmp
            local_words += local_words_tmp

        return foreign_words, local_words

    @staticmethod
    def __learn_words(raw_names: str):

        batch_names: list[str] = [name.strip() for name in raw_names.split(',')]

        foreign_words, local_words = LearnWordsQuery.__get_word_lists(batch_names)

        print()
        if foreign_words and local_words:
            RandomLearn().learn(foreign_words, local_words)

            refresh_agreement: str = input('do you want to complete refresh time(y/N): ')
            if refresh_agreement.lower() == 'y':
                for batch_name in batch_names:
                    add_refresh = HistoryAddQuery()
                    add_refresh.command_select('hisAdd', batch_name)


    def prompt(self) -> str:
        return 'print lw to learn words'


    def command_select(self, command: str, *args, **kwargs):
        if command == 'lw':
            raw_names: str = input('write batch names you want to learn: ')
            LearnWordsQuery.__learn_words(raw_names)