from Tools import  cleaner ,sub_pub
import ast

class Preprocessor:

    @staticmethod
    def add_clean_text_and_send(topic_to_send_for_antisemitic ,topic_to_send_for_not_antisemitic ,consumer , publisher):
        for message in consumer:
            dic_ = message.value
            text = dic_['text']
            dic_['clean_text'] = cleaner.Cleaner.activate_all_functions(text)
            if message.topic   == 'raw_tweets_antisemitic':
                publisher.publish_message(topic_to_send_for_antisemitic , dic_)
                print("11")
            elif message.topic == "raw_tweets_not_antisemitic":
                publisher.publish_message(topic_to_send_for_not_antisemitic , dic_)
                # print("00")







if __name__ == '__main__':

    con , sub = sub_pub.sub_and_pub( 'raw_tweets_antisemitic' , 'raw_tweets_not_antisemitic')
    Preprocessor.add_clean_text_and_send('preprocessed_tweets_antisemitic' ,"preprocessed_tweets_not_antisemitic",consumer= con ,publisher= sub)
