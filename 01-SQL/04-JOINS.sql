-- 1. CREATE DATABASE
CREATE DATABASE hospital_lab;
USE hospital_lab;

-- 2. CREATE PATIENTS TABLE
CREATE TABLE patients (
    patient_id INT PRIMARY KEY,
    patient_name VARCHAR(100),
    age INT,
    city VARCHAR(50)
);

-- 3. INSERT PATIENT DATA
INSERT INTO patients VALUES
(1, 'Rohan Das', 34, 'Hyderabad'),
(2, 'Meena Iyer', 46, 'Chennai'),
(3, 'Kabir Khan', 29, 'Hyderabad'),
(4, 'Lakshmi Rao', 61, 'Bangalore'),
(5, 'John Mathew', 38, 'Mumbai'),
(6, 'Ayesha Ali', 25, NULL),
(7, 'Naveen Reddy', 52, 'Pune');


-- 4. CREATE DOCTORS TABLE
CREATE TABLE doctors (
    doctor_id INT PRIMARY KEY,
    doctor_name VARCHAR(100),
    specialization VARCHAR(50),
    consultation_fee DECIMAL(10,2)
);


-- 5. INSERT DOCTOR DATA
INSERT INTO doctors VALUES
(101, 'Dr. Sharma', 'Cardiology', 1200),
(102, 'Dr. Farah', 'Dermatology', 800),
(103, 'Dr. Joseph', 'Orthopedics', 1000),
(104, 'Dr. Mehta', 'General Medicine', 600),
(105, 'Dr. Sana', 'Neurology', 1500),
(106, 'Dr. Rao', 'Pediatrics', 700);


-- 6. CREATE APPOINTMENTS TABLE
CREATE TABLE appointments (
    appointment_id INT PRIMARY KEY,
    patient_id INT,
    doctor_id INT,
    appointment_date DATE,
    status VARCHAR(30)
);


-- 7. INSERT APPOINTMENT DATA
INSERT INTO appointments VALUES
(1001, 1, 101, '2026-10-01', 'Completed'),
(1002, 2, 104, '2026-10-01', 'Completed'),
(1003, 3, 102, '2026-10-02', 'Cancelled'),
(1004, 1, 105, '2026-10-03', 'Completed'),
(1005, 4, 101, '2026-10-03', 'Scheduled'),
(1006, 5, 103, '2026-10-04', 'Completed'),
(1007, 3, 104, '2026-10-04', 'Completed'),
(1008, NULL, 102, '2026-10-05', 'Scheduled'),
(1009, 20, 103, '2026-10-05', 'Completed'),
(1010, 2, NULL, '2026-10-06', 'Scheduled');


-- VIEW TABLE DATA
SELECT * FROM patients;

SELECT * FROM doctors;

SELECT * FROM appointments;









-- Q1. Appointment ID, patient name, doctor name and appointment date
SELECT
    a.appointment_id,
    p.patient_name,
    d.doctor_name,
    a.appointment_date
FROM appointments a
INNER JOIN patients p
    ON a.patient_id = p.patient_id
INNER JOIN doctors d
    ON a.doctor_id = d.doctor_id;



-- Q2. Doctor and specialization for completed appointments
SELECT
    d.doctor_name,
    d.specialization
FROM appointments a
INNER JOIN doctors d
    ON a.doctor_id = d.doctor_id
WHERE a.status = 'Completed';


-- Q3. Appointments made by Hyderabad patients
SELECT
    a.appointment_id,
    p.patient_name,
    p.city,
    a.appointment_date
FROM appointments a
INNER JOIN patients p
    ON a.patient_id = p.patient_id
WHERE p.city = 'Hyderabad';


-- Q4. Every patient with appointment details, including patients who never booked
SELECT
    p.patient_id,
    p.patient_name,
    a.appointment_id,
    a.appointment_date,
    a.status
FROM patients p
LEFT JOIN appointments a
    ON p.patient_id = a.patient_id;


-- Q5. Patients who never booked an appointment
SELECT
    p.patient_id,
    p.patient_name
FROM patients p
LEFT JOIN appointments a
    ON p.patient_id = a.patient_id
WHERE a.appointment_id IS NULL;


-- Q6. Every doctor with appointments, including doctors with no appointments
SELECT
    d.doctor_id,
    d.doctor_name,
    a.appointment_id,
    a.appointment_date,
    a.status
FROM doctors d
LEFT JOIN appointments a
    ON d.doctor_id = a.doctor_id;


-- Q7. Doctors with no appointments
SELECT
    d.doctor_id,
    d.doctor_name
FROM doctors d
LEFT JOIN appointments a
    ON d.doctor_id = a.doctor_id
WHERE a.appointment_id IS NULL;


-- Q8. Appointment records where a valid patient cannot be found
SELECT
    a.appointment_id,
    a.patient_id,
    a.doctor_id,
    a.appointment_date,
    a.status
FROM appointments a
LEFT JOIN patients p
    ON a.patient_id = p.patient_id
WHERE p.patient_id IS NULL;



-- Q9. Appointment records where doctor is not assigned
SELECT
    a.appointment_id,
    a.patient_id,
    a.doctor_id,
    a.appointment_date,
    a.status
FROM appointments a
LEFT JOIN doctors d
    ON d.doctor_id = a.doctor_id
WHERE a.doctor_id IS NULL;



-- Q10. Patient name, doctor name, specialization, fee and status for all valid appointments
SELECT
    p.patient_name,
    d.doctor_name,
    d.specialization,
    d.consultation_fee,
    a.status
FROM appointments a
INNER JOIN patients p
    ON a.patient_id = p.patient_id
INNER JOIN doctors d
    ON a.doctor_id = d.doctor_id;

-- Q11. Number of appointments per doctor
SELECT
    d.doctor_id,
    d.doctor_name,
    COUNT(a.appointment_id) AS appointment_count
FROM doctors d
LEFT JOIN appointments a
    ON d.doctor_id = a.doctor_id
GROUP BY
    d.doctor_id,
    d.doctor_name;



-- Q12. Total consultation value per doctor for completed appointments
SELECT
    d.doctor_name,
    SUM(d.consultation_fee) AS total_consultation_value
FROM appointments a
INNER JOIN doctors d
    ON a.doctor_id = d.doctor_id
WHERE a.status = 'Completed'
GROUP BY d.doctor_name;


-- Q13. Doctors with more than 1 appointment
SELECT
    d.doctor_name,
    COUNT(a.appointment_id) AS appointment_count
FROM doctors d
INNER JOIN appointments a
    ON d.doctor_id = a.doctor_id
GROUP BY d.doctor_name
HAVING COUNT(a.appointment_id) > 1;


-- Q14. Specialization with the highest total consultation value
SELECT 
    d.specialization,
    SUM(d.consultation_fee) AS total_consultation_value
FROM appointments a
INNER JOIN doctors d
    ON a.doctor_id = d.doctor_id
GROUP BY d.specialization
ORDER BY total_consultation_value DESC
LIMIT 1;

-- Q15. Every patient with number of appointments, including zero
SELECT
    p.patient_id,
    p.patient_name,
    COUNT(a.appointment_id) AS appointment_count
FROM patients p
LEFT JOIN appointments a
    ON p.patient_id = a.patient_id
GROUP BY
    p.patient_id,
    p.patient_name;


-- Q16. Patients who consulted more than 1 doctor
SELECT
    p.patient_id,
    p.patient_name,
    COUNT(DISTINCT a.doctor_id) AS doctor_count
FROM patients p
INNER JOIN appointments a
    ON p.patient_id = a.patient_id
WHERE a.doctor_id IS NOT NULL
GROUP BY
    p.patient_id,
    p.patient_name
HAVING COUNT(DISTINCT a.doctor_id) > 1;


-- Q17. Patients who visited a Cardiology doctor
SELECT DISTINCT
    p.patient_name
FROM patients p
INNER JOIN appointments a
    ON p.patient_id = a.patient_id
INNER JOIN doctors d
    ON a.doctor_id = d.doctor_id
WHERE d.specialization = 'Cardiology';



-- Q18. Appointments where consultation fee is greater than 900
SELECT
    a.appointment_id,
    p.patient_name,
    d.doctor_name,
    d.consultation_fee,
    a.status
FROM appointments a
INNER JOIN patients p
    ON a.patient_id = p.patient_id
INNER JOIN doctors d
    ON a.doctor_id = d.doctor_id
WHERE d.consultation_fee > 900;



-- Q19. Average consultation fee of doctors involved in completed appointments
SELECT
    AVG(d.consultation_fee) AS average_consultation_fee
FROM appointments a
INNER JOIN doctors d
    ON a.doctor_id = d.doctor_id
WHERE a.status = 'Completed';


-- Q20. Doctor with the highest number of completed appointments
SELECT 
    d.doctor_id,
    d.doctor_name,
    COUNT(a.appointment_id) AS completed_appointments
FROM doctors d
INNER JOIN appointments a
    ON d.doctor_id = a.doctor_id
WHERE a.status = 'Completed'
GROUP BY
    d.doctor_id,
    d.doctor_name
ORDER BY completed_appointments DESC
LIMIT 1;
