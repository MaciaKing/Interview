# Interview

Api elegida: Marvel
Hecha hasta el nivel 4
web responsive
Versiones de lenguages:
- Python 3.9.12
- PHP 8.2.3


Este proyecto esta hecho con:

  - Backend:
      - 1) Python. This code uses two Python files to connect to the Marvel API and store the information obtained in a database. The first file, database.py, is a class that connects to the database and provides methods to insert data and optimize performance.

The second file, marvel_api.py, is responsible for obtaining the Marvel character information through the Marvel API and storing it in the database using the methods provided by the database.py class. This file initializes the process of extracting data from Marvel heroes and stores it in the database for later use.
      
      
      - 2) Postgres. The database will contain a single table called "hero", which will store information about Marvel characters. The table will have several fields, including "name" for the character's name, "photo" to store an image of the character, "description" to describe the character's abilities or characteristics, "comic book appearances" for the number of comic books in which the character has appeared, and "series appearances" for the number of television series in which the character has appeared. Also, each character will have a unique identifier. To view the creation file click here.
      
      A user with a password will also be created and given access to the application to work with it (macia, macia).
      
      - 3) PHP. This code handles requests from our web application through two PHP files. One of them, database.php, contains a class that connects to the database and has a method to execute queries. The other file, receiver.php, receives requests from our web application and creates a database object to perform a query.
      
  - Front-End:
      - 1) Bootstrap. To make sure that my website has an attractive appearance and is compatible with mobile devices, I used the Bootstrap framework.
      
      
      - 2) Jquery. To access the elements (divs) in my HTML file dynamically and make changes to them without having to reload the page, I used the jQuery JavaScript library.
      
      
      - 3) Ajax. To allow my website to interact with the server asynchronously, I have used AJAX. AJAX is a technique that allows me to send and receive data in the background without having to reload the page.
      
      
      - 4) Datatables. To give users a more dynamic and interactive experience and allow them to search and sort data in a table, I used a JavaScript library called DataTables. DataTables is a data visualization tool that allows me to add interactivity to static HTML tables. With DataTables, I can add functions such as pagination, searching and sorting of data with just a few lines of code.
      
      
 This is how it looks: 
 
 
 <img width="1498" alt="Captura de pantalla 2023-02-21 a las 15 07 50" src="https://user-images.githubusercontent.com/51322831/220374971-e6d9b14f-b4f8-4443-ae31-023515f98254.png">
 
 
<img width="1506" alt="Captura de pantalla 2023-02-21 a las 15 07 39" src="https://user-images.githubusercontent.com/51322831/220375024-4278c6a3-0ee7-4b37-a88e-5d85eb9f8430.png">

Searching A- hero

<img width="1511" alt="Captura de pantalla 2023-02-21 a las 15 06 45" src="https://user-images.githubusercontent.com/51322831/220375062-f05e27c7-d55e-40b3-a0f3-a241c6dc42e5.png">


<img width="1510" alt="Captura de pantalla 2023-02-21 a las 15 06 24" src="https://user-images.githubusercontent.com/51322831/220375094-fa42e17a-d78a-4ea4-93c0-773eb5b9cf75.png">


