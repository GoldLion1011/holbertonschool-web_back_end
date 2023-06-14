-- task 4: Create a trigger that decreases the quantity of an item after inserting a new order.
DELIMITER //
CREATE TRIGGER decrease_quantity AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    UPDATE items
    SET quantity = quantity - (SELECT SUM(number) FROM orders WHERE item_name = NEW.item_name)
    WHERE name = NEW.item_name;
END//
DELIMITER ;
