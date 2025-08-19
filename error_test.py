class Stack:
    def __init__(self):
        self.__stack_list = []

stack_object = Stack()

print(len(stack_object.__stack_list))
# AttributeError: 'Stack' object has no attribute '__stack_list'  ==>  on voit bien que l'on ne peut pas accéder "simplement" à l'attribut privé

print(len(stack_object._Stack__stack_list))
# 0