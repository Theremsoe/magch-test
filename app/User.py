"""User Model."""

from masoniteorm.models import Model


class User(Model):
    """User Model
    """

    __dates__ = ['deleted_at']

    __table__ = 'USER'

    __fillable__ = ['name', 'username', 'email', 'picture', 'type', 'url_profile']
