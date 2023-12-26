import requests
from operator import itemgetter

# Make an API call to get the top submission IDs.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
response = requests.get(url)
print("Status code:", response.status_code)

# Process information about each submission.
submission_ids = response.json()
submission_dicts = []

# Iterate over the top 30 submissions.
for submission_id in submission_ids[:30]:
    # Make a separate API call for each submission.
    url = f'https://hacker-news.firebaseio.com/v0/item/{submission_id}.json'
    submission_r = requests.get(url)
    print(submission_r.status_code)

    # Process the response for each submission.
    response_dict = submission_r.json()

    # Create a dictionary for each submission.
    submission_dict = {
        'title': response_dict['title'],
        'link': f'http://news.ycombinator.com/item?id={submission_id}',
        'comments': response_dict.get('descendants', 0)
    }

    submission_dicts.append(submission_dict)

# Sort submissions based on the number of comments in descending order.
submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)

# Print details for each submission.
for submission_dict in submission_dicts:
    print("\nTitle:", submission_dict['title'])
    print("Discussion link:", submission_dict['link'])
    print("Comments:", submission_dict['comments'])
