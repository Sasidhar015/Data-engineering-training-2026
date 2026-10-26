USE smart_home_energy;


INSERT INTO devices (device_id, device_name, device_type, room_id, rated_watts, status, installed_date)
VALUES ('D15', 'Smart Speaker', 'speaker', 'R01', 10, 'ON', CURDATE());

INSERT INTO energy_logs (device_id, logged_at, energy_kwh, power_watts)
VALUES ('D15', '2026-09-02 10:00:00', 0.0100, 10.0);


SELECT d.device_id, d.device_name, r.room_name, d.status
FROM devices d JOIN rooms r ON r.room_id = d.room_id
ORDER BY r.room_name;

SELECT * FROM energy_logs WHERE device_id = 'D01' AND DATE(logged_at) = '2026-09-01' LIMIT 24;


UPDATE devices SET status = 'OFF' WHERE device_id = 'D09';
UPDATE energy_logs SET energy_kwh = 0.0120, power_watts = 12.0
WHERE device_id = 'D15' AND logged_at = '2026-09-02 10:00:00';


DELETE FROM energy_logs WHERE device_id = 'D15';
DELETE FROM devices     WHERE device_id = 'D15';


DROP PROCEDURE IF EXISTS sp_update_device_status;
DROP PROCEDURE IF EXISTS sp_room_energy_per_day;

DELIMITER $$
CREATE PROCEDURE sp_update_device_status(IN p_device_id VARCHAR(5), IN p_status VARCHAR(3))
BEGIN
    UPDATE devices SET status = p_status WHERE device_id = p_device_id;
    SELECT device_id, device_name, status FROM devices WHERE device_id = p_device_id;
END$$


CREATE PROCEDURE sp_room_energy_per_day(IN p_date DATE)
BEGIN
    SELECT r.room_id,
           r.room_name,
           DATE(l.logged_at)          AS usage_date,
           ROUND(SUM(l.energy_kwh),3) AS total_kwh
    FROM energy_logs l
    JOIN devices d ON d.device_id = l.device_id
    JOIN rooms   r ON r.room_id   = d.room_id
    WHERE p_date IS NULL OR DATE(l.logged_at) = p_date
    GROUP BY r.room_id, r.room_name, DATE(l.logged_at)
    ORDER BY usage_date, total_kwh DESC;
END$$
DELIMITER ;

CALL sp_update_device_status('D14', 'ON');
CALL sp_room_energy_per_day('2026-09-01');
CALL sp_room_energy_per_day(NULL);
