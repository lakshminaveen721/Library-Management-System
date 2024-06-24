from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Database setup
DATABASE = 'library.db'

def create_table():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            quantity INTEGER NOT NULL
        )
    ''')

    conn.commit()
    conn.close()

# Routes
@app.route('/')
def home():
    if 'username' in session:
        return render_template('index.html')
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('home'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/add_book', methods=['POST'])
def add_book():
    if 'username' in session:
        title = request.form['title']
        author = request.form['author']
        quantity = request.form['quantity']

        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()

        cursor.execute('INSERT INTO books (title, author, quantity) VALUES (?, ?, ?)', (title, author, quantity))

        conn.commit()
        conn.close()

        return redirect(url_for('home'))
    return redirect(url_for('login'))

@app.route('/view_books')
def view_books():
    if 'username' in session:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM books')
        books = cursor.fetchall()

        conn.close()

        return render_template('view_books.html', books=books)
    return redirect(url_for('login'))



@app.route('/borrow_book/<int:book_id>', methods=['POST'])
def borrow_book(book_id):
    if 'username' in session:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()

        # Check if the book is available
        cursor.execute('SELECT * FROM books WHERE id = ? AND quantity > 0', (book_id,))
        book = cursor.fetchone()

        if book:
            # Update the quantity and record the borrow
            cursor.execute('UPDATE books SET quantity = quantity - 1 WHERE id = ?', (book_id,))
            conn.commit()

            # Insert borrow record (you may need to create a borrow table for this)
            # For simplicity, I'll just print a message here
            print(f"Book {book_id} borrowed by {session['username']}")

        conn.close()

        return redirect(url_for('view_books'))
    return redirect(url_for('login'))




if __name__ == '__main__':
    create_table()
    app.run(debug=True)
