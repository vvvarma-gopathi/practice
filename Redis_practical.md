**1.Create a student name key with a TTL of 60 seconds and verify the TTL.** 



SET student:name "varma" ex 60

TTL student:name

\----shows the remaining Time To Live in integer



**2. Create a student Hash with name, email, and course.**



HSET student:1 name 'varma' email 'varma23@gmail.com' course 'python fullstack'



**3. Create a Set of student skills and verify duplicate values are not stored.**



SADD skills 'redis' 'fast api' 'python'



**4. Create a Sorted Set leaderboard and display members from highest score to lowest.**



ZADD leaderboard 90 'varma' 96 'mohan' 60 'aparna' 70 'aakash'



\---- creates a sorted set named leaderboard 



ZREVRANGE leaderboard 0 -1 WITHSCORES



**5. Create a Pub/Sub notification channel and test one publisher with one subscriber.**



SUBSCRIBE notifications

\---subscribes to the notification channel and wait for the messages from publisher



PUBLISH notifications 'New student registered'

\-----publishes the message to the notifications subscriber receives the message



**6. Implement a simple Cache-Aside flow for GET /products/{id} using Redis.**



SET product:1 "LAPTOP,50000" ex 60

\-------product 1 is created with the expiry of 60 sec

GET product:1

\-------product 1 is displayed 

TTL product:1

\-------remaining Time To Live displayed



**7. Explain how Redis can prevent duplicate payment processing.** 



Redis can prevent duplicate payment processing by using a unique transaction ID as a key.



When a payment request comes, check whether the transaction ID already exists.

If it exists, reject it as a duplicate.

If it doesn’t exist, store the ID in Redis and process the payment.

SET payment:TXN123 "processed" NX EX 3600



NX ensures the key is created only if it doesn't already exist, preventing the same payment from being processed twice.



