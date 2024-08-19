from tensorflow.keras.datasets import imdb
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM, Embedding
from sklearn.model_selection import train_test_split

number_of_words = 10000

(X_train, y_train), (X_test, y_test) = imdb.load_data(num_words=number_of_words)
word_to_index = imdb.get_word_index()
index_to_word = {index: word for (word, index) in word_to_index.items()}

words_per_review = 200

X_train = pad_sequences(X_train, maxlen=words_per_review)
X_test = pad_sequences(X_test, maxlen=words_per_review)

X_test, X_val, y_test, y_val = train_test_split(X_test, y_test, random_state=11, test_size=0.2)

rnn = Sequential()

rnn.add(Embedding(input_dim=number_of_words, output_dim=128, input_length=words_per_review))
rnn.add(LSTM(units=128, dropout=0.2, recurrent_dropout=0.2))
rnn.add(Dense(units=1, activation="sigmoid"))

rnn.compile(optimizer="adam",
            loss="binary_crossentropy",
            metrics=["accuracy"])

print(rnn.summary())

rnn.fit(X_train, y_train, epochs=10, batch_size=32, validation_data=(X_val, y_val))

results = rnn.evaluate(X_test, y_test)
print(results)