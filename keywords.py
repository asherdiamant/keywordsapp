import requests
import string
import pandas as pd

fivews = ['how', 'what', 'why', 'who', 'when', 'where']

def get_suggestions(queryroot):
    num_results = 10
    formatted_root = '+'.join(queryroot.split())

    results = []
    relevance = []
    for suffix in ' '+string.ascii_lowercase:
        formatted_query = formatted_root + '+' + suffix
        response = requests.get(f'https://suggestqueries.google.com/complete/search?client=chrome&q={formatted_query}')
        if response.json()[1]:
            results += response.json()[1][0:num_results]
            relevance += response.json()[4]['google:suggestrelevance'][0:num_results]

    for prefix in fivews:
        formatted_query = prefix + '+' + formatted_root
        response = requests.get(f'https://suggestqueries.google.com/complete/search?client=chrome&q={formatted_query}')
        if response.json()[1]:
            results += response.json()[1][0:num_results]
            relevance += response.json()[4]['google:suggestrelevance'][0:num_results]

    results_url = [f'<a href=\"https://www.google.com/search?q={"+".join(kw.split())}\" target="_blank">{kw}</a>' for kw in results]
    results_list = list(zip(results_url, relevance))
    sorted_results = sorted(results_list, key=lambda tup: tup[1], reverse=True)
    df = pd.DataFrame(sorted_results, columns=['keyword', 'relevance'])
    return df.to_html(render_links=True, justify='left', escape=False)

