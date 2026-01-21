from tkinter import*
from tkinter import ttk
import mysql.connector
from tkinter import messagebox

class LibManSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Library Management System")
        self.root.geometry("1550x800+0+0")

# label title
        title_lbl = Label ( self.root,
            text="LIBRARY MANAGEMENT SYSTEM",
            font=("Times New Roman", 50, "bold"),
            bg="powder blue",
            fg="green",relief=RIDGE
            )  
        title_lbl.place(relx=0.5, y=20, anchor="n")


        main_frame = Frame(
            self.root,
            bd=12,
            relief=RIDGE,
            bg="lightgray"
        )
        main_frame.place(x=0, y=130, width=1530, height=380)
        
        # Data Frame Left
        DataFrameLeft = LabelFrame(
            main_frame,
            text="Library Membership Information",
            font=("Times New Roman", 14, "bold"),
            bd=3,
            relief=RIDGE,
            bg="powder blue"
        )
        DataFrameLeft.place(x=10, y=5, width=900, height=350)

        labels_left = [
            "Member Type", "PRN No", "ID No", "First Name",
            "Last Name", "Address 1", "Address 2",
            "Post Code", "Mobile"
        ]

        for i, text in enumerate(labels_left):
            lbl = Label(
                DataFrameLeft,
                text=text + " :",
                font=("Arial", 12, "bold"),
                bg="lightblue"
            )
            lbl.grid(row=i, column=0, padx=10, pady=5, sticky=W)

        # Member Type ComboBox
        member_combo = ttk.Combobox(
            DataFrameLeft,
            values=("Admin Staff", "Student", "Faculty"),
            font=("Arial", 12),
            width=25,
            state="readonly"
        )
        member_combo.current(0)
        member_combo.grid(row=0, column=1, padx=10, pady=5)

        # Entry fields (left)
        for i in range(1, 9):
            entry = Entry(DataFrameLeft, font=("Arial", 11), width=30)
            entry.grid(row=i, column=1, padx=10, pady=5)

        # ================= Right Labels =================
        labels_right = [
            "Book Id", "Book Title", "Author Name",
            "Date Borrowed", "Date Due", "Days On Book",
            "Late Return Fine", "Date Over Due",
            "Actual Price"
        ]

        for i, text in enumerate(labels_right):
            lbl = Label(
                DataFrameLeft,
                text=text + " :",
                font=("Arial", 12, "bold"),
                bg="lightblue"
            )
            lbl.grid(row=i, column=2, padx=20, pady=5, sticky=W)

            entry = Entry(DataFrameLeft, font=("Arial", 11), width=30)
            entry.grid(row=i, column=3, padx=10, pady=5)




        DataFrameRight = LabelFrame(
            main_frame,
            text="Book Information",
            font=("Times New Roman", 14, "bold"),
            bd=3,
            relief=RIDGE,
            bg="powder blue"
        )
        DataFrameRight.place(x=920, y=5, width=570, height=350)

        scroll_y = Scrollbar(DataFrameRight, orient=VERTICAL)
        scroll_y.pack(side=RIGHT, fill=Y)

        # Listbox
        book_list = Listbox(
        DataFrameRight,
        font=("Arial", 11),
        yscrollcommand=scroll_y.set,
        bg="white"
        )
        book_list.pack(fill=BOTH, expand=1)

        scroll_y.config(command=book_list.yview)

         # Sample Book Data
        books = [
            "The Alchemist",
            "Harry Potter and the Philosopher's Stone",
            "Harry Potter and the Chamber of Secrets",
            "The Hobbit",
            "The Lord of the Rings",
            "The Chronicles of Narnia",
            "The Little Prince",
            "The Kite Runner",
            "Life of Pi",
            "The Book Thief",
            "The Fault in Our Stars",
            "Pride and Prejudice",
            "Jane Eyre",
            "Wuthering Heights",
            "To Kill a Mockingbird",
            "1984",
            "Animal Farm",
            "The Great Gatsby",
            "The Catcher in the Rye",
            "The Da Vinci Code",
            "Angels and Demons",
            "The Hunger Games",
            "Divergent",
            "The Maze Runner",
            "Percy Jackson and the Lightning Thief"
            "Head First Book",
            "Learn Python The Hard Way",
            "Python Programming",
            "Secret Rashing",
            "Python Cookbook",
            "Into to Machine Learning",
            "Fluent Python",
            "Programming Python",
            "The Algorithm",
            "The Techrich Python",
            "Machine Techno",
            "My Python",
            "Joss Ellif guru",
            "Little Jungle Python",
            "Jungle Python",
            "Mumbai Python"
        ]

        for book in books:
            book_list.insert(END, book)


        # ============= Buttons =============
        main_frame = Frame(
            self.root,
            bd=12,
            relief=RIDGE,
            bg="lightgray"
        )
        main_frame.place(x=0, y=510, width=1530, height=100)

        #Button
        ButtonFrame = LabelFrame(
            self.root,
            bd=3,
            relief=RIDGE,
            bg="powder blue"
        )
        ButtonFrame.place(x=20, y=525, width=1480, height=70)

        # Buttons ===============
        Button(ButtonFrame, text="Add Data", width=18, font=("Arial", 15, "bold")).grid(row=0, column=0, padx=5, pady=10)
        Button(ButtonFrame, text="Show Data", width=18, font=("Arial", 15, "bold")).grid(row=0, column=1, padx=5)
        Button(ButtonFrame, text="Update", width=18, font=("Arial", 15, "bold")).grid(row=0, column=2, padx=5)
        Button(ButtonFrame, text="Delete", width=18, font=("Arial", 15, "bold")).grid(row=0, column=3, padx=5)
        Button(ButtonFrame, text="Reset", width=18, font=("Arial", 15, "bold")).grid(row=0, column=4, padx=5)
        Button(ButtonFrame, text="Exit", width=18, font=("Arial", 15, "bold")).grid(row=0, column=5, padx=5)
    
        main_frame = Frame(
            self.root,
            bd=12,
            relief=RIDGE,
            bg="lightgray"
        )
        main_frame.place(x=0, y=610, width=1530, height=180)

        #Details ===============
        DetailsFrame = LabelFrame(
            self.root,
            bd=3,
            relief=RIDGE,
            bg="powder blue"
        )
        DetailsFrame.place(x=20, y=625, width=1480, height=150)


        # ================= Table Frame =================
        #TableFrame = Frame(self.root, bd=5, relief=RIDGE, bg="lightblue")
        #TableFrame.place(x=20, y=640, width=1530, height=230)

        scroll_x = Scrollbar(DetailsFrame, orient=HORIZONTAL)
        scroll_y = Scrollbar(DetailsFrame, orient=VERTICAL)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        self.library_table = ttk.Treeview(
    DetailsFrame,
    columns=(
        "member_type","ref_no","first_name","last_name","address1",
        "address2","post_code","mobile","book_id","book_title",
        "author","date_borrowed","date_due","days"
        ),
        xscrollcommand=scroll_x.set,
        yscrollcommand=scroll_y.set
        )

        scroll_x.config(command=self.library_table.xview)
        scroll_y.config(command=self.library_table.yview)

        self.library_table.heading("member_type", text="Member Type")
        self.library_table.heading("ref_no", text="Reference No")
        self.library_table.heading("first_name", text="First Name")
        self.library_table.heading("last_name", text="Last Name")
        self.library_table.heading("address1", text="Address 1")
        self.library_table.heading("address2", text="Address 2")
        self.library_table.heading("post_code", text="Post Code")
        self.library_table.heading("mobile", text="Mobile Number")
        self.library_table.heading("book_id", text="Book ID")
        self.library_table.heading("book_title", text="Book Title")
        self.library_table.heading("author", text="Author")
        self.library_table.heading("date_borrowed", text="Date Of Borrowed")
        self.library_table.heading("date_due", text="Date Due")
        self.library_table.heading("days", text="Days")

        self.library_table["show"] = "headings"
        self.library_table.pack(fill=BOTH, expand=1)

        '''# Sample Data Insertion
        data = [
                    ("Student","4587981","Kapil","Kamble","Solapur","Delhi",
                    "458721","9876543210",
                    "BKID7896","Harry Potter and the Philosopher's Stone",
                    "Zed A Shaw","2020-12-17","2021-01-01","15"),

                    ("Student","5421987","Yashwant","Kumar","Madurai","South","548712","7894561230",
                    "BKID2546","Python Cookbook","Brian Jones","2020-12-17","2021-01-01","15"),

                    ("Lecturer","6549323","Swapnil","Phase","Mumbai","Maharashtra","548795","7894561230",
                    "BKID1245","Intro to Python Comp Science","John Zhelle","2020-12-17","2021-01-01","15"),

                    ("Lecturer","6549323","Swapnil","Phase","Mumbai","Maharashtra","548795","7894561230",
                    "BKID1245","Intro to Python Comp Science","John Zhelle","2020-12-17","2021-01-01","15"),

                    ("Student","7654398","Pranit","Memane","Pune","Maharashtra","457896","7894561230",
                    "BKID8796","Basic Of Python","Ref Kapil Kamble","2020-12-17","2021-01-01","15"),

                    ("Student","8796541","Aman","Verma","Lucknow","UP","226018","9123456789",
                    "BKID5698","Fluent Python","Luciano Ramalho","2020-12-20","2021-01-04","15"),

                    ("Student","9821345","Rohit","Sharma","Nagpur","Maharashtra","440010","9988776655",
                    "BKID3478","Python Crash Course","Eric Matthes","2020-12-22","2021-01-06","15"),

                    ("Lecturer","7745123","Neha","Singh","Jaipur","Rajasthan","302015","9871234560",
                    "BKID9981","Data Science From Scratch","Joel Grus","2020-12-25","2021-01-09","15"),

                    ("Student","6654982","Rahul","Mehta","Indore","MP","452001","9012345678",
                    "BKID2254","Machine Learning Basics","Andrew Ng","2020-12-27","2021-01-11","15")
                ]
        
        for row in data:
            self.library_table.insert("", END, values=row)'''

    def connect_db(self):
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="Orangutan@2005",
            database="library_management"
        )
    
    def add_data(self):
        conn = self.connect_db()
        cur = conn.cursor()

        cur.execute("""
        INSERT INTO library_records VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                """, (
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
                ))

        conn.commit()
        conn.close()
        self.fetch_data()

    
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
        cursor_row = self.library_table.focus()
        content = self.library_table.item(cursor_row)
        row = content["values"]

        self.member_type_var.set(row[0])
        self.ref_no_var.set(row[1])
        self.first_name_var.set(row[2])
        self.last_name_var.set(row[3])
        self.address1_var.set(row[4])
        self.address2_var.set(row[5])
        self.post_code_var.set(row[6])
        self.mobile_var.set(row[7])
        self.book_id_var.set(row[8])
        self.book_title_var.set(row[9])
        self.author_var.set(row[10])
        self.date_borrowed_var.set(row[11])
        self.date_due_var.set(row[12])
        self.days_var.set(row[13])

        self.library_table.bind("<ButtonRelease-1>", self.get_cursor)

    def update_data(self):
        conn = self.connect_db()
        cur = conn.cursor()

        cur.execute("""
            UPDATE library_records SET
            member_type=%s, first_name=%s, last_name=%s, address1=%s, address2=%s,
            post_code=%s, mobile_number=%s, book_id=%s, book_title=%s, author=%s,
            date_borrowed=%s, date_due=%s, days_on_book=%s
            WHERE reference_no=%s
        """, (
        self.member_type_var.get(),
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
        self.days_var.get(),
        self.ref_no_var.get()
        ))

        conn.commit()
        conn.close()
        self.fetch_data()

    def delete_data(self):
        conn = self.connect_db()
        cur = conn.cursor()
        cur.execute(
        "DELETE FROM library_records WHERE reference_no=%s",
        (self.ref_no_var.get(),)
    )
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Record Deleted Successfully")
        self.fetch_data()

    def reset_data(self):
        vars_list = [
        self.member_type_var, self.ref_no_var, self.first_name_var,
        self.last_name_var, self.address1_var, self.address2_var,
        self.post_code_var, self.mobile_var, self.book_id_var,
        self.book_title_var, self.author_var,
        self.date_borrowed_var, self.date_due_var, self.days_var
    ]
        for var in vars_list:
            var.set("")







if __name__ =="__main__":
    root=Tk()
    obj=LibManSystem(root)
    root.mainloop()


