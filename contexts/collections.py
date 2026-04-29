from databases.db import get_database

User = lambda: get_database().get_collection("users")
