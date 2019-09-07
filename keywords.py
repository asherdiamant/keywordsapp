import requests
import string
import pandas as pd


def get_suggestions(queryroot):
    num_results = 5
    formatted_root = '+'.join(queryroot.split())

    results = []
    relevance = []
    for suffix in string.ascii_lowercase:
        formatted_query = formatted_root + '+' + suffix
        response = requests.get(f'https://suggestqueries.google.com/complete/search?client=chrome&q={formatted_query}')
        results += response.json()[1][0:num_results]
        relevance += response.json()[4]['google:suggestrelevance'][0:num_results]

    results_list = list(zip(results, relevance))
    sorted_results = sorted(results_list, key=lambda tup: tup[1], reverse=True)
    df = pd.DataFrame(sorted_results, columns=['keyword', 'relevance'])
    return df.to_html()
