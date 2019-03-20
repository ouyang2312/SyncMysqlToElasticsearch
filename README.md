# SyncMysqlToElasticsearch

#### 介绍
利用Binlog和Kafka实时同步mysql数据到Elasticsearch

#### 项目模块
BinlogMiddleware
1、binlog中间件，负责解析binlog，把变动的数据以json形式发送到kafka队列。

KafkaMiddleware
2、kafka中间件，负责消费kafka队列中的Message，把数据写入Elasticsearch中。

#### 基础服务
（1）Mysql
（2）Kafka（用于存放mysql变动消息，存放于Kafka队列）
（3）Elasticsearch

#### 使用说明

1. Demo初始化数据库使用: teemoliu_init.sql
2. Demo初始化ES索引使用：es_build_index.py
3. 教程见：https://www.jianshu.com/p/3ebab93ff075

#### Email:lzhzh825@gmail.com
PS:本demo只是简单示例，有很多可以优化的地方，本人也才疏学浅，欢迎大家提建议。