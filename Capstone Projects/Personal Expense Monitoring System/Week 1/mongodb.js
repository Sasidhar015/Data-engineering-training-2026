use("expense_db");
db.receipts.drop();

db.receipts.insertMany([
  { receipt_id: "RCP-0001", user_id: 1, expense_id: 1,
    store: "FreshMart", receipt_date: ISODate("2026-04-03"),
    items: [
      { name: "Rice 5kg", qty: 1, price: 28.0 },
      { name: "Milk 1L",  qty: 4, price: 1.5 },
      { name: "Vegetables", qty: 1, price: 20.0 }],
    total: 54.0, payment_method: "UPI",
    notes: "Weekly groceries, used coupon",
    scan: { file: "receipts/rcp0001.jpg", ocr_confidence: 0.94 },
    tags: ["groceries", "weekly"] },
  { receipt_id: "RCP-0002", user_id: 1, expense_id: 3,
    store: "Spice Garden", receipt_date: ISODate("2026-04-09"),
    items: [{ name: "Dinner combo", qty: 2, price: 16.0 }],
    total: 32.0, payment_method: "Credit Card",
    notes: "Birthday dinner",
    scan: { file: "receipts/rcp0002.jpg", ocr_confidence: 0.88 },
    tags: ["dining", "special"]},
  { receipt_id: "RCP-0003", user_id: 2, expense_id: 4,
    store: "City Cabs", receipt_date: ISODate("2026-04-04"),
    items: [{ name: "Airport ride", qty: 1, price: 18.75 }],
    total: 18.75, payment_method: "UPI",
    notes: "Reimbursable by office",
    scan: { file: "receipts/rcp0003.jpg", ocr_confidence: 0.91 },
    tags: ["transport", "reimbursable"]}]);

db.receipts.createIndex({ receipt_id: 1 }, { unique: true });
db.receipts.createIndex({ user_id: 1, receipt_date: -1 });
db.receipts.createIndex({ expense_id: 1 });
db.receipts.createIndex({ notes: "text", store: "text" });

printjson(db.receipts.getIndexes());
printjson(db.receipts.find({ user_id: 1 }).sort({ receipt_date: -1 }).toArray());
printjson(db.receipts.find({ $text: { $search: "dinner" } }).toArray());
printjson(db.receipts.find({ user_id: 1 }).explain("executionStats").executionStats.totalDocsExamined);
