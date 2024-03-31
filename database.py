import json
import os
import tempfile
from typing import Any

class Database:
    """
    A class to manage a simple key-value store using a JSON file.
    """

    def __init__(self, name: str, keys: dict = {}):
        """
        Initialize a new instance of the Database class.

        Args:
            name (str): The name of the JSON file.
            keys (dict, optional): A dictionary containing the initial data. Defaults to an empty dictionary.
        """
        self.name = name
        self.keys = keys

    def save_db(self):
        """
        Save the data dictionary to the JSON file in an atomic way.

        Raises:
            Exception: If an error occurs while creating or writing to the file.
        """
        try:
            temp_file = tempfile.NamedTemporaryFile(mode="w+", delete=False)

            json.dump(self.keys, temp_file, indent=4)
            temp_file.flush()
            temp_file.close()

            target_file = f"{self.name}.json"
            os.replace(temp_file.name, target_file)

        except (FileNotFoundError, IOError, PermissionError) as e:
            raise Exception(e)
        
    def _convert_key(self, key: Any):
        """
        Convert a non-string key to a string representation.

        Args:
            key (Any): The key to be converted.

        Returns:
            str: The string representation of the key.
        """
        return str(key)

    def update_key(self, key: Any, value: Any):
        """
        Update or add a new key-value pair to the data dictionary.

        Args:
            key (Any): The key to update or add.
            value (Any): The value associated with the key.
        """
        key_str = self._convert_key(key)
        self.keys.update({key_str: value})
        self.save_db()

    def delete_key(self, key: Any):
        """
        Remove a key-value pair from the data dictionary.

        Args:
            key (Any): The key to remove.
        """
        key_str = self._convert_key(key)
        self.keys.pop(key_str)
        self.save_db()

    def get_key(self, key: Any):
        """
        Get the value associated with a key from the data dictionary.

        Args:
            key (Any): The key for which to get the value.

        Returns:
            Any: The value associated with the key, or None if the key does not exist.
        """
        key_str = self._convert_key(key)
        return self.keys.get(key_str)
    
    def get_keys(self):
        """
        Get all the keys in the data dictionary.

        Returns:
            dict_keys: A view of the keys in the data dictionary.
        """
        return self.keys.keys()
    
    def has_key(self, key: Any):
        """
        Check if a key exists in the data dictionary.

        Args:
            key (Any): The key to check.

        Returns:
            bool: True if the key exists, False otherwise.
        """
        key_str = self._convert_key(key)
        return True if self.keys.get(key_str) else False
    
    def __str__(self):
        """
        Represent the data dictionary as a string.

        Returns:
            str: A string representation of the data dictionary.
        """
        return str(self.keys)