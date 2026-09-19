from stack import Stack


stack = Stack()

print("Пустой:", stack.is_empty())

stack.push(10)
stack.push(20)
stack.push(30)

print("Размер:", stack.size())
print("Верхний элемент:", stack.peek())
print("Удалён:", stack.pop())
print("Верхний после удаления:", stack.peek())
print("Размер:", stack.size())