**creating the database**



use database\_name

ex:

use students -------------creates database students if the database doesn't exists if exists students data base will be used



**To display all the collections in the databse**



show collections



**To drop the collections**



db.deparments.drop(); -----------------departments collection will dropped in present database



**inserting one record into the collection students**



&#x20;db.students.insertOne({id:1,name:'vishnu',age:20,dept:'CSE',marks:80,city:'Hyderabad'}





**Inserting the multiple records into the collection students**



db.students.insertMany(\[

&#x20;   { id: 2, name: "Ravi", age: 20, dept: "CSE", marks: 85, city: "Hyderabad" },

&#x20;   { id: 3, name: "Arjun", age: 21, dept: "ECE", marks: 78, city: "Bangalore" },

&#x20;   { id: 4, name: "Priya", age: 20, dept: "CSE", marks: 92, city: "Chennai" },

&#x20;   { id: 5, name: "Sneha", age: 22, dept: "IT", marks: 88, city: "Hyderabad" },

&#x20;   { id: 6, name: "Kiran", age: 21, dept: "CSE", marks: 76, city: "Mumbai" },

&#x20;   { id: 7, name: "Anjali", age: 19, dept: "IT", marks: 95, city: "Pune" },

&#x20;   { id: 8, name: "Rahul", age: 22, dept: "ECE", marks: 69, city: "Delhi" },

&#x20;   { id: 9, name: "Divya", age: 20, dept: "CSE", marks: 84, city: "Hyderabad" },

&#x20;   { id: 10, name: "Vikram", age: 23, dept: "MECH", marks: 73, city: "Bangalore" },

&#x20;   { id: 11, name: "Neha", age: 21, dept: "IT", marks: 89, city: "Chennai" },

&#x20;   { id: 12, name: "Suresh", age: 20, dept: "CSE", marks: 81, city: "Mumbai" },

&#x20;   { id: 13, name: "Pooja", age: 22, dept: "ECE", marks: 91, city: "Hyderabad" },

&#x20;   { id: 14, name: "Aman", age: 19, dept: "IT", marks: 67, city: "Delhi" },

&#x20;   { id: 15, name: "Lakshmi", age: 21, dept: "CSE", marks: 87, city: "Vijayawada" },

&#x20;   { id: 16, name: "Rohit", age: 23, dept: "ECE", marks: 74, city: "Pune" },

&#x20;   { id: 17, name: "Meena", age: 20, dept: "IT", marks: 93, city: "Hyderabad" },

&#x20;   { id: 18, name: "Tarun", age: 22, dept: "CSE", marks: 79, city: "Bangalore" },

&#x20;   { id: 19, name: "Swathi", age: 21, dept: "ECE", marks: 86, city: "Chennai" },

&#x20;   { id: 20, name: "Naveen", age: 20, dept: "IT", marks: 71, city: "Hyderabad" },

&#x20;   { id: 21, name: "Keerthi", age: 19, dept: "CSE", marks: 90, city: "Vijayawada" }

])



**3. Display all students belonging to the CSE department.**



db.students.find({dept:'CSE'})



**4. Display all students whose city is Hyderabad**



db.students.find({city:'Hyderabad'})



**5. Find the student named Aarav.**



db.students.findOne({name:'Aarav'})



**6. Find all students whose marks are greater than 80.**



db.students.findOne({marks:{$gt:80}})



**7. Find students whose age is greater than 20 and less than 23**



db.students.find({age: {$gt: 20,$lt: 23}})



**8. Find students who belong to CSE and are from Hyderabad.**



db.students.find({city:"Hyderabad",dept:"CSE"})



**9. Display only student name and marks. Do not display \_id.**



db.students.find({},{name:1,marks:1,\_id:0})



**10. Find students belonging to either CSE or ECE.**



db.students.find({dept:{$in:\['CSE','ECE']}})



**11. Find students who have Python as one of their skills.**





db.students.find({skills:"Python"})



**12. Find students who have both Python and SQL in their skills.**



db.students.find({skills:{$in:\["Python","SQL"]}})



**13. Find students whose paid fees are less than ■40,000 using fees.paid.**



db.students.find({fees.paid:{$gt:40000}})



**14. Display the top 3 students based on marks, highest to lowest.**



db.students.find().sort({marks:-1}).limit(3)



**15. Display all unique cities represented in the students collection.**



db.students.distinct("city")



**16. Update Meera's marks to 70.**



db.students.updateOne({name:"Meera"},{$set:{marks:70}})



**17. Give 5 additional marks to all CSE students.**



db.students.updateMany({dept:'CSE'},{$inc:{marks:5}})



**18. Add "git" to the skills of all CSE students without creating duplicates.**





db.students.updateMany({dept:"CSE"},{$addToSet:{skills:"git"}})



**19. Increase fees.total by ■2,000 for all ECE students.**



db.students.updateMany({dept:'ECE'},{$inc:{'fees.total':2000}})



**20. Delete all students whose marks are below 60. Verify the filter first.**



db.students.deleteMany({marks:{$lt:60}})



**21. Find the average marks for each department.**



db.students.aggregate(\[{$group:{\_id:'$dept',average\_marks:{$avg:'$marks'}}}])



**22. Display each department with its number of students, sorted by count descending.**



db.students.aggregate(\[{ $group: { \_id: "$dept", studentCount: { $sum: 1 } } }, { $sort: { studentCount: -1 } }])



**23. Calculate pendingFees = fees.total - fees.paid for every student and sort by pending fees highest first.**



db.students.aggregate(\[{ $project: { name: 1, pendingFees: { $subtract: \["$fees.total", "$fees.paid"] } } }, { $sort: { pendingFees: -1 } }])





**24. Find the top 3 most common skills among all students.**



db.students.aggregate(\[{ $unwind: "$skills" }, { $group: { \_id: "$skills", count: { $sum: 1 } } }, { $sort: { count: -1 } }, { $limit: 3 }])



**25. Join students with departments and display Student Name, Department, and HOD.**



db.students.aggregate(\[{ $lookup: { from: "departments", localField: "department", foreignField: "department", as: "dept" } }, { $unwind: "$dept" }, { $project: { \_id: 0, StudentName: "$name", Department: "$department", HOD: "$dept.HOD" } }])

