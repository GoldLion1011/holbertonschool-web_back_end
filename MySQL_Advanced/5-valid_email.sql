-- task 5: Trigger that resets attr valid_email if attr email is changed
DELIMITER //
CREATE TRIGGER reset_valid_email AFTER UPDATE ON users
FOR EACH ROW
BEGIN
    IF NEW.email != OLD.email THEN
        SET NEW.valid_email = 0;
    END IF;
END//
DELIMITER ;

