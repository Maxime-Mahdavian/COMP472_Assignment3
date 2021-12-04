from gensim import corpora, models, similarities, downloader
import pandas as pd
import matplotlib.pyplot as plt


def create_plot():
    left = [1, 2, 3, 4, 5]


def main():
    # doc = pd.read_csv('synonyms.csv')
    # name_model = 'glove-twitter-25'
    # # model_other = '/home/max/gensim-data/word2vec-wikigiga-300/glove.6B.300d.txt'
    # model = downloader.load(name_model)
    # # model = models.KeyedVectors.load_word2vec_format(model_other, binary=False)
    # correct_guesses = 0
    # answer_without_guessing = 0
    # vocab = []
    # output_file = open(name_model + '-details.csv', 'w')
    #
    # for index, word in enumerate(model.index_to_key):
    #     vocab.append(word)
    #
    # for i in range(80):
    #     row = doc.loc[i, :]
    #     question_word = row.loc["question"]
    #     answer_word = row.loc["answer"]
    #     try:
    #         similars = model.most_similar(question_word)
    #         answer_without_guessing += 1
    #         guess_word = similars[0][0]
    #
    #         choices = row["0":]
    #         count = 0
    #         for j in range(len(choices)):
    #             if choices[j] in vocab == False:
    #                 count += 1
    #
    #         if count == 4:
    #             ans = "guess"
    #         elif answer_word == guess_word:
    #             ans = "correct"
    #             correct_guesses += 1
    #         else:
    #             ans = "wrong"
    #         output = str(question_word) + "," + str(answer_word) + "," + str(guess_word) + "," + str(ans) + "\n"
    #     except KeyError:
    #         output = str(question_word) + "," + str(answer_word) + "," + "NO ANSWER,guess\n"
    #
    #     output_file.write(output)
    #
    # analysis_file = open("analysis.csv", "a")
    #
    # analysis_output = name_model + ',' + str(len(model.index_to_key)) + ',' + str(correct_guesses) + ',' \
    #                   + str(answer_without_guessing) + ',' + str(correct_guesses / answer_without_guessing) + "\n"
    #
    # analysis_file.write(analysis_output)

    analysis_file = pd.read_csv("analysis.csv")
    left =[1,2,3,4,5,6]
    height = []
    for i in range(6):
        height.append(analysis_file.loc[i, "accuracy"])
    print(height)

    tick_label = ['humans', 'google-300','wikiDump-300','gigaword-300', 'twitter-25', 'twitter-200']
    colors =['red', 'blue', 'green', 'orange', 'gold', 'lightcoral']

    bar = plt.bar(left,height, width=0.8, color=colors)
    plt.xlabel('x-axis')
    plt.ylabel('y-axis')
    plt.legend(bar, tick_label, loc='upper center')
    plt.title("Accuracy of every model")
    plt.show()


if __name__ == "__main__":
    main()
