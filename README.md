# Library-Management-System
Sure, let's break down the function of the library management system web application.

1. Home Page (/): 
   - This is the landing page of the web application. It displays the title "Library Management System" and provides navigation links to different sections of the application.
   - It includes a link to the "Home" section,"search""ADD book" section, "view book" section which essentially refreshes the home page.

2. View Books Page (/view): 
   - This page displays a list of books stored in the database.
   - It retrieves book data from the database and renders it in a table format.
   - Each book entry includes details such as Book ID, Book Name, Author, Quantity, and three action buttons: Borrow, return and "Delete".
   - Clicking the "borrow" button for a particular book, it means it lends to the others.
   - Clicking the "return" button for a particular book, it means it returns to the library from the borrower.
   - Clicking the "Delete" button removes the corresponding book entry from the database.


3. Delete Book Functionality (/delete): 
   - This functionality handles the deletion of a book entry from the database.
   - It is triggered when a user clicks the "Delete" button next to a book entry on the View Books page.
   - Upon deletion, the application removes the corresponding record from the database and redirects the user back to the View Books page.

4. Search Book Functionality (/search): 
   - The search_books function handles search queries submitted via the search form.
   - It retrieves books from the database based on the search query (matching book name or author).
   - The search results are then passed to the view_books.html template for rendering.
   - The search functionality allows users to find books based on their titles or authors.
   - If no search query is provided, the function redirects back to the View Books page to display all books.

5. Add Book Functionality (/add):
   - The /add_book route handles POST requests sent from the Add Book form.
   - When the form is submitted, the data is extracted from the form fields (book name, author, and quantity).
   - The data is then inserted into the SQLite database using an SQL INSERT statement.
   - After adding the book, the user is redirected to the View Books page to see the updated list of books


Overall, the web application serves as a basic library management system where users can view the list of books, update their details, and delete books as needed. It utilizes Flask for the backend logic, SQLite for data storage, and HTML/CSS for the user interface.
