chai_order = dict(type='Masala Chai', size='Large', sugar=2)
print(f"Chai Order: {chai_order}")

chai_recepie = {}
chai_recepie['base'] = 'black tea'
chai_recepie['liquid'] = 'milk'
print(f"Recepie Base: {chai_recepie['base']}")
print(f"Recepie: {chai_recepie}")
del chai_recepie['liquid']
print(f"Recepie: {chai_recepie}")

# membership testing
print(f"Is sugar in order: {'sugar' in chai_order}")

chai_order = dict(type='Ginger Chai', size='Medium', sugar=1)

# print(f"order details: {chai_order.keys()}")
# print(f"order details: {chai_order.values()}")
# print(f"order details: {chai_order.items()}")

last_item = chai_order.popitem()
print(f"Removed last item: {last_item}")

extra_spices = {"cardamom": "crushed", "ginger": 'sliced'}
chai_recepie.update(extra_spices)

print(f"Updated Chai recepie: {chai_recepie}")

chai_size = chai_order['size']
print(f"Chai size is: {chai_size}")