class Node:
    """Класс для узла очереди"""

    def __init__(self, data, next_node=None):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class Queue:
    """Класс для очереди"""

    def __init__(self):
        """Конструктор класса Queue"""
        self.head = None
        self.tail = None

    def enqueue(self, data):
        """
        Метод для добавления элемента в очередь

        :param data: данные, которые будут добавлены в очередь
        """
        node = Node(data)  # Создаем новый узел
        if self.head is None:  # Если очередь пуста, новый узел становится головой и хвостом
            self.head = node
            self.tail = node
        else:  # Иначе добавляем новый узел в конец очереди и обновляем хвост
            self.tail.next_node = node
            self.tail = node

    def dequeue(self):
        """
        Метод для удаления элемента из очереди. Возвращает данные удаленного элемента

        :return: данные удаленного элемента
        """
        if self.head is None:  # Если очередь пуста, возвращаем None
            return None
        head_data = self.head.data  # Запоминаем данные головного элемента
        self.head = self.head.next_node  # Обновляем голову, переходя к следующему узлу
        if self.head is None:  # Если после удаления головного элемента очередь оказалась пустой, обновляем хвост
            self.tail = None
        return head_data

    def __str__(self):
        """Магический метод для строкового представления объекта"""

        current_node = self.head
        data_list = []
        while current_node:
            data_list.append(str(current_node.data))
            current_node = current_node.next_node
        return '\n'.join(data_list)

