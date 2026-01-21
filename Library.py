from tkinter import *
from tkinter import ttk
import mysql.connector

class LibManSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("1550x800+0+0")

        # ================= VARIABLES =================
        self.member_type_var = StringVar()
        self.ref_no_var = StringVar()
        self.first_name_var = StringVar()
        self.last_name_var = StringVar()
        self.address1_var = StringVar()
        self.address2_var = StringVar()
        self.post_code_var = StringVar()
        self.mobile_var = StringVar()

        self.book_id_var = StringVar()
        self.book_title_var = StringVar()
        self.author_var = StringVar()
        self.date_borrowed_var = StringVar()
        self.date_due_var = StringVar()
        self.days_var = StringVar()
        self.price_var = StringVar()

        # ================= TITLE =================
        title_lbl = Label(
            self.root,
            text="LIBRARY MANAGEMENT SYSTEM",
            font=("Times New Roman", 30, "bold"),
            bg="lightblue",
            fg="green",
            bd=8,
            relief=RIDGE
        )
        title_lbl.pack(fill=X)

        # ================= MAIN FRAME =================
        self.main_frame = Frame(self.root, bd=5, relief=RIDGE, bg="lightblue")
        self.main_frame.place(x=10, y=90, width=1530, height=360)

        # ================= DATA FRAME LEFT =================
        self.DataFrameLeft = LabelFrame(
            self.main_frame,
            text="Library Membership Information",
            font=("Times New Roman", 14, "bold"),
            bg="lightblue",
            bd=5,
            relief=RIDGE
        )
        self.DataFrameLeft.place(x=10, y=10, width=1000, height=330)

        # ---- Left labels ----
        labels = [
            "Member Type", "Reference No", "First Name", "Last Name",
            "Address 1", "Address 2", "Post Code", "Mobile"
        ]
        vars_left = [
            self.member_type_var, self.ref_no_var, self.first_name_var,
            self.last_name_var, self.address1_var, self.address2_var,
            self.post_code_var, self.mobile_var
        ]
        

        for i, text in enumerate(labels):
            Label(self.DataFrameLeft, text=text + " :", bg="lightblue",
                  font=("Arial", 11, "bold")).place(x=10, y=20 + i*35)
            Entry(self.DataFrameLeft, textvariable=vars_left[i],
                  font=("Arial", 11), width=25).place(x=160, y=20 + i*35)

        # ---- Right labels (Book info) ----
        book_labels = [
            "Book ID", "Book Title", "Author",
            "Date Borrowed", "Date Due", "Days", "Price"
        ]
        vars_right = [
            self.book_id_var, self.book_title_var, self.author_var,
            self.date_borrowed_var, self.date_due_var,
            self.days_var, self.price_var
        ]

        for i, text in enumerate(book_labels):
            Label(self.DataFrameLeft, text=text + " :", bg="lightblue",
                  font=("Arial", 11, "bold")).place(x=420, y=20 + i*35)
            Entry(self.DataFrameLeft, textvariable=vars_right[i],
                  font=("Arial", 11), width=25).place(x=580, y=20 + i*35)

        # ================= DATA FRAME RIGHT =================
        self.DataFrameRight = LabelFrame(
            self.main_frame,
            text="Book Details",
            font=("Times New Roman", 14, "bold"),
            bg="lightblue",
            bd=5,
            relief=RIDGE
        )
        self.DataFrameRight.place(x=1020, y=10, width=490, height=330)

        # Scrollbar + Listbox
        scroll_y = Scrollbar(self.DataFrameRight, orient=VERTICAL)
        scroll_y.pack(side=RIGHT, fill=Y)

        self.book_list = Listbox(
            self.DataFrameRight,
            font=("Arial", 11),
            yscrollcommand=scroll_y.set
        )
        self.book_list.pack(fill=BOTH, expand=1)
        scroll_y.config(command=self.book_list.yview)

        # ================= BOOK DATA =================
        self.book_data = {
            "The Alchemist": ("BKID1001", "The Alchemist", "Paulo Coelho", "350"),
            "Harry Potter and the Philosopher's Stone": ("BKID1002", "Harry Potter and the Philosopher's Stone", "J.K. Rowling", "550"),
            "Harry Potter and the Chamber of Secrets": ("BKID1003", "Harry Potter and the Chamber of Secrets", "J.K. Rowling", "600"),
            "The Hobbit": ("BKID1004", "The Hobbit", "J.R.R. Tolkien", "450"),
            "The Lord of the Rings": ("BKID1005", "The Lord of the Rings", "J.R.R. Tolkien", "900"),
            "The Chronicles of Narnia": ("BKID1006", "The Chronicles of Narnia", "C.S. Lewis", "500"),
            "The Little Prince": ("BKID1007", "The Little Prince", "Antoine de Saint-Exupéry", "300"),
            "The Kite Runner": ("BKID1008", "The Kite Runner", "Khaled Hosseini", "400"),
            "Life of Pi": ("BKID1009", "Life of Pi", "Yann Martel", "350"),
            "The Book Thief": ("BKID1010", "The Book Thief", "Markus Zusak", "450"),
            "The Fault in Our Stars": ("BKID1011", "The Fault in Our Stars", "John Green", "400"),
            "Pride and Prejudice": ("BKID1012", "Pride and Prejudice", "Jane Austen", "300"),
            "Jane Eyre": ("BKID1013", "Jane Eyre", "Charlotte Brontë", "350"),
            "Wuthering Heights": ("BKID1014", "Wuthering Heights", "Emily Brontë", "320"),
            "To Kill a Mockingbird": ("BKID1015", "To Kill a Mockingbird", "Harper Lee", "380"),
            "1984": ("BKID1016", "1984", "George Orwell", "300"),
            "Animal Farm": ("BKID1017", "Animal Farm", "George Orwell", "250"),
            "The Great Gatsby": ("BKID1018", "The Great Gatsby", "F. Scott Fitzgerald", "330")
        }


        for book in self.book_data.keys():
            self.book_list.insert(END, book)

        self.book_list.bind("<<ListboxSelect>>", self.selectbook)

        # ================= BUTTON FRAME =================
        btn_frame = Frame(self.root, bd=4, relief=RIDGE, bg="lightblue")
        btn_frame.place(x=10, y=460, width=1530, height=70)

        Button(btn_frame, text="ADD DATA", width=30, command=self.add_data).grid(row=0, column=0, padx=5, pady=15)
        Button(btn_frame, text="SHOW DATA", width=30, command=self.fetch_data).grid(row=0, column=1, padx=5)
        Button(btn_frame, text="UPDATE", width=30, command=self.update_data).grid(row=0, column=2, padx=5)
        Button(btn_frame, text="DELETE", width=30, command=self.delete_data).grid(row=0, column=3, padx=5)
        Button(btn_frame, text="RESET", width=30, command=self.reset_data).grid(row=0, column=4, padx=5)
        Button(btn_frame, text="EXIT", width=30, command=self.root.quit).grid(row=0, column=5, padx=5)

        # ================= TABLE FRAME =================
        table_frame = Frame(self.root, bd=5, relief=RIDGE)
        table_frame.place(x=10, y=540, width=1530, height=230)

        scroll_x = Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(table_frame, orient=VERTICAL)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        self.library_table = ttk.Treeview(
            table_frame,
            columns=("member","ref","fname","lname","a1","a2","pc","mob",
                     "bid","btitle","author","db","dd","days"),
            xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set
        )

        scroll_x.config(command=self.library_table.xview)
        scroll_y.config(command=self.library_table.yview)

        headings = [
            "Member","Ref No","First Name","Last Name","Address1","Address2",
            "Post Code","Mobile","Book ID","Book Title","Author",
            "Date Borrowed","Date Due","Days"
        ]

        for col, head in zip(self.library_table["columns"], headings):
            self.library_table.heading(col, text=head)
            self.library_table.column(col, width=120)

        self.library_table["show"] = "headings"
        self.library_table.pack(fill=BOTH, expand=1)

        self.library_table.bind("<ButtonRelease-1>", self.get_cursor)

    # ================= DATABASE CONNECTION =================
    def connect_db(self):
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="Orangutan@2005",
            database="library_management"
        )

    # ================= FUNCTIONS =================
    def selectbook(self, event):
        index = self.book_list.curselection()
        if index:
            book = self.book_list.get(index)
            data = self.book_data[book]
            self.book_id_var.set(data[0])
            self.book_title_var.set(data[1])
            self.author_var.set(data[2])
            self.price_var.set(data[3])

    def add_data(self):
        try:
            conn = self.connect_db()
            cur = conn.cursor()

            sql = """
            INSERT INTO library_records
            (member_type, reference_no, first_name, last_name,
            address1, address2, post_code, mobile_number,
            book_id, book_title, author, date_borrowed, date_due, days_on_book)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            """

            values = (
                self.member_type_var.get(),
                self.ref_no_var.get(),
                self.first_name_var.get(),
                self.last_name_var.get(),
                self.address1_var.get(),
                self.address2_var.get(),
                self.post_code_var.get(),
                self.mobile_var.get(),
                self.book_id_var.get(),
                self.book_title_var.get(),
                self.author_var.get(),
                self.date_borrowed_var.get(),
                self.date_due_var.get(),
                self.days_var.get()
            )

            cur.execute(sql, values)
            conn.commit()
            conn.close()

            print("✅ DATA INSERTED SUCCESSFULLY")
            self.fetch_data()

        except Exception as e:
            print("❌ INSERT ERROR:", e)

    def fetch_data(self):
        conn = self.connect_db()
        cur = conn.cursor()
        cur.execute("SELECT * FROM library_records")
        rows = cur.fetchall()
        self.library_table.delete(*self.library_table.get_children())
        for row in rows:
            self.library_table.insert("", END, values=row)
        conn.close()

    def get_cursor(self, event):
        row = self.library_table.item(self.library_table.focus())["values"]
        if row:
            vars_all = [
                self.member_type_var, self.ref_no_var, self.first_name_var,
                self.last_name_var, self.address1_var, self.address2_var,
                self.post_code_var, self.mobile_var, self.book_id_var,
                self.book_title_var, self.author_var,
                self.date_borrowed_var, self.date_due_var, self.days_var
            ]
            for v, r in zip(vars_all, row):
                v.set(r)

    def update_data(self):
        conn = self.connect_db()
        cur = conn.cursor()
        cur.execute("""
            UPDATE library_records SET
            member_type=%s, first_name=%s, last_name=%s,
            address1=%s, address2=%s, post_code=%s, mobile_number=%s,
            book_id=%s, book_title=%s, author=%s,
            date_borrowed=%s, date_due=%s, days_on_book=%s
            WHERE reference_no=%s
        """, (
            self.member_type_var.get(), self.first_name_var.get(),
            self.last_name_var.get(), self.address1_var.get(),
            self.address2_var.get(), self.post_code_var.get(),
            self.mobile_var.get(), self.book_id_var.get(),
            self.book_title_var.get(), self.author_var.get(),
            self.date_borrowed_var.get(), self.date_due_var.get(),
            self.days_var.get(), self.ref_no_var.get()
        ))
        conn.commit()
        conn.close()
        self.fetch_data()

        Button(self.btn_frame, text="ADD DATA", command=self.add_data).grid(row=0, column=0)
        Button(self.btn_frame, text="UPDATE", command=self.update_data).grid(row=0, column=2)


    def delete_data(self):
        conn = self.connect_db()
        cur = conn.cursor()
        cur.execute("DELETE FROM library_records WHERE reference_no=%s",
                    (self.ref_no_var.get(),))
        conn.commit()
        conn.close()
        self.fetch_data()

    def reset_data(self):
        for var in [
            self.member_type_var, self.ref_no_var, self.first_name_var,
            self.last_name_var, self.address1_var, self.address2_var,
            self.post_code_var, self.mobile_var, self.book_id_var,
            self.book_title_var, self.author_var,
            self.date_borrowed_var, self.date_due_var,
            self.days_var, self.price_var
        ]:
            var.set("")

# ================= RUN =================
if __name__ == "__main__":
    root = Tk()
    app = LibManSystem(root)
    root.mainloop()
