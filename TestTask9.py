from collections import Counter


queries = [
    "watch new movies", "coffee near me", "how to find the determinant", "python",
    "data science jobs in UK", "courses for data science", "taxi", "google", "yandex",
    "bing", "foreign exchange rates USD/BYN", "Netflix movies watch online free",
    "Statistics courses online from top universities"
]

def queries_distribution(queries):
    count_word = Counter()

    for el in queries:
        words = el.split()
        num_words = len(words)
        count_word[num_words] +=1

    total_queries = len(queries)

    for num_words, count in count_word.items():
        percentage = (count / total_queries) * 100
        print(f"{num_words} слова: {percentage:.2f}%")

queries_distribution(queries)