import tkinter as tk
from tkinter import messagebox


class Book:
    def __init__(self,ID,title,author,available='True'):
        self.ID = ID
        self.title = title
        self.author = author
        self.available = available
    

   
class Bookapp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title('Book Management system')
        self.window.config(bg='#9be9eb')
        self.window.geometry('420x420')

        self.books = []

        self.set_up()
    
    def search(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

        search_label = tk.Label(self.frame,text='Enter the ID:',font=('arial',15),bg='#9be9eb')
        search_label.pack()
        search_entry = tk.Entry(self.frame,font=('arial',15))
        search_entry.pack(padx=10)

        def perform_search():
            book_id = search_entry.get().strip()
            if not book_id:
                messagebox.showerror(title='There is an error',message='please enter a valid id')
                return
            else:
                found = False
                for book in self.books:
                    if book.ID == book_id:
                        found = True
                        search_label.config(text=f'book title: {book.title}\nbook author: {book.author}\nbook id: {book.ID}')
                if not found:
                    messagebox.showerror(title='not found book',message="sorry book wasn't found")
                    return
        search_button = tk.Button(self.frame,text='search',command=perform_search)
        search_button.pack()

    def get_back(self):
        for widget in self.frame.winfo_children():
            widget.destroy()
        self.frame.pack_forget()
        self.set_up()

        


    def delete(self):
        self.title_entry.delete(0,tk.END)
        self.author_entry.delete(0,tk.END)
        self.id_entry.delete(0,tk.END)
 
    def open(self):
        container = tk.Frame(self.window,bg='#9be9eb')
        container.pack( pady=10)

        # Create the scrollbar
        scrollbar = tk.Scrollbar(container)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        listbox = tk.Listbox(container,font=('constantia',15))
        listbox.pack(padx=10,pady=10)
        count = 0
        for book in self.books:
            count += 1
            listbox.insert(tk.END,f"---- Book{count} ----")
            listbox.insert(tk.END,f'Title: {book.title}')
            listbox.insert(tk.END,f'Author: {book.author}')
            listbox.insert(tk.END,f'ID: {book.ID}')
            listbox.insert(tk.END,f"available: {book.available}")
       
    def save(self):
        if self.title_entry.get().strip() == '':
            messagebox.showerror(title='Forms uncomplete',message='complete filling out the forms')

        elif self.author_entry.get().strip() == '':
            messagebox.showerror(title='Forms uncomplete',message='complete filling out the forms')

        elif self.id_entry.get().strip() == '':
            messagebox.showerror(title='Forms uncomplete',message='complete filling out the forms')

        else:
            title = self.title_entry.get()
            author = self.author_entry.get()
            book_id = self.id_entry.get()

            book = Book(ID=book_id,title=title,author=author)
            self.books.append(book)

            label = tk.Label(self.window,font=('constantia',20),
                             text='the book saved successfully',bg='#9be9eb',fg='black')
            label.pack()

            self.window.after(3000,label.destroy)

    def new(self):
        self.title_entry.delete(0,tk.END)
        self.author_entry.delete(0,tk.END)
        self.id_entry.delete(0,tk.END)

    def exit(self):
        answer = messagebox.askyesno(title='exit the window',message='are you sure you wanna exit')
        if answer:
            self.window.destroy()

    def set_up(self):
        self.frame = tk.Frame(self.window)
        self.frame.config(bg='#9be9eb')
        self.frame.pack(padx=10,pady=10)

        menubar = tk.Menu(self.window)
        self.window.config(menu=menubar)

        file = tk.Menu(menubar,tearoff=0,font=('arial',15),relief='raised')
        menubar.add_cascade(label='File',menu=file)

        file.add_command(label='New' ,command=self.new)
        file.add_command(label='Open',command=self.open)
        file.add_command(label='Save',command=self.save)
        file.add_command(label='Exit',command=self.exit) 

        edit = tk.Menu(menubar,tearoff=0,font=('arial',15))
        menubar.add_cascade(label='Edit',menu=edit)
        edit.add_command(label='Delete',command=self.delete)
        edit.add_command(label='search',command=self.search)
        edit.add_command(label='Return',command=self.get_back)



        title_label = tk.Label(self.frame,text="Book Title:",font=('arial',15),bg='#9be9eb')
        title_label.pack()
        self.title_entry = tk.Entry(self.frame,font=('arial',15))
        self.title_entry.pack(padx=10)


        author_label = tk.Label(self.frame,text="Book Author:",font=('arial',15),bg='#9be9eb')
        author_label.pack()
        self.author_entry = tk.Entry(self.frame,font=('arial',15))
        self.author_entry.pack(padx=10)


        id_label = tk.Label(self.frame,text="Book ID:",font=('arial',15),bg='#9be9eb')
        id_label.pack()
        self.id_entry = tk.Entry(self.frame,font=('arial',15))
        self.id_entry.pack(padx=10)


        self.window.mainloop()

    

book1 = Bookapp()
