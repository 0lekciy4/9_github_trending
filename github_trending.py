from datetime import date, timedelta

import requests

TOP_SIZE = 20
GITHUB_API_URL = 'https://api.github.com'
GITHUB_API_SEARCH_QUERY = 'search/repositories'
GITHUB_API_CREATED = 'q=created'
REPOSITORIES_FROM_REQUEST = 'items'
GITHUB_STARS = 'stargazers_count'
GITHUB_OPEN_ISSUES = 'open_issues_count'
GITHUB_REPO_URL = 'html_url'


def get_past_date(days=7):
    now = date.today()
    date_for_search = now - timedelta(days=days)
    return date_for_search


def get_trending_repositories(top_size):
    last_week = get_past_date()
    request = requests.get(
        '{}/{}?{}:>={}'.format(
            GITHUB_API_URL,
            GITHUB_API_SEARCH_QUERY,
            GITHUB_API_CREATED,
            last_week,
        ),
    )
    all_repositories = request.json()[REPOSITORIES_FROM_REQUEST]
    all_repositories.sort(
        key=lambda item: item[GITHUB_STARS],
        reverse=True,
    )
    trending_repositories = all_repositories[:top_size]
    return trending_repositories


if __name__ == '__main__':
    trending_repositories = get_trending_repositories(TOP_SIZE)
    for repo in trending_repositories:
        print('Stars: {}'.format(repo[GITHUB_STARS]))
        print('Open issues: {}'.format(repo[GITHUB_OPEN_ISSUES]))
        print('Repo url: {}'.format(repo[GITHUB_REPO_URL]))
