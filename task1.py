class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        key_hash = self.hash_function(key)
        key_value = [key, value]

        if self.table[key_hash] is None:
            self.table[key_hash] = list([key_value])
            return True
        else:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.table[key_hash].append(key_value)
            return True

    def get(self, key):
        key_hash = self.hash_function(key)
        if self.table[key_hash] is not None:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None
    
# Метод для видалення пари ключ-значення
    def delete(self, key):
        key_hash = self.hash_function(key)

        if self.table[key_hash] is None:
            return False
        for i, pair in enumerate(self.table[key_hash]):
            if pair [0] ==key:
                     del self.table[key_hash][i]
                     return True
        return False
      


H = HashTable(5)
print(H.table)
H.insert("apple", 10)
H.insert("orange", 20)
H.insert("banana", 30)

print(H.table) # Вивід таблиці після вставки

# Вивід значень за ключами
print("Значення за ключами:")
print(H.get("apple"))
print(H.get("orange"))
print(H.get("banana"))

# Видалення пари ключ-значення
print("Видалення 'banana':")
H.delete("banana")
print(H.table)  # Вивід таблиці після видалення 
print(f"Якщо None, то видалено значення--> {H.get("banana")}")  # Перевірка, чи видалено значення
