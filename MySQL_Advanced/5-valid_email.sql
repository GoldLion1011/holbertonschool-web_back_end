-- task 5: Trigger that resets attr valid_email if attr email is changed
DELIMITER //
CREATE TRIGGER validate_email 
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    IF OLD.email != NEW.email THEN
        SET NEW.valid_email = 0;
    END IF;
END;
//
DELIMITER ;
