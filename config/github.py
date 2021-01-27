from masonite.environment import LoadEnvironment, env

LoadEnvironment()

OAUTH = {
    'access_token':  env('GITHUB_ACCESS_TOKEN')
}
