import os
import subprocess

from queries.query import Query

class QueryRequest:
    def __init__(self, queries: list[Query]):
        self.__queries = queries


    def print_prompts(self):
        for query in self.__queries:
            print(query.prompt())


    def search_query(self, command):
        for query in self.__queries:
            query.command_select(command)


    def query_select(self):
        select = True
        while select:
            self.print_prompts()
            print('type q to quit')
            command = input('your request: ')
            subprocess.run("cls" if os.name == "nt" else "clear", shell=True)
            self.search_query(command)
            if command == 'q':
                select = False