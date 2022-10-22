***QaaS***

**Description**
----
The app for build & host quizzes (simple multiple-choice with questions and answers)

**Endpoints**
----

**/answer**
----
  Get list of all answers, create new answer

* **Method:**

  `GET` | `POST`

   **Data Params**  
{  
"name":"name",  
"creator":"user_id"  
}

**/answer/\<int:answer_id\>** 
----
  Get single answer by id, update answer, remove answer

* **Method:**

  `GET` | `PUT` | `DELETE`

   **Data Params**  
{  
"name":"name",  
"creator":"user_id"  
}  

**/assignee**
----
  get all quizzes assigned to the current user, add new assignment to the current user

* **Method:**

  `GET` | `POST`

* **Data Params**  
{    
"quiz":"quiz_id"  
} 

**/assignee/\<int:quiz_id\>** 
----
  delete the quiz assigned to the current user by quiz_id

* **Method:**

  `DELETE` 

**/email**
----
  send an email

* **Method:**

  `POST`

   **Data Params**  
{  
"subject" = "subject"  
"message" = "message"  
"from_email" = "from_email"  
}

**/progress/\<int:quiz_id\>**
----
  check the proggres of a quiz by quiz_id

* **Method:**

  `GET`

**/question**
----
  Get list of all questions, create new question

* **Method:**

  `GET` | `POST`

   **Data Params**  
{  
"text":"text",  
"quiz":"quiz_id"  
}

**/question/\<int:question_id\>** 
----
  Get single question by id, update question, remove question

* **Method:**

  `GET` | `PUT` | `DELETE`

   **Data Params**  
{  
"text":"text",  
"quiz":"quiz_id"  
} 

**/question/\<int:question_id\>/result** 
----
  Get result of a question by id, delete result

* **Method:**

  `GET` | `DELETE`
  
**/quiz**
----
  Get list of all quizzes of current user, create new quiz

* **Method:**

  `GET` | `POST`

   **Data Params**  
{  
"name":"name",  
"creator":"user_id"  
}

**/quiz/\<int:quiz_id\>** 
----
  Get single quiz by id, update quiz, remove quiz

* **Method:**

  `GET` | `PUT` | `DELETE`

   **Data Params**  
{  
"name":"name",  
"creator":"user_id"  
}  

**/quiz/\<int:quiz_id\>/result** 
----
  Get result of a quiz by id, add results

* **Method:**

  `GET` | `POST`

* **Data Params**  
[
{  
"answer": "answer_id",  
"user": "user_id"  
},..]

**/quiz/all**
----
  Get list of all quizzes

* **Method:**

  `GET` 