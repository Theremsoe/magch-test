"""A FetchGithubUsersCommand Command."""
from cleo import Command
from github import Github, GithubObject
from github.NamedUser import  NamedUser
from wsgi import container
from app.User import User
from typing import List, Callable, Iterator
from masoniteorm.query import QueryBuilder


class FetchGithubUsersCommand(Command):
    """
    Description of command

    github:fetch-users
        {--total=150 : Max number of random users at store in database. By default 150}
    """

    def handle(self) -> None:
        total: int = int(self.option('total'))
        table: str = User().get_table_name()
        stored: int = 0
        CastToUser: Callasble[[NamedUser], dict] = lambda user: User.create({
            'id': user.id,
            'name': user.name,
            'username': user.login,
            'email': user.email,
            'picture': user.avatar_url,
            'type': user.type,
            'url_profile': user.html_url,
        })

        for users in UsersIterator.iterate():
            stored += len(list(map(CastToUser, users)))

            print(stored)

            if stored >= total:
                break


class UsersIterator:
    """Users iterator
    """
    def __init__(self):
        self.client: Github = container.make(Github)
        self.last: NamedUser = None

    def __iter__(self) -> Iterator:
        while True:
            items: List[NamedUser] = self.fetch()

            self.last = items[-1] if len(items) else None

            yield items

    def fetch(self) -> List[NamedUser]:
        return self.client.get_users(self.since).get_page(1)

    @property
    def since(self) -> GithubObject.NotSet:
        return self.last.id if self.last else GithubObject.NotSet

    @staticmethod
    def iterate() -> Iterator:
        return iter(UsersIterator())
