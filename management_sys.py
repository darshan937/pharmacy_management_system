# Firstly import Tkinter Module
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk

root = Tk()
root.title("Pharmacy Management System")
p1 = PhotoImage(file ='pill.png')
root.iconphoto(False, p1)
root.geometry("1280x680")


#dataframe
DataFrame = Frame(root, bd=10, bg="black", relief=RIDGE, padx=20, pady=20)
DataFrame.place(x=0, y=110, width=1280, height=420)

 #title
title=Label(root,text="Pharmacy Management System",bg="black",fg="red",font=("Bradley Hand ITC",50,"bold"))
title.pack(side=TOP,fill=X,padx=10,pady=10)

 #dataframe left
DataFrameLeft=LabelFrame(DataFrame,bd=10,bg="lightblue",relief=RIDGE,padx=20,text="Medicine Information",fg="black",font=("arial",16,"bold"))
DataFrameLeft.place(x=0,y=5,width=900,height=355)

# images in left dataframe
img2 = Image.open("tab.png")
img2 = img2.resize((100, 80), Image.ANTIALIAS)
photoimg2 = ImageTk.PhotoImage(img2)
btn = Button(root, image=photoimg2, borderwidth=0)
btn.place(x=800, y=177)

img3 = Image.open("doc.png")
img3 = img3.resize((430, 200), Image.ANTIALIAS)
photoimg3 = ImageTk.PhotoImage(img3)
btn = Button(root, image=photoimg3, borderwidth=0)
btn.place(x=470, y=270)

# images in right dataframe
img4 = Image.open("abc.png")
img4 = img4.resize((70, 120), Image.ANTIALIAS)
photoimg4 = ImageTk.PhotoImage(img4)
btn = Button(root, image=photoimg4, borderwidth=0)
btn.place(x=1140, y=200)

img5 = Image.open("123.png")
img5 = img5.resize((70, 80), Image.ANTIALIAS)
photoimg5 = ImageTk.PhotoImage(img5)
btn = Button(root, image=photoimg5, borderwidth=0)
btn.place(x=1140, y=387)

 #textfield and entry for dataframe in left
 #refrence no
Refno = Label(DataFrameLeft, font=("arial", 10, "bold"), text="Reference no",bg="lightblue", padx=2,pady=6)
Refno.grid(row=0, column=0, sticky=W)
Refno_entry = Entry(DataFrameLeft,font=("arial",10,"bold"),bg="white",bd=2,relief=RIDGE,width=29)
Refno_entry.grid(row=0,column=1)

    #company/costumer name
Company = Label(DataFrameLeft, font=("arial", 10, "bold"), text="Company/Customer Name",bg="lightblue", padx=2,pady=6)
Company.grid(row=1, column=0, sticky=W)
Company_entry = Entry(DataFrameLeft,font=("arial",10,"bold"),bg="white",bd=2,relief=RIDGE,width=29)
Company_entry.grid(row=1,column=1)

    #medicine type
Med_type = Label(DataFrameLeft, font=("arial", 10, "bold"), text="Medicine Type",bg="lightblue", padx=2,pady=6)
Med_type.grid(row=2,column=0, sticky=W)
MedType_combo = ttk.Combobox(DataFrameLeft, width=27, font=("arial", 10, "bold"), state="readonly")
MedType_combo["values"] = ("Tablet", "Liquid", "Capsules","Drops","Inhales","Injection")
MedType_combo.grid(row=2, column=1)
MedType_combo.current(0)

    #medicine name
Med_name = Label(DataFrameLeft, font=("arial", 10, "bold"), text="Medicine Name",bg="lightblue", padx=2,pady=6)
Med_name.grid(row=3,column=0, sticky=W)
Medname_entry=Entry(DataFrameLeft,font=("arial",10,"bold"),bg="white",bd=2,relief=RIDGE,width=29)
Medname_entry.grid(row=3,column=1)

    #lot no
LotNo = Label(DataFrameLeft, font=("arial", 10, "bold"), text="Lot no.",bg="lightblue", padx=2,pady=6)
LotNo.grid(row=4,column=0, sticky=W)
Lot_entry = Entry(DataFrameLeft,font=("arial",10,"bold"),bg="white",bd=2,relief=RIDGE,width=29)
Lot_entry.grid(row=4,column=1)

    #issue date
Issue_date = Label(DataFrameLeft, font=("arial", 10, "bold"), text="Issue Date",bg="lightblue", padx=2,pady=6)
Issue_date.grid(row=5,column=0, sticky=W)
Issue_entry = Entry(DataFrameLeft,font=("arial",10,"bold"),bg="white",bd=2,relief=RIDGE,width=29)
Issue_entry.grid(row=5,column=1)

    #expiry date
Expiry_date = Label(DataFrameLeft, font=("arial", 10, "bold"), text="Expiry Date",bg="lightblue", padx=2,pady=6)
Expiry_date.grid(row=6,column=0, sticky=W)
Expiry_entry = Entry(DataFrameLeft,font=("arial",10,"bold"),bg="white",bd=2,relief=RIDGE,width=29)
Expiry_entry.grid(row=6,column=1)

    #dosage
Dosage = Label(DataFrameLeft, font=("arial", 10, "bold"), text="Dosage",bg="lightblue", padx=2,pady=6)
Dosage.grid(row=7,column=0, sticky=W)
Dosage_entry = Entry(DataFrameLeft,font=("arial",10,"bold"),bg="white",bd=2,relief=RIDGE,width=29)
Dosage_entry.grid(row=7,column=1)

    #tablets price
Tablets_price = Label(DataFrameLeft, font=("arial", 10, "bold"), text="Tablets Price",bg="lightblue", padx=2,pady=6)
Tablets_price.grid(row=8,column=0, sticky=W)
Tablets_entry = Entry(DataFrameLeft,font=("arial",10,"bold"),bg="white",bd=2,relief=RIDGE,width=29)
Tablets_entry.grid(row=8,column=1)

    #precution and warning
Precs_Warning = Label(DataFrameLeft, font=("arial", 10, "bold"), text="Precs & Warning",bg="lightblue",padx=6,pady=6)
Precs_Warning.grid(row=0,column=3, sticky=W)
Precs_entry = Entry(DataFrameLeft,font=("arial",10,"bold"),bg="white",bd=2,relief=RIDGE,width=29)
Precs_entry.grid(row=0,column=4)

    #uses
Uses = Label(DataFrameLeft, font=("arial", 10, "bold"), text=" Uses",bg="lightblue",padx=2,pady=6)
Uses.grid(row=1,column=3, sticky=W)
Uses_entry = Entry(DataFrameLeft,font=("arial",10,"bold"),bg="white",bd=2,relief=RIDGE,width=29)
Uses_entry.grid(row=1,column=4)

    #side effects
Sideeffects = Label(DataFrameLeft, font=("arial", 10, "bold"), text=" Side Effects",bg="lightblue",padx=2,pady=6)
Sideeffects.grid(row=2,column=3, sticky=W)
Sideeffects_entry = Entry(DataFrameLeft,font=("arial",10,"bold"),bg="white",bd=2,relief=RIDGE,width=29)
Sideeffects_entry.grid(row=2,column=4)

   # dataframe Right
DataFrameRight = LabelFrame(DataFrame, bd=10, bg="lightblue", relief=RIDGE, padx=20, text="Medicine Edit Department",
                            fg="darkgreen", font=("arial", 16, "bold"))
DataFrameRight.place(x=910, y=5, width=300, height=355)

    # edit buttons and refrence id entry on dataframe Right
    # buttons
btnAddData = Button(DataFrameRight, text="Add Medicine", font=("arial", 12, "bold"), width=14, fg="white",
                    bg="darkgreen", padx=2 )
btnAddData.grid(row=1, column=0, padx=3, pady=3)

btnUpdate = Button(DataFrameRight, text="Update", font=("arial", 12, "bold"), width=14, fg="white", bg="darkgreen",
                   padx=2 )
btnUpdate.grid(row=2, column=0, padx=3, pady=3)

btnDelete = Button(DataFrameRight, text="Delete", font=("arial", 12, "bold"), width=14, fg="white", bg="darkred"
                   )
btnDelete.grid(row=3, column=0, padx=3, pady=3)

btnExit = Button(DataFrameRight, text="Exit", font=("arial", 12, "bold"), width=14, fg="white", bg="darkred"
                 )
btnExit.grid(row=5, column=0, padx=3, pady=3)

  # search entry
txtsearch = Entry(DataFrameRight, bd=3, relief=RIDGE, width=14, font=("arial", 12, "bold"))
txtsearch.grid(row=7, column=0, padx=3, pady=3)

  #show button
ShowAllbtn = Button(DataFrameRight, text="Show All", font=("arial", 12, "bold"), width=14, fg="white", bg="darkgreen")
ShowAllbtn.grid(row=9, column=0, padx=3, pady=3)

 # Details frame
details_frame = Frame(root, bd=10, relief=RIDGE)
details_frame.place(x=0, y=540, width=1279, height=300)

 # details and scrollbar
sc_x = ttk.Scrollbar(details_frame, orient=HORIZONTAL)
sc_x.pack(side=BOTTOM, fill=X)
sc_y = ttk.Scrollbar(details_frame, orient=VERTICAL)
sc_y.pack(side=RIGHT, fill=Y)

sc_x.pack(side=BOTTOM, fill=X)
sc_y.pack(side=RIGHT, fill=Y)

mainloop()

