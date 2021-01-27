# Test git Github.

### Requirements

 - **Python** 3.8
 - **Virtualenv** 20.4

### How to install:
 - For create the virtual environemnt, you shall run this command in your terminal:  ```python -m venv venv```.
 - Next, activate the virtualenv. If you operative system is Linux/Unix, you can run ```source venv/bin/activate```, else run ```./venv/Scripts/activate``` if your OS is Windows.
 - Install all python pakages runing into virtualenv the next command: ```pip install -r requirements.txt```.
 - Now, duplicate the ```.env-example``` file and rename as ```.env```.
 - Go to [https://github.com/settings/tokens](https://github.com/settings/tokens) for generate an access token. Copy and save the code into ```.env``` file next to **GITHUB_ACCESS_TOKEN** key, like this:
```text
    GITHUB_ACCESS_TOKEN=1e196492985a2af9b75224dbc09249744a25f86a
```
 - Save changes.

### Database
 - Activate virtualenv in your shell.
 - Run ```python craft migrate``` for create the SQLite file with USER table.
 - For start to consume the Github API, run in shell the next command:
```bash
python craft github:fetch-users
```
 - By default the task pull 150 users from API and store in SQLite database. If you need custon the number or users yo pull you can set the optional agument ```total```. Example:
```bash
python craft github:fetch-users --total=20
```

### Start the Server
 - Activate virtualenv in your shell.
 - Run ```python craft serve```.

### Consume API
 - You can consume the API make a request at the next address: [http://127.0.0.1:8000/api/v1/user?page=4&pagination=15](http://127.0.0.1:8000/api/v1/user?page=4&pagination=15)
 - The available url parameters are:
    - **pagination**: Number with the size of chunks to return. By default is 25.
    - **page**: Number with the page index to see.
    - **id**: Number that filter the ```id``` column. The operator to use is equals.
    - **type**: String that filter the ```type``` column. The operator to use is equals
    - **name**: String that filter the ```name``` column. The operator to use is like.
    - **username**: String that filter the ```username``` column. The operator to use is like.
    - **email**: String that filter the ```email``` column. The operator to use is like.
    - **url_profile**: String that filter the ```url_profile``` column. The operator to use is like.
    - **order_by**: String for sort fields. By default sort using ```asc``` operator. For sort in ```desc``` mode you can add the prefix ```-``` to value, for example: ```order_by=-id```
