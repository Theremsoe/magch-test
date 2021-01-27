from masoniteorm.migrations import Migration
from masoniteorm.schema.Blueprint import Blueprint


class CreateUsersTable(Migration):
    """Generate table USER
    """
    def up(self):
        """Run the migrations
        """
        with self.schema.create("USER") as table:
            table: Blueprint
            table.increments("id")
            table.string("name")
            table.string('username').nullable()
            table.string("email").nullable()
            table.string('picture').nullable()
            table.string('type').nullable()
            table.string('url_profile').nullable()
            table.timestamps()
            table.soft_deletes()

    def down(self):
        """Revert the migrations.
        """
        self.schema.drop("USER")
