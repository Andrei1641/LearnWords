from queries.history_add import HistoryAddQuery
from queries.query import Query
from random_select import RandomLearn
from text_file_manager import OneTextFileManager



class LearnWordsQuery(Query):
    @staticmethod
    def select_text_manager(name: str):
        return OneTextFileManager(name)

    def prompt(self) -> str:
        return 'print lw to learn words'

    def command_select(self, command: str, *args, **kwargs):
        if command == 'lw':
            foreign_words: list[str] = []
            local_words: list[str] = []

            raw_names: str = input('write batch names you want to learn: ')
            raw_names = raw_names.replace(' ', '')
            batch_names: list[str] = raw_names.split(',')

            for batch_name in batch_names:
                text_manager = LearnWordsQuery.select_text_manager(batch_name)

                try:
                    words_set = text_manager.create_word_set()
                except ValueError as e:
                    print(e)
                    continue
                except FileNotFoundError as e:
                    print(e)
                    continue

                for word in words_set:
                    foreign_words.append(word[0])
                    local_words.append(word[1])
            print()
            if foreign_words and local_words:
                RandomLearn().learn(foreign_words, local_words)

                refresh_agreement: str = input('do you want to complete refresh time(y/N)')
                if refresh_agreement.lower() == 'y':
                    for batch_name in batch_names:
                        add_refresh = HistoryAddQuery()
                        add_refresh.command_select('hisAdd', batch_name)