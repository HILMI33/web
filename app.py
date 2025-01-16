from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'  
app.config['MYSQL_PASSWORD'] = ''  
app.config['MYSQL_DB'] = 'pawon'

mysql = MySQL(app)
app.secret_key = 'pawon'

@app.route("/")
def home():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM contacts")
    contact_list = cursor.fetchall()
    return render_template("index.html", products=products, contacts=contact_list)
# @app.route("/home")
# def utama():
#     render_template("home.html")

@app.route("/add", methods=["GET", "POST"])
def add_product():
    if request.method == "POST":
        name = request.form['name']
        description = request.form['description']
        price = request.form['price']
        image = request.form['image']
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO products (name, description, price, image) VALUES (%s, %s, %s, %s)", 
                       (name, description, price, image))
        mysql.connection.commit()
        flash("Produk berhasil ditambahkan!")
        return redirect(url_for("home"))
    return render_template("add_product.html")

@app.route('/about')
def about():
    return render_template ('about.html')

@app.route('/contacskuh')
def contactku():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM contacts")
    contact_list = cursor.fetchall()
    return render_template("contactskuh.html", contacts=contact_list)

@app.route('/product')
def product():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    return render_template ('product.html', products=products)

@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_product(id):
    cursor = mysql.connection.cursor()
    if request.method == "POST":
        name = request.form['name']
        description = request.form['description']
        price = request.form['price']
        image = request.form['image']
        cursor.execute("""
            UPDATE products 
            SET name=%s, description=%s, price=%s, image=%s 
            WHERE id=%s
        """, (name, description, price, image, id))
        mysql.connection.commit()
        flash("Produk berhasil diperbarui!")
        return redirect(url_for("home"))

    cursor.execute("SELECT * FROM products WHERE id=%s", (id,))
    product = cursor.fetchone()
    return render_template("edit_product.html", product=product)

@app.route("/delete/<int:id>")
def delete_product(id):
    cursor = mysql.connection.cursor()
    cursor.execute("DELETE FROM products WHERE id=%s", (id,))
    mysql.connection.commit()
    flash("Produk berhasil dihapus!")
    return redirect(url_for("home"))

@app.route("/contacts")
def contacts():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM contacts")
    contact_list = cursor.fetchall()
    return render_template("contacts.html", contacts=contact_list)

@app.route("/contacts/add", methods=["GET", "POST"])
def add_contact():
    if request.method == "POST":
        name = request.form['name']
        whatsapp_number = request.form['whatsapp_number']
        description = request.form['description']
        cursor = mysql.connection.cursor()
        cursor.execute(
            "INSERT INTO contacts (name, whatsapp_number, description) VALUES (%s, %s, %s)",
            (name, whatsapp_number, description)
        )
        mysql.connection.commit()
        flash("Kontak berhasil ditambahkan!")
        return redirect(url_for("contacts"))
    return render_template("add_contact.html")

@app.route("/contacts/edit/<int:id>", methods=["GET", "POST"])
def edit_contact(id):
    cursor = mysql.connection.cursor()
    if request.method == "POST":
        name = request.form['name']
        whatsapp_number = request.form['whatsapp_number']
        description = request.form['description']
        cursor.execute(
            """
            UPDATE contacts 
            SET name=%s, whatsapp_number=%s, description=%s 
            WHERE id=%s
            """,
            (name, whatsapp_number, description, id)
        )
        mysql.connection.commit()
        flash("Kontak berhasil diperbarui!")
        return redirect(url_for("contacts"))

    cursor.execute("SELECT * FROM contacts WHERE id=%s", (id,))
    contact = cursor.fetchone()
    return render_template("edit_contact.html", contact=contact)

@app.route("/contacts/delete/<int:id>")
def delete_contact(id):
    cursor = mysql.connection.cursor()
    cursor.execute("DELETE FROM contacts WHERE id=%s", (id,))
    mysql.connection.commit()
    flash("Kontak berhasil dihapus!")
    return redirect(url_for("contacts"))

if __name__ == "__main__":
    app.run(debug=True)

