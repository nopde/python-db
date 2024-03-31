# python-db
This is a Python class that manages a simple key-value database. The class provides methods to create, update, delete, and retrieve key-value pairs.

## Usage
- Import the Database class:
```from database import Database```
- Create an instance of the Database class with a name for the database:
```db = Database("my_database")```
You can also provide an initial dictionary of key-value pairs:
```
initial_data = { "name": "John Doe", "age": 30 }
db = Database("my_database", initial_data)
```

### Example usage:
```
initial_data = { "name": "John Doe", "age": 30 }
db = Database("my_database", initial_data)

db.update_key("email", "john@example.com")
db.update_key(123, "This is a number key")

print(db.get_key("name"))  # Output: John Doe
print(db.get_key(123))  # Output: This is a number key

db.delete_key("age")

print(list(db.get_keys()))  # Output: ['name', 'email', '123']
print(db.has_key("age"))  # Output: False
```

## Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request on the project's GitHub repository.