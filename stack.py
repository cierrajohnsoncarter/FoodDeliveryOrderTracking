from node import Node

class Stack:
  def __init__(self, limit=1000):
    self.top_item = None
    self.size = 0
    self.limit = limit
  
  def push(self, value):
    if self.has_space():
      item = Node(value)
      item.set_next_node(self.top_item)
      self.top_item = item
      self.size += 1
      print("Adding {} to Robert's incoming orders!".format(value))
    else:
      print("You have too many deliveries to complete {}!".format(value))

  def pop(self):
    if not self.is_empty():
      item_to_remove = self.top_item
      self.top_item = item_to_remove.get_next_node()
      self.size -= 1
      print("Delivering " + item_to_remove.get_value())
      return item_to_remove.get_value()
    print("You've completed all your orders.")

  def peek(self):
    if not self.is_empty():
      return self.top_item.get_value()
    print("You don't have any current orders")

  def has_space(self):
    return self.limit > self.size

  def is_empty(self):
    return self.size == 0
  
# Defining an empty order dock
food_delivery = Stack(6)
# Adding orders as they are ready until we have recived the maximum amount of orders 
food_delivery.push("order #109867")
food_delivery.push("order #276558")
food_delivery.push("order #324756")
food_delivery.push("order #406228")
food_delivery.push("order #509912")
food_delivery.push("order #645332")

# Delivering orders from the top of the stack down
print("The first order to be delivered is " + food_delivery.peek())
food_delivery.pop()
food_delivery.pop()
food_delivery.pop()
food_delivery.pop()
food_delivery.pop()
food_delivery.pop()
