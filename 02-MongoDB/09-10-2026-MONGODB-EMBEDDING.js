// USE CASE 1: EMBEDDING

db.orders.insertOne({
    order_id: 1001,

    customer: {
        customer_id: 501,
        customer_name: "Rohit Sharma",
        email: "rohit@gmail.com"
    },

    products: [
        {
            product_id: 101,
            product_name: "Laptop",
            price: 55000,
            quantity: 1
        },
        {
            product_id: 102,
            product_name: "Mouse",
            price: 1000,
            quantity: 2
        }
    ],

    total_amount: 57000,
    order_status: "Delivered"
});


db.orders.find();




// USE CASE 2: EMBEDDING

db.patients.insertOne({
    patient_id: 1001,
    patient_name: "Arun Kumar",
    age: 35,
    gender: "Male",

    contact: {
        phone: "9876543210",
        city: "Nellore"
    },

    medical_history: [
        {
            visit_date: "2026-09-15",
            disease: "Fever",
            doctor: "Dr. Ravi",
            treatment: "Medication"
        },
        {
            visit_date: "2026-10-05",
            disease: "Cold",
            doctor: "Dr. Priya",
            treatment: "Tablets"
        }
    ]
});

db.patients.find();



