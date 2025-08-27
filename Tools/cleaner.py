import string
import re
import nltk

nltk.download('stopwords')
nltk.download('wordnet')


class Cleaner:
    @staticmethod
    def remove_special_characters_and_marks(text):
        translator = str.maketrans('', '', string.punctuation)
        return text.translate(translator)

    @staticmethod
    def removing_unnecessary_spaces(text):
        return re.sub(' +', ' ', text).strip()

    @staticmethod
    def removing_stop_words(text ,language ='english'):
        stop_words = set(nltk.corpus.stopwords.words(language))
        text = ' '.join([word for word in text.split() if word not in (stop_words)])
        return text

    @staticmethod
    def get_text_in_lowercase(text):
        return text.lower()

    @staticmethod
    def get_matize_text(text):
        lemmatizer =nltk.stem.WordNetLemmatizer()
        word_list = nltk.word_tokenize(text)
        lemmatized_output = ' '.join([lemmatizer.lemmatize(w) for w in word_list])
        return  lemmatized_output

    @staticmethod
    def activate_all_functions(text):
        text_without_marks = Cleaner.remove_special_characters_and_marks(text)
        text_removing_unnecessary_spaces = Cleaner.removing_unnecessary_spaces(text_without_marks)
        text_removing_stop_words = Cleaner.removing_stop_words(text_removing_unnecessary_spaces)
        text_matize = Cleaner.get_matize_text(text_removing_stop_words)
        text_in_lowercase= Cleaner.get_text_in_lowercase(text_matize)
        return text_in_lowercase
# print(Cleaner.activate_all_functions("ghfjgkh dgfbn    sfhj BHGRRV a bugs 58 * / 0456 jnf8 543%$#@"))