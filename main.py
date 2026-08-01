from delete_batch import DeleteBatchQuery
from queries.batch_settings.change_batch_settings import ChangeBatchSettingsQuery
from queries.batch_settings.rename_batch import RenameBatchQuery
from queries.change_batch_words import ChangeBatchWordsQuery
from queries.create_batch import CreateBatchQuery
from queries.batch_settings.history_add import HistoryAddQuery
from queries.batch_settings.history_delete import HistoryDeleteQuery
from queries.learn_words import LearnWordsQuery
from queries.query import Query
from queries.query_request import QueryRequest
from queries.ramaining_time_calculate import RemainingTimeCalculateQuery


queries: list[Query] = [
                        ChangeBatchSettingsQuery([HistoryDeleteQuery(), HistoryAddQuery(), RenameBatchQuery()]),
                        ChangeBatchWordsQuery(), CreateBatchQuery(),
                        LearnWordsQuery(), RemainingTimeCalculateQuery(), DeleteBatchQuery()
                       ]

query_request = QueryRequest(queries)

query_request.query_select()
