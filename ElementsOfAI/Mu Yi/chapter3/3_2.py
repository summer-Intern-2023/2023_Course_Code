import numpy as np
text = '''Humpty Dumpty sat on a wall
Humpty Dumpty had a great fall
all the king's horses and all the king's men
couldn't put Humpty together again'''


def main(text):
    # tasks your code should perform:

    # 1. split the text into words, and get a list of unique words that appear in it
    # a short one-liner to separate the text into sentences (with words lower-cased to make words equal
    # despite casing) can be done with
    # docs = [line.lower().split() for line in text.split('\n')]

    # 2. go over each unique word and calculate its term frequency, and its document frequency

    # 3. after you have your term frequencies and document frequencies, go over each line in the text and
    # calculate its TF-IDF representation, which will be a vector

    # 4. after you have calculated the TF-IDF representations for each line in the text, you need to
    # calculate the distances between each line to find which are the closest.
    docs = [line.lower().split() for line in text.split('\n')]

    # 1. split the text into words, and get a list of unique words that appear in it
    unique_words = set()
    for doc in docs:
        for word in doc:
            unique_words.add(word)
    unique_words = list(unique_words)

    # 2. go over each unique word and calculate its term frequency, and its document frequency
    term_freq = np.zeros((len(docs), len(unique_words)))
    doc_freq = np.zeros(len(unique_words))
    for i, sentence in enumerate(docs):
        for j, word in enumerate(sentence):
            term_freq[i][j] = sentence.count(word)

        for k, word_1 in enumerate(unique_words):
            if word_1 in sentence:
                doc_freq[k] += 1

    # 3. after you have your term frequencies and document frequencies, go over each line in the text and
    # calculate its TF-IDF representation, which will be a vector
    tf_idf = np.zeros((len(docs), len(unique_words)))
    for i, doc in enumerate(docs):
        for j, word in enumerate(doc):
            # print(word, term_freq[i][j], doc_freq[unique_words.index(word)])
            tf_idf[i][j] = (1/term_freq[i][j]) - \
                np.log(len(docs) / doc_freq[unique_words.index(word)])

    # 4. after you have calculated the TF-IDF representations for each line in the text, you need to
    # calculate the distances between each line to find which are the closest.
    distances = np.zeros((len(docs), len(docs)))
    for i, doc in enumerate(tf_idf):
        for j, doc2 in enumerate(tf_idf):
            if i == j:
                distances[i][j] = np.inf
            else:
                distances[i][j] = np.sum(np.abs(doc - doc2))

    print(np.unravel_index(np.argmin(distances), distances.shape))


main(text)
