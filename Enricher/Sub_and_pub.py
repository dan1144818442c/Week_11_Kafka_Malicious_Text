from Tools import kafka_consumer , kafka_producer, cleaner , sub_pub
from Enricher.enricher import Enricher_C


def add_enricher_func(topic_to_send_for_antisemitic ,topic_to_send_for_not_antisemitic ,consumer , publisher:kafka_producer.Produce , path_weapon_list):
    for message in consumer:
        dic_ = message.value
        enr = Enricher_C(dic_)
        dic_with_enricher_add =  enr.activate_all_func(path_weapon_list=path_weapon_list)

        if message.topic   == 'preprocessed_tweets_antisemitic':
            print(dic_with_enricher_add)
            publisher.publish_message(topic_to_send_for_antisemitic , dic_with_enricher_add)
        elif message.topic == "preprocessed_tweets_not_antisemitic":
            print(dic_with_enricher_add)

            publisher.publish_message(topic_to_send_for_not_antisemitic , dic_with_enricher_add)

if __name__ == '__main__':
    con,sub = sub_pub.sub_and_pub('preprocessed_tweets_antisemitic' , 'preprocessed_tweets_not_antisemitic')
    add_enricher_func('enriched_preprocessed_tweets_antisemitic' , 'enriched_preprocessed_tweets_not_antisemitic' , consumer=con , publisher=sub , path_weapon_list=r'/app/Enricher/weapon_list.txt')


