import tkinter as tk
import sqlite3
from tkinter import END, Entry, messagebox
from time import gmtime, strftime
import datetime

dbstore=sqlite3.connect('Customer.db')


def is_number(s):
    try:
        float(s)
        return 1
    except ValueError:
        return 0

def check_acc_nmb(num,pin):

	cursor=dbstore.cursor()
	cursor.execute("SELECT * FROM Accnt_Record_new where (account_no = ? AND pin =?)",(num,pin,))
	acc_ex=cursor.fetchall()
	dbstore.commit()

	parm = acc_ex

	if len(parm) == 0:
		messagebox.showinfo("Error","Invalid Credentials!\nTry Again!")
		return 0
	else:
		return 1

	#try:
	#	fpin=open(num+".txt",'r')
	#except FileNotFoundError:
	#	messagebox.showinfo("Error","Invalid Credentials!\nTry Again!")
	#	return 0
	#fpin.close()
	#return 

def home_return(master):
	master.destroy()
	Main_Menu()

def write(master,name,oc,pin):
	
	if( (is_number(name)) or (is_number(oc)==0) or (is_number(pin)==0)or name==""):
		messagebox.showinfo("Error","Invalid Credentials\nPlease try again.")
		master.destroy()
		return 

	#f1=open("Accnt_Record.txt",'r')
	#accnt_no=int(f1.readline())
	#accnt_no+=1
	#f1.close()

	#f1=open("Accnt_Record.txt",'w')
	#f1.write(str(accnt_no))
	#f1.close()

	#cursor=dbstore.cursor()
	#cursor.execute("SELECT MAX(account_no) FROM Accnt_Record_new")
	#acc_no=cursor.fetchone
	#dbstore.commit()
	#acc_no+=1
	
	cursor=dbstore.cursor()
	cursor.execute("INSERT INTO Accnt_Record_new (name,op_credit,pin) values (?,?,?)",(name,oc,pin))
	dbstore.commit()

	cursor=dbstore.cursor()
	cursor.execute("SELECT MAX(account_no) from Accnt_Record_new" )
	acc_no=cursor.fetchone()
	dbstore.commit()

	acc=int(acc_no[0])
	#print(acc)
	time_now=datetime.datetime.now()
	#time_new = str(time).split()[0]

	cursor=dbstore.cursor()
	cursor.execute("INSERT INTO transaction_new (account_no,credit,debit,Date) values (?,?,?,?)",(acc,oc,0,time_now))
	dbstore.commit()


	#fdet=open(str(accnt_no)+".txt","w")
	#fdet.write(pin+"\n")
	#fdet.write(oc+"\n")
	#fdet.write(str(accnt_no)+"\n")
	#fdet.write(name+"\n")
	#fdet.close()



	#frec=open(str(accnt_no)+"-rec.txt",'w')
	#frec.write("Date                             Credit      Debit     Balance\n")
	#frec.write(str(strftime("[%Y-%m-%d] [%H:%M:%S]  ",gmtime()))+"     "+oc+"              "+oc+"\n")
	#frec.close()
	
	messagebox.showinfo("Details","Your Account Number is:"+str(acc))
	master.destroy()
	return

def crdt_write(master,amt,accnt,name):

	if(is_number(amt)==0):
		messagebox.showinfo("Error","Invalid Credentials\nPlease try again.")
		master.destroy()
		return 

	time_now=datetime.datetime.now()

	cursor=dbstore.cursor()
	cursor.execute("INSERT INTO transaction_new (account_no,credit,debit,Date) values (?,?,?,?)",(accnt,amt,0,time_now))
	dbstore.commit()

	#fdet=open(accnt+".txt",'r')
	#pin=fdet.readline()
	#camt=int(fdet.readline())
	#fdet.close()
	#amti=int(amt)
	#cb=amti+camt
	#fdet=open(accnt+".txt",'w')
	#fdet.write(pin)
	#fdet.write(str(cb)+"\n")
	#fdet.write(accnt+"\n")
	#fdet.write(name+"\n")
	#fdet.close()
	#frec=open(str(accnt)+"-rec.txt",'a+')
	#frec.write(str(strftime("[%Y-%m-%d] [%H:%M:%S]  ",gmtime()))+"     "+str(amti)+"              "+str(cb)+"\n")
	#frec.close()
	messagebox.showinfo("Operation Successfull!!","Amount Credited Successfully!!")
	master.destroy()
	return

def debit_write(master,amt,accnt,name):

	if(is_number(amt)==0):
		messagebox.showinfo("Error","Invalid Credentials\nPlease try again.")
		master.destroy()
		return 

	time_now=datetime.datetime.now()

	cursor=dbstore.cursor()
	cursor.execute("INSERT INTO transaction_new (account_no,credit,debit,Date) values (?,?,?,?)",(accnt,0,amt,time_now))
	dbstore.commit()


	#fdet=open(accnt+".txt",'r')
	#pin=fdet.readline()
	#camt=int(fdet.readline())
	#fdet.close()
	#if(int(amt)>camt):
	#	messagebox.showinfo("Error!!","You dont have that amount left in your account\nPlease try again.")
	#else:
	#	amti=int(amt)
	#	cb=camt-amti
	#	fdet=open(accnt+".txt",'w')
	#	fdet.write(pin)
	#	fdet.write(str(cb)+"\n")
	#	fdet.write(accnt+"\n")
	#	fdet.write(name+"\n")
	#	fdet.close()
	#	frec=open(str(accnt)+"-rec.txt",'a+')
	#	frec.write(str(strftime("[%Y-%m-%d] [%H:%M:%S]  ",gmtime()))+"     "+"              "+str(amti)+"              "+str(cb)+"\n")
	#	frec.close()
	messagebox.showinfo("Operation Successfull!!","Amount Debited Successfully!!")
	master.destroy()
	return

def Cr_Amt(accnt,name):
	creditwn=tk.Tk()
	creditwn.geometry("600x300") 
	creditwn.title("Credit Amount")
	creditwn.configure(bg="SteelBlue1")
	fr1=tk.Frame(creditwn,bg="blue")
	l_title=tk.Message(creditwn,text="BANK MANAGEMENT SYSTEM",relief="raised",width=2000,padx=600,pady=0,fg="white",bg="blue4",justify="center",anchor="center")
	l_title.config(font=("Arial","50","bold"))
	l_title.pack(side="top")
	l1=tk.Label(creditwn,relief="raised",font=("Times",16),text="Enter Amount to be credited: ")
	e1=tk.Entry(creditwn,relief="raised")
	l1.pack(side="top")
	e1.pack(side="top")
	b=tk.Button(creditwn,text="Credit",font=("Times",16),relief="raised",command=lambda:crdt_write(creditwn,e1.get(),accnt,name))
	b.pack(side="top")
	creditwn.bind("<Return>",lambda x:crdt_write(creditwn,e1.get(),accnt,name))


def De_Amt(accnt,name):
	debitwn=tk.Tk()
	debitwn.geometry("600x300")
	debitwn.title("Debit Amount")	
	debitwn.configure(bg="SteelBlue1")
	fr1=tk.Frame(debitwn,bg="blue")
	l_title=tk.Message(debitwn,text="BANK MANAGEMENT SYSTEM",relief="raised",width=2000,padx=600,pady=0,fg="white",bg="blue4",justify="center",anchor="center")
	l_title.config(font=("Arial","50","bold"))
	l_title.pack(side="top")
	l1=tk.Label(debitwn,relief="raised",font=("Times",16),text="Enter Amount to be debited: ")
	e1=tk.Entry(debitwn,relief="raised")
	l1.pack(side="top")
	e1.pack(side="top")
	b=tk.Button(debitwn,text="Debit",font=("Times",16),relief="raised",command=lambda:debit_write(debitwn,e1.get(),accnt,name))
	b.pack(side="top")
	debitwn.bind("<Return>",lambda x:debit_write(debitwn,e1.get(),accnt,name))


def fund_trans_write(master,accnt2,amt,accnt):
	if(is_number(amt)==0):
		messagebox.showinfo("Error","Invalid Credentials\nPlease try again.")
		master.destroy()
		return 

	time_now=datetime.datetime.now()

	cursor=dbstore.cursor()
	cursor.execute("INSERT INTO transaction_new (account_no,credit,debit,Date) values (?,?,?,?)",(accnt2,amt,0,time_now))
	dbstore.commit()

	cursor=dbstore.cursor()
	cursor.execute("INSERT INTO transaction_new (account_no,credit,debit,Date) values (?,?,?,?)",(accnt,0,amt,time_now))
	dbstore.commit()

	messagebox.showinfo("Operation Successfull!!","Amount transferred Successfully!!")
	master.destroy()
	return




def fund_trans(accnt):
	creditwn=tk.Tk()
	creditwn.geometry("600x300") 
	creditwn.title("Fund Transfer")
	creditwn.configure(bg="SteelBlue1")
	fr1=tk.Frame(creditwn,bg="blue")
	l_title=tk.Message(creditwn,text="BANK MANAGEMENT SYSTEM",relief="raised",width=2000,padx=600,pady=0,fg="white",bg="blue4",justify="center",anchor="center")
	l_title.config(font=("Arial","50","bold"))
	l_title.pack(side="top")
	l2=tk.Label(creditwn,relief="raised",font=("Times",16),text="Enter account no of transferrer: ")
	e2=tk.Entry(creditwn,relief="raised")
	l2.pack(side="top")
	e2.pack(side="top")
	l1=tk.Label(creditwn,relief="raised",font=("Times",16),text="Enter Amount to be transfered: ")
	e1=tk.Entry(creditwn,relief="raised")
	l1.pack(side="top")
	e1.pack(side="top")

	b=tk.Button(creditwn,text="Credit",font=("Times",16),relief="raised",command=lambda:fund_trans_write(creditwn,e2.get(),e1.get(),accnt))
	b.pack(side="top")
	creditwn.bind("<Return>",lambda x:fund_trans_write(creditwn,e2.get(),e1.get(),accnt))
	
	






def disp_bal(accnt):
	#fdet=open(accnt+".txt",'r')
	#fdet.readline()
	#bal=fdet.readline()
	#fdet.close()
	
	cursor=dbstore.cursor()
	cursor.execute("SELECT * from transaction_new where account_no = ?",(accnt,))
	tr_det=cursor.fetchall()
	dbstore.commit()
	crd = 0
	deb = 0

	#for stm in tr_det:
	#	for i in range(len(stm)):
	#		crd = crd + i[1]
		
	
	#for stn in tr_det:
	#	for j in range(len(stn)):
	#		deb = deb + j[1]

	cursor=dbstore.cursor()
	cursor.execute("SELECT credit from transaction_new where account_no = ?",(accnt,))
	tr_det_crd=cursor.fetchall()
	dbstore.commit()

	cursor=dbstore.cursor()
	cursor.execute("SELECT debit from transaction_new where account_no = ?",(accnt,))
	tr_det_deb=cursor.fetchall()
	dbstore.commit()

	crd_new = int(0)
	for x in tr_det_crd:
		crd_new+=int(x[0])
	
	deb_new = int(0)
	for y in tr_det_deb:
		deb_new+=int(y[0])
		
	
	bala = crd_new-deb_new


	#acc=int(acc_no[0])
	#print(acc)
	#time_now=datetime.datetime.now()
	#time_new = str(time).split()[0]

	#cursor=dbstore.cursor()
	#cursor.execute("INSERT INTO transaction_new (account_no,credit,debit,Date) values (?,?,?,?)",(acc,oc,0,time_now))
	#dbstore.commit()

	messagebox.showinfo("Balance",bala)




def disp_tr_hist(accnt):
	disp_wn=tk.Tk()
	disp_wn.geometry("900x600")
	"""disp_wn.title("Transaction History")
	disp_wn.configure(bg="SteelBlue1")
	fr1=tk.Frame(disp_wn,bg="blue")
	l_title=tk.Message(disp_wn,text="BANK MANAGEMENT SYSTEM",relief="raised",width=2000,padx=600,pady=0,fg="white",bg="blue4",justify="center",anchor="center")
	l_title.config(font=("Arial","50","bold"))
	#l_title.pack(side="top")
	fr1=tk.Frame(disp_wn)
	#fr1.pack(side="top")
	l1=tk.Message(disp_wn,text="Your Transaction History:",font=("Times",16),padx=100,pady=20,width=1000,bg="blue4",fg="SteelBlue1",relief="raised")
	#l1.pack(side="top")
	fr2=tk.Frame(disp_wn)
	#fr2.pack(side="top")"""

	cursor=dbstore.cursor()
	cursor.execute("SELECT * from transaction_new where account_no = ?",(accnt,))
	trnst=cursor.fetchall()
	dbstore.commit()

	i=0 # row value inside the loop 
	for student in trnst:
		for j in range(len(student)):
			e = Entry(disp_wn, width=30, fg='blue') 
			e.grid(row=i, column=j) 
			e.insert(END, student[j])
		i=i+1
	
	
	#frec=open(accnt+"-rec.txt",'r')
	#for line in frec:
	#	l=tk.Message(disp_wn,anchor="w",text=line,relief="raised",width=2000)
	#	l.pack(side="top")
	#b=tk.Button(disp_wn,text="Quit",relief="raised",command=disp_wn.destroy)
	#b.pack(side="top")
	#frec.close()

def logged_in_menu(accnt,name):
	rootwn=tk.Tk()
	rootwn.geometry("1600x500")
	rootwn.title("CopyAssignment Bank | Welcome - "+name)
	rootwn.configure(background='SteelBlue1')
	fr1=tk.Frame(rootwn)
	fr1.pack(side="top")
	l_title=tk.Message(rootwn,text="BANK MANAGEMENT SYSTEM",relief="raised",width=2000,padx=600,pady=0,fg="white",bg="blue4",justify="center",anchor="center")
	l_title.config(font=("Arial","50","bold"))
	l_title.pack(side="top")
	label=tk.Label(text="Logged in as: "+name,relief="raised",bg="blue3",font=("Times",16),fg="white",anchor="center",justify="center")
	label.pack(side="top")
	img2=tk.PhotoImage(file="credit.gif")
	myimg2=img2.subsample(2,2)
	img3=tk.PhotoImage(file="debit.gif")
	myimg3=img3.subsample(2,2)
	img4=tk.PhotoImage(file="balance1.gif")
	myimg4=img4.subsample(2,2)
	img5=tk.PhotoImage(file="transaction-1.gif")
	myimg5=img5.subsample(2,2)
	img7=tk.PhotoImage(file="fund_transfer.gif")
	myimg7=img7.subsample(2,2)
	b2=tk.Button(image=myimg2,command=lambda: Cr_Amt(accnt,name))
	b2.image=myimg2
	b3=tk.Button(image=myimg3,command=lambda: De_Amt(accnt,name))
	b3.image=myimg3
	b4=tk.Button(image=myimg4,command=lambda: disp_bal(accnt))
	b4.image=myimg4
	b5=tk.Button(image=myimg5,command=lambda: disp_tr_hist(accnt))
	b5.image=myimg5
	b7=tk.Button(image=myimg7,command=lambda: fund_trans(accnt))
	b7.image=myimg7
	
	img6=tk.PhotoImage(file="logout-1.gif")
	myimg6=img6.subsample(2,2)
	b6=tk.Button(image=myimg6,relief="raised",command=lambda: logout(rootwn))
	b6.image=myimg6

	
	b2.place(x=100,y=150)
	b3.place(x=100,y=220)
	b4.place(x=900,y=150)
	b5.place(x=900,y=220)
	b6.place(x=500,y=350)
	b7.place(x=500,y=300)

	
def logout(master):
	
	messagebox.showinfo("Logged Out","You Have Been Successfully Logged Out!!")
	master.destroy()
	Main_Menu()

def check_log_in(master,name,acc_num,pin):
	if(check_acc_nmb(acc_num,pin)==0):
		master.destroy()
		Main_Menu()
		return

	if( (is_number(name))  or (is_number(pin)==0) ):
		messagebox.showinfo("Error","Invalid Credentials\nPlease try again.")
		master.destroy()
		Main_Menu()
	else:
		master.destroy()
		logged_in_menu(acc_num,name)


def log_in(master):
	master.destroy()
	loginwn=tk.Tk()
	loginwn.geometry("600x300")
	loginwn.title("Log in")
	loginwn.configure(bg="SteelBlue1")
	fr1=tk.Frame(loginwn,bg="blue")
	l_title=tk.Message(loginwn,text="BANK MANAGEMENT SYSTEM",relief="raised",width=2000,padx=600,pady=0,fg="white",bg="blue4",justify="center",anchor="center")
	l_title.config(font=("Arial","50","bold"))
	l_title.pack(side="top")
	l1=tk.Label(loginwn,text="Enter Name:",font=("Times",16),relief="raised")
	l1.pack(side="top")
	e1=tk.Entry(loginwn)
	e1.pack(side="top")
	l2=tk.Label(loginwn,text="Enter account number:",font=("Times",16),relief="raised")
	l2.pack(side="top")
	e2=tk.Entry(loginwn)
	e2.pack(side="top")
	l3=tk.Label(loginwn,text="Enter your PIN:",font=("Times",16),relief="raised")
	l3.pack(side="top")
	e3=tk.Entry(loginwn,show="*")
	e3.pack(side="top")
	b=tk.Button(loginwn,text="Submit",command=lambda: check_log_in(loginwn,e1.get().strip(),e2.get().strip(),e3.get().strip()))
	b.pack(side="top")
	b1=tk.Button(text="HOME",font=("Times",16),relief="raised",bg="blue4",fg="white",command=lambda: home_return(loginwn))
	b1.pack(side="top")
	loginwn.bind("<Return>",lambda x:check_log_in(loginwn,e1.get().strip(),e2.get().strip(),e3.get().strip()))
	

def Create():
	
	crwn=tk.Tk()
	crwn.geometry("600x300")
	crwn.title("Create Account")
	crwn.configure(bg="SteelBlue1")
	fr1=tk.Frame(crwn,bg="blue")
	l_title=tk.Message(crwn,text="BANK MANAGEMENT SYSTEM",relief="raised",width=2000,padx=600,pady=0,fg="white",bg="blue4",justify="center",anchor="center")
	l_title.config(font=("Arial","50","bold"))
	l_title.pack(side="top")
	l1=tk.Label(crwn,text="Enter Name:",font=("Times",16),relief="raised")
	l1.pack(side="top")
	e1=tk.Entry(crwn)
	e1.pack(side="top")
	l2=tk.Label(crwn,text="Enter opening credit:",font=("Times",16),relief="raised")
	l2.pack(side="top")
	e2=tk.Entry(crwn)
	e2.pack(side="top")
	l3=tk.Label(crwn,text="Enter desired PIN:",font=("Times",16),relief="raised")
	l3.pack(side="top")
	e3=tk.Entry(crwn,show="*")
	e3.pack(side="top")
	b=tk.Button(crwn,text="Submit",font=("Times",16),command=lambda: write(crwn,e1.get().strip(),e2.get().strip(),e3.get().strip()))
	b.pack(side="top")
	crwn.bind("<Return>",font=("Times",16),command=lambda x:write(crwn,e1.get().strip(),e2.get().strip(),e3.get().strip()))
	return


def Main_Menu():
	rootwn=tk.Tk()
	rootwn.geometry("1600x500")
	rootwn.title("Bank Management System - 	CopyAssignment")
	rootwn.configure(background='SteelBlue1')
	fr1=tk.Frame(rootwn)
	fr1.pack(side="top")
	l_title=tk.Message(text="BANK MANAGEMENT SYSTEM ",relief="raised",width=2000,padx=600,pady=0,fg="white",bg="blue4",justify="center",anchor="center")
	l_title.config(font=("Verdana","40","bold"))
	l_title.pack(side="top")
	imgc1=tk.PhotoImage(file="new-1.gif")
	imglo=tk.PhotoImage(file="login.gif")
	imgc=imgc1.subsample(2,2)
	imglog=imglo.subsample(2,2)

	b1=tk.Button(image=imgc,command=Create)
	b1.image=imgc
	b2=tk.Button(image=imglog,command=lambda: log_in(rootwn))
	b2.image=imglog
	img6=tk.PhotoImage(file="quit-1.gif")
	myimg6=img6.subsample(2,2)

	b6=tk.Button(image=myimg6,command=rootwn.destroy)
	b6.image=myimg6
	b1.place(x=800,y=300)
	b2.place(x=800,y=200)	
	b6.place(x=920,y=400)

	rootwn.mainloop()

Main_Menu()
