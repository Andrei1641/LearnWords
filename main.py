from queries.change_batch_settings import ChangeBatchSettingsQuery
from queries.change_batch_words import ChangeBatchWordsQuery
from queries.create_batch import CreateBatchQuery
from queries.history_add import HistoryAddQuery
from queries.history_delete import HistoryDeleteQuery
from queries.learn_words import LearnWordsQuery
from queries.query import Query
from queries.query_request import QueryRequest
from queries.ramaining_time_calculate import RemainingTimeCalculateQuery


queries: list[Query] = [
                        ChangeBatchSettingsQuery([HistoryDeleteQuery(), HistoryAddQuery()]),
                        ChangeBatchWordsQuery(), CreateBatchQuery(),
                        LearnWordsQuery(), RemainingTimeCalculateQuery()
                       ]

query_request = QueryRequest(queries)

query_request.query_select()
