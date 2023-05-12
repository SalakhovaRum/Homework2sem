import hashlib
import time

#  Создаем функцию, которая на основе нужных параметров создает первый блок.
class Block:
    def __init__(self, index, previous_hash, hash, timestamp, data):
        self.index = index
        self.previous_hash = previous_hash
        self.hash = hash
        self.timestamp = timestamp
        self.data = data


def create_first_block():
    index = 0
    previous_hash = ""
    timestamp = time.time()
    data = "Hello, world!"
    hash = calculate_hash(index, previous_hash, timestamp, data)
    return Block(index, previous_hash, hash, timestamp, data)

# Создаем функцию add_block, которая будет добавлять новый блок к уже существующим.
def add_block(data, blockchain):
    previous_block = blockchain[-1]
    index = previous_block.index + 1
    previous_hash = previous_block.hash
    timestamp = time.time()
    hash = calculate_hash(index, previous_hash, timestamp, data)
    new_block = Block(index, previous_hash, hash, timestamp, data)
    blockchain.append(new_block)

#  Реализация хэш-функции  SHA-256
def calculate_hash(index, previous_hash, timestamp, data):
    hash_data = (str(index) + previous_hash + str(timestamp) + data).encode('utf-8')
    return hashlib.sha256(hash_data).hexdigest()

# Добавляем заданное количество блоков в цепочку блоков blockchain с последовательными данными
def create_blocks(amount, blockchain):
    for i in range(amount):
        data = f"Block #{i+1}"
        add_block(data, blockchain)

# Для проверки работы блокчейна, добавим код создания 10 блоков и вывод информации об индексе, данных и хэше каждого блока в цепочке.
blockchain = [create_first_block()]
create_blocks(10, blockchain)

for block in blockchain:
    print(f"Index: {block.index}")
    print(f"Data: {block.data}")
    print(f"Hash: {block.hash}")
    print(f"Timestamp: {block.timestamp}")
    print("------------------------------")