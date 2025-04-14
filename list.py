class ListItem:
   def __init__(self, data) -> None:
      self._data = data
      self._next = None

class List:
    def __init__(self) -> None:
      self._head = None

    def insert_to_head(self, data):
        newListItem = ListItem(data)
        if self._head is None:
            self._head = newListItem
            return
        
        newListItem._next = self._head
        self._head = newListItem

    def find(self, data) -> ListItem:
        if self._head is None:
          return None
        n = self._head

        while n is not None: 
            if n.data is data:
                return n
            n = n._next
        return None

lst = List()
lst.insert_to_head(4)
lst.insert_to_head(7)
lst.insert_to_head(10)
