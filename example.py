from main import Database

def main():
    db = Database("test_db")

    db.update_key("value", "ping")
    print(db.get_key("value"))

    db.update_key("value", "pong")
    print(db.get_key("value"))

    db.delete_key("value")

if __name__ == "__main__":
    main()