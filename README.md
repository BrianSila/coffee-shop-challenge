# ☕ Coffee Shop OOP System

A Python implementation demonstrating object-oriented programming principles with Customer, Coffee, and Order models.

## Core Models

### `Customer`
- **Properties**: `name` (string, 1-15 chars)
- **Relationships**:
  - `orders()`: Returns all orders
  - `coffees()`: Returns unique coffees ordered
- **Methods**:
  - `create_order(coffee, price)`: Creates new Order

### `Coffee` 
- **Properties**: `name` (string, ≥3 chars, immutable)
- **Relationships**:
  - `orders()`: All orders for this coffee
  - `customers()`: Unique customers who ordered
- **Analytics**:
  - `num_orders()`: Total order count
  - `average_price()`: Mean order price

### `Order`
- **Properties**:
  - `customer` (Customer instance)
  - `coffee` (Coffee instance) 
  - `price` (float, 1.0-10.0, immutable)

## Key Features

✅ Strict type validation  
✅ Immutable properties enforcement  
✅ Automatic relationship management  
✅ Circular import prevention  
✅ Complete test coverage  

## Usage Example

```python
from models import Customer, Coffee

# Create instances
customer = Customer("Sarah")
coffee = Coffee("Latte")

# Create order
order = customer.create_order(coffee, 4.75)

# Access relationships
print(f"{customer.name} ordered {coffee.name}")
print(f"Total orders: {coffee.num_orders()}")
