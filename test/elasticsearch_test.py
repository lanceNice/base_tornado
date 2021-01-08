# -*- coding: utf-8 -*-
# @Time    : 2020/12/18 14:49
# @Author  : lance
# @File    : elasticsearch_test.py
# @Software: PyCharm


from elasticsearch import Elasticsearch

# 连接ES
es = Elasticsearch([{'host': '192.168.4.2', 'port': 9200}], timeout=3600)
# print(es.index(index="megacorp",
#                body={"first_name": "xiao", "last_name": "xiao", 'age': 25, 'about': 'I love to go rock climbing',
#                      'interests': ['game', 'play']}))
# print(es.delete(index='megacorp', id='fcvNdHYBUcp2ufMm6Q4k'))
# query = {
#     "query": {
#         "term":{
#             'age': 25
#         }
#     }
# }
# {'took': 0, 'timed_out': False, '_shards': {'total': 1, 'successful': 1, 'skipped': 0, 'failed': 0}, 'hits': {'total': {'value': 0, 'relation': 'eq'}, 'max_score': None, 'hits': []}}
# {'took': 0, 'timed_out': False, '_shards': {'total': 1, 'successful': 1, 'skipped': 0, 'failed': 0}, 'hits': {'total': {'value': 1, 'relation': 'eq'}, 'max_score': 1.0, 'hits': [{'_index': 'megacorp', '_type': '_doc', '_id': 'fMvMdHYBUcp2ufMmVg7T', '_score': 1.0, '_source': {'first_name': 'xiao', 'last_name': 'xiao', 'age': 25, 'about': 'I love to go rock climbing', 'interests': ['game', 'play']}}]}}
# print(es.search(index="megacorp", body=query))













