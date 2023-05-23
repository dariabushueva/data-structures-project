class Node:
    """Класс для узла стека"""

    def __init__(self, data, next_node):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """

        self.data = data
        self.next_node = next_node


class Stack:
    """Класс для стека"""

    def __init__(self):
        """Конструктор класса Stack"""

        # при инициализаци наверху стека пусто
        self.top = None

    def __str__(self):
        """Возвращает строковое представление стека"""

        current_node = self.top
        data_list = []
        while current_node:
            data_list.append(str(current_node.data))
            current_node = current_node.next_node
        return '\n'.join(data_list)

    def push(self, data):
        """
        Метод для добавления элемента на вершину стека

        :param data: данные, которые будут добавлены на вершину стека
        """

        node = Node(data, self.top)
        self.top = node

    def pop(self):
        """
        Метод для удаления элемента с вершины стека и его возвращения

        :return: данные удаленного элемента
        """

        node = self.top
        if not node:
            return None
        self.top = node.next_node
        return node.data
