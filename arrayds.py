class Array:
    def __init__(self) -> None:
        self._capacity = 0
        self._size = 0
        self._data = None

    def __getitem__(self, index):
        if index >= 0 and index < self._size:
            return self._data[index]
        return None
    
    def __setitem__(self, index, value):
        if index >= 0 and index < self._size:
            self._data[index] = value
      
    def expand(self):
        if self._size < self._capacity:
            return
        
        if self._capacity == 0:
            new_capacity = 5
        else:
            new_capacity = self._capacity + (self._capacity // 2)
        new_data = [None] * new_capacity
        for i in range(self._capacity):
            new_data[i] = self._data[i]
        self._capacity = new_capacity
        self._data = new_data


   # O(n)
    def insert_back(self, value):
        self.expand()

        self._data[self._size] = value

        # update attributes O(1)
        self._size += 1

    # O(n)
    def insert_front(self, value):
        self.expand()

        for i in range(self._size):
            self._data[i + 1] = self._data[i]

        self._size += 1
  
    # O(1)
    def count(self):
        return self._size
    
    def contains(self, other):
        if self._size >= other.size:
            for i in range (self._size - other.size + 1):
                all_same = True
                for j in range (other.size):
                    if self._data[i + j] != other.data[j]:
                        all_same = False
                        break
                if all_same:
                    return True
        return False


my_array = Array()
my_array.insert_back(4)
my_array.insert_back(5)
my_array.insert_back(2)
my_array.insert_back(1)

print(my_array[2])
my_array[2] = 15
print(my_array[2])

other = Array()
other.insert_back(2)
other.insert_back(1)

result1 = my_array.contains(other)

other2 = Array()
other2.insert_back(1)
other2.insert_back(2)

result2 = my_array.contains(other2)