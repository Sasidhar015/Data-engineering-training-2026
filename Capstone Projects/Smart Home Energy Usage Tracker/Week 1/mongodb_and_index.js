use("smart_home_energy");

db.sensor_logs.drop();

db.sensor_logs.insertMany([
  { device_id: "D01", room_id: "R01", timestamp: "2026-09-01 18:00:00", energy_kwh: 1.12, power_watts: 1120.0, voltage: 231.4, signal_strength: -52 },
  { device_id: "D01", room_id: "R01", timestamp: "2026-09-01 19:00:00", energy_kwh: 1.05, power_watts: 1050.0, voltage: 230.1, signal_strength: -55 },
  { device_id: "D02", room_id: "R01", timestamp: "2026-09-01 19:00:00", energy_kwh: 0.12, power_watts: 120.0,  voltage: 229.8, signal_strength: -48 },
  { device_id: "D08", room_id: "R04", timestamp: "2026-09-01 19:00:00", energy_kwh: 0.06, power_watts: 60.0,   voltage: 232.0, signal_strength: -60 },
  { device_id: "D11", room_id: "R05", timestamp: "2026-09-01 06:00:00", energy_kwh: 1.95, power_watts: 1950.0, voltage: 233.5, signal_strength: -45 },
  { device_id: "D13", room_id: "R06", timestamp: "2026-09-01 10:00:00", energy_kwh: 0.04, power_watts: 40.0,   voltage: 230.9, signal_strength: -50 }]);


db.sensor_logs.createIndex({ device_id: 1 });
db.sensor_logs.createIndex({ timestamp: 1 });
db.sensor_logs.createIndex({ device_id: 1, timestamp: -1 });  


printjson(db.sensor_logs.getIndexes());
printjson(db.sensor_logs.find({ device_id: "D01" }).sort({ timestamp: -1 }).limit(2).toArray());
printjson(db.sensor_logs.find({ timestamp: { $gte: "2026-09-01 18:00:00" } }).explain("executionStats").executionStats.totalDocsExamined);
