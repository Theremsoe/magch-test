"""Web Routes."""

from masonite.routes import Get, Post, RouteGroup

ROUTES = [
    RouteGroup([
            RouteGroup(
                [
                    Get("/", "ListController@index").name("list"),
                ],
                namespace="user",
                name="user.",
                prefix="user",
            ),
        ],
        namespace="api.v1",
        name="api.v1.",
        prefix="/api/v1/",
        add_methods=["OPTIONS"],
    ),
    Get("/", "WelcomeController@show").name("welcome"),
]
