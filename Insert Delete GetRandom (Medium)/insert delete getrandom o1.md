##### **Задача**
Реализовать структуру данных, в которой есть методы: *добавить элемент*, *удалить элемент*, *вернуть случайный элемент с одинаковой вероятностью*. Все эти операции должны выполняться за $O(1)$ по времени.
##### **Крайние случаи**
Так как *'set' object is not subscriptable*, то функция random.choice() не сработает с ним. 
##### **Логика решения**
Для того, чтобы всё работало за $O(1)$ нужно понимать следующие вещи: 
* функция random.choice() не сработает с set()
* функция random.choice() работает с list за $O(1)$
* Однако нужно проверять за $O(1)$, находится ли элемент в структуре или нет
* Для этого нужен именно словарь, так как вместе с элементом нужно хранить ещё и его индекс в массиве, чтобы уметь переходить из одной структуры в другую.
* Удалять из массива за $O(1)$ можно следующим образом: поменять местами последний элемент массива и тот который надо удалить, сделать pop()
Остальные технические моменты можно понять из кода
##### **Решение**
```python
class RandomizedSet:
    def __init__(self):
        self.rs = {}
        self.data = []

    def insert(self, val: int) -> bool:
        if val not in self.rs:
            self.data.append(val)
            self.rs[val] = len(self.data) - 1
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.rs:
            pr = self.data[-1]
            idx = self.rs[val]
            self.data[idx] = pr
            self.data[-1] = val
            self.data.pop()
            self.rs[pr] = idx
            self.rs.pop(val)
            return True
        else:
            return False
            
    def getRandom(self) -> int:
        return random.choice(self.data)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
```

##### **Теги**
#Компетенции 
##### **Ссылки**
[[Алгоритмы и структуры данных]]