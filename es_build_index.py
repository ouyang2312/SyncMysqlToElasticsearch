# -*- coding: utf-8 -*-


import logging
import socket
import sys

from elasticsearch import Elasticsearch

socket.setdefaulttimeout(30)

reload(sys)
sys.setdefaultencoding('utf-8')

es_host = '127.0.0.1'
es_port = '9200'


# 设置mapping
def set_mapping():
    my_mapping = \
        {
            'mappings': {
                'user': {
                    'properties': {
                        'id': {
                            'type': 'long'
                        },
                        'name': {
                            'type': 'keyword'
                        }
                    }
                },
                'role': {
                    'properties': {
                        'id': {
                            'type': 'long'
                        },
                        'name': {
                            'type': 'keyword'
                        }
                    }
                },

            },
            'settings': {
                'index': {
                    'refresh_interval': '60s',  # 减少shard刷新间隔，用于大规模bulk插入，且对实时查询不要求时使用，完成bulk插入后再修改为1s
                    'number_of_shards': '5',  # 初始化20个主分片, 分片数量确定后不可修改, 非常重要
                    'number_of_replicas': '0',  # 设置1个备份，bulk导入大量的数据，可以考虑不要副本，设置为0
                    'translog': {
                        'sync_interval': '60s',  # sync间隔调高
                        'durability': 'async',  # 异步更新
                        'flush_threshold_size': '1g'  # log文件大小
                    }
                }
            }
        }
    # 创建Index和mapping
    create_index = elastic.indices.create(index='temmoliu', body=my_mapping)  # {u'acknowledged': True}
    if create_index['acknowledged'] == True:
        logging.warn('Index creation success!')


if __name__ == '__main__':
    logging.basicConfig(level=logging.WARNING,
                        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                        datefmt='%a, %d %m %Y %H:%M:%S',
                        filename='wtv3_create_index.log',
                        filemode='a')


    elastic = Elasticsearch(hosts=[es_host + ':' + es_port], timeout=50)
    set_mapping()
