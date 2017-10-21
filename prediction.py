import gensim

model = gensim.models.Word2Vec()


def train(method):
    sentences = []
    with open("filtered_messages.txt", encoding="utf-8") as file:
        for line in file:
            buf = line.replace('\n', '').split(', ')
            filtered_buf = list(filter(lambda x: len(x) > 1 or x == 'я' or x == 'к', buf))

            if filtered_buf:
                sentences.append(filtered_buf)
    return gensim.models.Word2Vec(sentences, min_count=1, workers=4, sg=method)


def predict(message, model_word):
    list_message = message.split('|_')
    while '' in list_message:
        list_message.remove('')
    print(list_message)
    return model_word.predict_output_word(list_message, topn=10)
