-- task 4: Create a trigger that decreases the quantity of an item after inserting a new order.
DELIMITER //
CREATE TRIGGER update_item_quantity
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    UPDATE items
    SET quantity = quantity - NEW.quantity
    WHERE item_id = NEW.item_id;
END//
DELIMITER ;

