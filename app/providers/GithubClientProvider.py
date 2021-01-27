"""A GithubClientProvider Service Provider."""

from masonite.provider import ServiceProvider
from github import Github
from masonite.helpers import config
from app.commands.FetchGithubUsersCommand import FetchGithubUsersCommand

class GithubClientProvider(ServiceProvider):
    """Provider service for Github."""

    wsgi = False

    def register(self) -> None:
        self.app.bind('Github', Github(config('github.oauth.access_token')))
        self.app.bind('FetchGithubUsersCommand', FetchGithubUsersCommand)
