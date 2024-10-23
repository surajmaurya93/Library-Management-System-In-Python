class library:
    no_of_book=0
    book_list=[]

    def library_manage(self):
        a=input("Hey If You Want To Insert A Book Then Type 'yes': ")
        while(a=='yes'):
            insert=input("Book Name Which You Want To Insert: ")
            self.book_list.append(insert)
            self.no_of_book=self.no_of_book+1
            a=input("Type 'yes' To Insert Again And See Books Then Type 'see': ")
        if a=='see':
            print(f"The Library Have {self.no_of_book} Books And Books Are: ")
            for i in self.book_list:
                print(i)
        else:
            print("invalid input")           

obj=library()
obj.library_manage()