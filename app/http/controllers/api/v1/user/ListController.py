"""A ListController Module."""

from masonite.controllers import Controller
from masonite.request import Request
from app.User import User
from masoniteorm.query.QueryBuilder import QueryBuilder


class ListController(Controller):
    """ListController Controller Class."""

    def index(self, request: Request):
        query: QueryBuilder = User

        if request.has('order_by'):
            order: str = request.input('order_by')
            query = query.order_by(order, 'DESC' if order.startswith('-') else 'ASC')

        # Match search
        for column in ['id', 'type']:
            if request.has(column):
                query = query.where(column, '=', request.input(column))

        # Like search
        for column in ['name', 'username', 'email', 'url_profile']:
            if request.has(column):
                query = query.where(column, 'like', f'%{request.input(column)}%')

        return query.paginate(
            int(request.input('pagination', 25)),
            int(request.input('page', 1))
        )
