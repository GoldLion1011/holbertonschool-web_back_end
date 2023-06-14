-- task 4: Create a trigger that decreases the quantity of an item after inserting a new order.
CREATE TRIGGER decrease_quantity AFTER INSERT ON orders
FOR EACH ROW
    UPDATE items
    SET quantity = quantity - NEW.number
    WHERE name = NEW.item_name;
