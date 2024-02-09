class CustomSet:
    def __init__(self):
    
        self.my_set = []

    def add(self, item: str):
        """Add an item to the list"""
        if item not in self.my_set:
           return self.my_set.append(item)


    def remove(self, item: str):
        """Remove an item from the list"""
        if item in self.my_set:
            return self.my_set.remove(item)

    def as_list(self):
        """Returns all the items in the list"""
        return self.my_set

    def clear(self):
        """Removes all the items from the list"""
        self.my_set = []

def main():
    my_set = CustomSet()
    my_set.add("item 1")
    my_set.add("item 2")
    my_set.add("item 1")

    print(my_set.as_list()) # ["item 1", "item 2"]

    my_set.remove("item 2")
    print(my_set.as_list()) # ["item 1"]

    try:
        my_set.remove("item 3")
    except KeyError:
        print("Item not removed, moving forward")

    my_set.clear()
    print(my_set.as_list()) # []



if __name__ == "__main__":
    main()
