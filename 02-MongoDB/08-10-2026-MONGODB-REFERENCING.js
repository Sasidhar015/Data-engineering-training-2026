// USE CASE 1: REFERENCING

db.courses.insertMany([
    {
        course_id: 101,
        course_name: "Data Engineering",
        trainer: "Mr. Kumar"
    },
    {
        course_id: 102,
        course_name: "MongoDB",
        trainer: "Ms. Priya"
    },
    {
        course_id: 103,
        course_name: "Python",
        trainer: "Mr. Raj"
    }
]);

db.students.insertMany([
    {
        student_id: 501,
        student_name: "Rohit Sharma",
        course_ids: [101, 102]
    },
    {
        student_id: 502,
        student_name: "Rahul Kumar",
        course_ids: [102, 103]
    }
]);


db.students.find();

db.courses.find();





// USE CASE 2: REFERENCING

db.categories.insertMany([
    {
        category_id: 101,
        category_name: "Electronics"
    },
    {
        category_id: 102,
        category_name: "Clothing"
    },
    {
        category_id: 103,
        category_name: "Books"
    }
]);

db.products.insertMany([
    {
        product_id: 1001,
        product_name: "Laptop",
        price: 55000,
        category_id: 101
    },

    {
        product_id: 1002,
        product_name: "Smartphone",
        price: 30000,
        category_id: 101
    },

    {
        product_id: 1003,
        product_name: "T-Shirt",
        price: 999,
        category_id: 102
    },

    {
        product_id: 1004,
        product_name: "Java Programming",
        price: 799,
        category_id: 103
    }
]);

db.categories.find();

db.products.find();
