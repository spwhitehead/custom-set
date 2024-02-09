class CustomSet:
    def __init__(self):
        my_set = []

    def add(self, item: str):
        """Add an item to the list"""
        if item not in self.my_set[]:
           return self.my_set.add(item)


    def remove(self, item: str):
        """Remove an item from the list"""
        if item in self.my_set[]:
            return self.my_set.remove(item)

    def as_list(self):
        """Returns all the items in the list"""
        pass

    def clear(self):
        """Removes all the items from the list"""
        pass

def main():
    pass



if __name__ == "__main__":
    main()
