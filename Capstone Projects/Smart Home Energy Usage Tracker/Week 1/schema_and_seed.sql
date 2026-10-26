CREATE DATABASE IF NOT EXISTS smart_home_energy;
USE smart_home_energy;

DROP TABLE IF EXISTS energy_logs;
DROP TABLE IF EXISTS devices;
DROP TABLE IF EXISTS rooms;

CREATE TABLE rooms (
    room_id    VARCHAR(5)  PRIMARY KEY,
    room_name  VARCHAR(50) NOT NULL,
    floor      TINYINT     NOT NULL DEFAULT 0);

CREATE TABLE devices (
    device_id      VARCHAR(5)  PRIMARY KEY,
    device_name    VARCHAR(80) NOT NULL,
    device_type    VARCHAR(40) NOT NULL,
    room_id        VARCHAR(5)  NOT NULL,
    rated_watts    INT         NOT NULL,
    status         ENUM('ON','OFF') NOT NULL DEFAULT 'OFF',
    installed_date DATE,
    CONSTRAINT fk_device_room FOREIGN KEY (room_id) REFERENCES rooms(room_id));

CREATE TABLE energy_logs (
    log_id      BIGINT AUTO_INCREMENT PRIMARY KEY,
    device_id   VARCHAR(5)    NOT NULL,
    logged_at   DATETIME      NOT NULL,
    energy_kwh  DECIMAL(8,4)  NOT NULL,
    power_watts DECIMAL(8,1),
    CONSTRAINT fk_log_device FOREIGN KEY (device_id) REFERENCES devices(device_id),
    INDEX idx_logs_device_time (device_id, logged_at),
    INDEX idx_logs_time (logged_at));

INSERT INTO rooms VALUES
 ('R01','Living Room',0),('R02','Bedroom 1',1),('R03','Bedroom 2',1),
 ('R04','Kitchen',0),('R05','Bathroom',0),('R06','Home Office',1);

INSERT INTO devices VALUES
 ('D01','Living Room AC','air_conditioner','R01',1200,'ON','2025-01-15'),
 ('D02','Living Room TV','television','R01',120,'ON','2025-01-15'),
 ('D03','Living Room Fan','fan','R01',70,'ON','2025-01-15'),
 ('D04','Bedroom 1 AC','air_conditioner','R02',1100,'ON','2025-01-15'),
 ('D05','Bedroom 1 Light','light','R02',20,'ON','2025-01-15'),
 ('D06','Bedroom 2 Fan','fan','R03',70,'ON','2025-01-15'),
 ('D07','Bedroom 2 Light','light','R03',15,'ON','2025-01-15'),
 ('D08','Refrigerator','refrigerator','R04',150,'ON','2025-01-15'),
 ('D09','Microwave','microwave','R04',1000,'OFF','2025-01-15'),
 ('D10','Kitchen Light','light','R04',25,'ON','2025-01-15'),
 ('D11','Water Heater','water_heater','R05',2000,'ON','2025-01-15'),
 ('D12','Office Laptop Charger','charger','R06',65,'ON','2025-01-15'),
 ('D13','Office Monitor','monitor','R06',40,'ON','2025-01-15'),
 ('D14','Washing Machine','washing_machine','R05',500,'OFF','2025-01-15');
