from gensim import corpora, models, similarities, downloader
import pandas as pd
import json


def main():
    doc = pd.read_csv('synonyms.csv')
    name_model = 'word2vec-google-news-300'
    # name_model = 'glove-twitter-200'
    model = downloader.load(name_model)
    correct_guesses = 0
    answer_without_guessing = 0
    vocab = []
    output_file = open(name_model + '-details.csv', 'w')

    for index, word in enumerate(model.index_to_key):
        vocab.append(word)

    for i in range(80):
        row = doc.loc[i, :]
        question_word = row.loc["question"]
        answer_word = row.loc["answer"]
        try:
            similars = model.most_similar(question_word)
            answer_without_guessing += 1
            guess_word = similars[0][0]

            choices = row["0":]
            count = 0
            for j in range(len(choices)):
                if choices[j] in vocab == False:
                    count += 1

            if count == 4:
                ans = "guess"
            elif answer_word == guess_word:
                ans = "correct"
                correct_guesses += 1
            else:
                ans = "wrong"
            output = str(question_word) + "," + str(answer_word) + "," + str(guess_word) + "," + str(ans) + "\n"
        except KeyError:
            output = str(question_word) + "," + str(answer_word) + "," + "NO ANSWER,guess\n"

        output_file.write(output)

    analysis_file = open("analysis.csv", "a")

    analysis_output = name_model + ',' + str(len(model.index_to_key)) + ',' + str(correct_guesses) + ',' \
                      + str(answer_without_guessing) + ',' + str(correct_guesses / answer_without_guessing) + "\n"

    analysis_file.write(analysis_output)


if __name__ == "__main__":
    main()
