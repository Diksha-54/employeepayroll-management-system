from tkinter import*
from tkinter import messagebox,ttk
import pymysql
import time
import os
import tempfile
class EmployeeSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Employee Payrol Management System ")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        title=Label(self.root,text="Employee Payroll Management System ",font=("times new roman",30,"bold")
                    ,bg="black",fg="white",padx=10).place(x=0,y=0,relwidth=1)
        btn_emp=Button(self.root,text="All Employees",command=self.employee_frame,font=("times new roman",15),bg="grey",fg="maroon").place(x=1100,y=9,height=30,width=120)

#**********Frame1************************************************

        #*********** variables ******************
        self.var_emp_code = StringVar()
        self.var_designation = StringVar()
        self.var_name = StringVar()
        self.var_age = StringVar()
        self.var_gender = StringVar()
        self.var_email = StringVar()
        self.var_hr_location = StringVar()
        self.var_dob = StringVar()
        self.var_doj = StringVar()
        self.var_proof = StringVar()
        self.var_contact = StringVar()
        self.var_status = StringVar()
        self.var_exp = StringVar()



        Frame1=Frame(self.root,bd=5,relief=RIDGE,bg="white")
        Frame1.place(x=10,y=50,width=720,height=640)

        #*****inside frame1*******
        title2 = Label(Frame1, text="Employee Details", font=("times new roman", 20, "bold")
                      , bg="lightgrey", fg="black", anchor="w", padx=10).place(x=0, y=0, relwidth=1)
        lbl_code=Label(Frame1, text="Employee Code", font=("times new roman", 20, "bold"), bg="white", fg="black").place(x=10, y=60)
        self.txt_code = Entry(Frame1,  font=("times new roman", 15),textvariable=self.var_emp_code, bg="lightgrey",
                                fg="black")
        self.txt_code.place(x=160, y=60)

        btn_search=Button(Frame1,text="Search",command=self.search,font=("time new roman",20),bg="pink",fg="red").place(x=370,y=60)

        lbl_designation=Label(Frame1, text="Designation", font=("times new roman", 20, "bold"), bg="white",
                         fg="black").place(x=10, y=110)
        txt_designation=Entry(Frame1, font=("times new roman", 15),textvariable=self.var_designation, bg="lightgrey",
                         fg="black").place(x=160, y=110)

        lbl_dob= Label(Frame1, text="D.O.B", font=("times new roman", 20, "bold"), bg="white",
                                fg="black").place(x=370, y=110)
        txt_dob = Entry(Frame1,  font=("times new roman", 15),textvariable=self.var_dob, bg="lightgrey",
                                fg="black").place(x=490, y=110)

        lbl_name = Label(Frame1, text="Name", font=("times new roman", 20, "bold"), bg="white",
                                fg="black").place(x=10, y=160)
        txt_name = Entry(Frame1,  font=("times new roman", 15),textvariable=self.var_name, bg="lightgrey",
                                fg="black").place(x=160, y=159)

        lbl_doj = Label(Frame1, text="D.O.J", font=("times new roman", 20, "bold"), bg="white",
                        fg="black").place(x=370, y=160)
        txt_doj = Entry(Frame1,  font=("times new roman", 15),textvariable=self.var_doj, bg="lightgrey",
                        fg="black").place(x=490, y=160)

        lbl_age = Label(Frame1, text="Age", font=("times new roman", 20, "bold"), bg="white",
                         fg="black").place(x=10, y=210)
        txt_age = Entry(Frame1,  font=("times new roman", 15),textvariable=self.var_age, bg="lightgrey",
                         fg="black").place(x=160, y=215)

        lbl_experience = Label(Frame1, text="Experience", font=("times new roman", 20, "bold"), bg="white",
                        fg="black").place(x=370, y=210)
        txt_experience = Entry(Frame1, font=("times new roman", 15),textvariable=self.var_exp, bg="lightgrey",
                        fg="black").place(x=490, y=210)

        lbl_gender = Label(Frame1, text="Gender", font=("times new roman", 20, "bold"), bg="white",
                        fg="black").place(x=10, y=260)
        txt_gender = Entry(Frame1, font=("times new roman", 15),textvariable=self.var_gender, bg="lightgrey",
                        fg="black").place(x=160, y=260)

        lbl_proofid= Label(Frame1, text="Proof ID", font=("times new roman", 20, "bold"), bg="white",
                               fg="black").place(x=370, y=260)
        txt_proofid = Entry(Frame1,  font=("times new roman", 15),textvariable=self.var_proof, bg="lightgrey",
                               fg="black").place(x=490, y=260)

        lbl_email = Label(Frame1, text="Email", font=("times new roman", 20, "bold"), bg="white",
                           fg="black").place(x=10, y=310)
        txt_email= Entry(Frame1,  font=("times new roman", 15),textvariable=self.var_email, bg="lightgrey",
                           fg="black").place(x=160, y=310)

        lbl_contact= Label(Frame1, text="Contact No.", font=("times new roman", 20, "bold"), bg="white",
                            fg="black").place(x=370, y=310)
        txt_contact= Entry(Frame1,  font=("times new roman", 15),textvariable=self.var_contact, bg="lightgrey",
                            fg="black").place(x=490, y=310)

        lbl_hiredlocation= Label(Frame1, text="Hired Location", font=("times new roman", 20, "bold"), bg="white",
                          fg="black").place(x=10, y=360)
        txt_hiredlocation = Entry(Frame1, font=("times new roman", 15),textvariable=self.var_hr_location, bg="lightgrey",
                          fg="black").place(x=160, y=360)

        lbl_status = Label(Frame1, text="Status", font=("times new roman", 20, "bold"), bg="white",
                            fg="black").place(x=370, y=360)
        txt_status = Entry(Frame1,  font=("times new roman", 15),textvariable=self.var_status, bg="lightgrey",
                            fg="black").place(x=490, y=360)

        lbl_address = Label(Frame1, text="Address", font=("times new roman", 20, "bold"), bg="white",
                                  fg="black").place(x=10, y=410)
        self.txt_address = Text(Frame1, font=("times new roman", 15), bg="lightgrey",
                                  fg="black")
        self.txt_address.place(x=160, y=410,width=500,height=190)





        #**********Frame2************************************************

        #***** variables ********

        self.var_month = StringVar()
        self.var_year = StringVar()
        self.var_basicsalary = StringVar()
        self.var_totaldays= StringVar()
        self.var_absent = StringVar()
        self.var_medical= StringVar()
        self.var_pf = StringVar()
        self.var_convence = StringVar()
        self.var_netsalary = StringVar()



        Frame2 = Frame(self.root, bd=5, relief=RIDGE, bg="white")
        Frame2.place(x=740, y=50, width=530, height=340)

        #********* inside frame2 *******
        title3 = Label(Frame2, text="Employee Salary Details", font=("times new roman", 20, "bold")
                       , bg="lightgrey", fg="black", anchor="w", padx=10).place(x=0, y=0, relwidth=1)

        lbl_month= Label(Frame2, text="Month", font=("times new roman", 20, "bold"), bg="white",
                                fg="black").place(x=10, y=50)
        txt_month = Entry(Frame2, font=("times new roman", 15),textvariable=self.var_month, bg="lightgrey",
                                fg="black").place(x=80, y=50,width=90)

        lbl_year = Label(Frame2, text="Year", font=("times new roman", 20, "bold"), bg="white",
                        fg="black").place(x=180, y=50)
        txt_year = Entry(Frame2, font=("times new roman", 15),textvariable=self.var_year, bg="lightgrey",
                        fg="black").place(x=240, y=50,width=90)

        lbl_basicsalary= Label(Frame2, text="Salary", font=("times new roman", 20, "bold"), bg="white",
                         fg="black").place(x=350, y=50)
        txt_basicsalary = Entry(Frame2, font=("times new roman", 15),textvariable=self.var_basicsalary, bg="lightgrey",
                         fg="black").place(x=420, y=50,width=90)

        lbl_totaldays= Label(Frame2, text="Total Days", font=("times new roman", 20, "bold"), bg="white",
                          fg="black").place(x=10, y=105)
        txt_totaldays = Entry(Frame2, font=("times new roman", 15),textvariable=self.var_totaldays, bg="lightgrey",
                          fg="black").place(x=120, y=105, width=100)

        lbl_absent= Label(Frame2, text="Absent", font=("times new roman", 20, "bold"), bg="white",
                         fg="black").place(x=250, y=105)
        txt_absent = Entry(Frame2, font=("times new roman", 15),textvariable=self.var_absent, bg="lightgrey",
                         fg="black").place(x=350, y=105, width=100)


        lbl_medical= Label(Frame2, text="Medical", font=("times new roman", 20, "bold"), bg="white",
                          fg="black").place(x=10, y=150)
        txt_medical = Entry(Frame2, font=("times new roman", 15),textvariable=self.var_medical, bg="lightgrey",
                          fg="black").place(x=120, y=150, width=100)

        lbl_pf= Label(Frame2, text="PF", font=("times new roman", 20, "bold"), bg="white",
                         fg="black").place(x=250, y=150)
        txt_pf= Entry(Frame2, font=("times new roman", 15),textvariable=self.var_pf, bg="lightgrey",
                         fg="black").place(x=350, y=150, width=100)

        lbl_commense= Label(Frame2, text="Commense", font=("times new roman", 20, "bold"), bg="white",
                            fg="black").place(x=10, y=190)
        txt_commense = Entry(Frame2, font=("times new roman", 15),textvariable=self.var_convence, bg="lightgrey",
                            fg="black").place(x=120, y=190, width=100)

        lbl_netsalary= Label(Frame2, text="Net Salary", font=("times new roman", 20, "bold"), bg="white",
                       fg="black").place(x=250, y=190)
        txt_netsalary = Entry(Frame2, font=("times new roman", 15),textvariable=self.var_netsalary, bg="lightgrey",
                       fg="black").place(x=350, y=190, width=100)

        btn_calculate = Button(Frame2, text="Calculate",command=self.calaculate, font=("time new roman", 20), bg="pink", fg="orange").place(x=100, y=240,width=120)
        self.btn_save = Button(Frame2, text="Save",command=self.add, font=("time new roman", 20), bg="pink", fg="lightblue")
        self.btn_save.place(x=240, y=240,width=120)
        btn_clear = Button(Frame2, text="Clear",command=self.clear, font=("time new roman", 20), bg="pink", fg="brown").place(x=390, y=240,width=120)
        self.btn_update = Button(Frame2, text="Update",command=self.update, font=("time new roman", 20), bg="pink", fg="green")
        self.btn_update.place(x=100, y=280, width=120)
        self.btn_delete = Button(Frame2, text="Delete",command=self.delete, font=("time new roman", 20), bg="pink", fg="purple")
        self.btn_delete.place(x=240, y=280, width=120)

        #**********Frame3************************************************
        Frame3=Frame(self.root,bd=5,relief=RIDGE,bg="white")
        Frame3.place(x=740,y=400,width=530,height=290)

        #********calaulator farme******
        self.var_txt=StringVar()
        self.var_operator=''
        def btn_click(num):
            self.var_operator=self.var_operator+str(num)
            self.var_txt.set(self.var_operator)


        def result():
            res=str(eval(self.var_operator))
            self.var_txt.set(res)
            self.var_operator=''
        def clear_cal():
            self.var_txt.set('')
            self.var_operator = ''





        Cal_Frame=Frame(Frame3,bg="white",bd=2,relief=RIDGE)
        Cal_Frame.place(x=2,y=2,width=250,height=280)

        txt_Result=Entry(Cal_Frame,bg="grey",textvariable=self.var_txt,font=("time new roman", 20,"bold"),justify=RIGHT).place(x=0,y=0,relwidth=1,height=40)

        btn_7=Button(Cal_Frame,text="7",command=lambda :btn_click(7),font=("time new roman",15,"bold"),fg="blue").place(x=0,y=40,w=60,h=60)
        btn_8=Button(Cal_Frame, text="8",command=lambda :btn_click(8), font=("time new roman", 15, "bold"), fg="blue").place(x=61, y=40, w=60, h=60)
        btn_9=Button(Cal_Frame, text="9",command=lambda :btn_click(9), font=("time new roman", 15, "bold"), fg="blue").place(x=122, y=40, w=60, h=60)
        btn_slash=Button(Cal_Frame, text="/",command=lambda :btn_click('/'), font=("time new roman", 15, "bold"), fg="blue").place(x=183, y=40, w=60, h=60)

        btn_4 = Button(Cal_Frame, text="4",command=lambda :btn_click(4), font=("time new roman", 15, "bold"), fg="blue").place(x=0, y=100, w=60, h=60)
        btn_5 = Button(Cal_Frame, text="5",command=lambda :btn_click(5), font=("time new roman", 15, "bold"), fg="blue").place(x=61, y=100, w=60, h=60)
        btn_6 = Button(Cal_Frame, text="6",command=lambda :btn_click(6), font=("time new roman", 15, "bold"), fg="blue").place(x=122, y=100, w=60, h=60)
        btn_star = Button(Cal_Frame, text="*",command=lambda :btn_click("*"), font=("time new roman", 15, "bold"), fg="blue").place(x=183, y=100, w=60, h=60)

        btn_1 = Button(Cal_Frame, text="1",command=lambda :btn_click(1), font=("time new roman", 15, "bold"), fg="blue").place(x=0, y=160, w=60, h=60)
        btn_2 = Button(Cal_Frame, text="2",command=lambda :btn_click(2), font=("time new roman", 15, "bold"), fg="blue").place(x=61, y=160, w=60, h=60)
        btn_3 = Button(Cal_Frame, text="3", command=lambda :btn_click(3),font=("time new roman", 15, "bold"), fg="blue").place(x=122, y=160, w=60, h=60)
        btn_minus = Button(Cal_Frame, text="-",command=lambda :btn_click("-"), font=("time new roman", 15, "bold"), fg="blue").place(x=183, y=160, w=60, h=60)

        btn_0 = Button(Cal_Frame, text="0",command=lambda :btn_click(0), font=("time new roman", 15, "bold"), fg="blue").place(x=0, y=220, w=60, h=56)
        btn_dot = Button(Cal_Frame, text="C", command=clear_cal,font=("time new roman", 15, "bold"), fg="blue").place(x=61, y=220, w=60, h=56)
        btn_plus = Button(Cal_Frame, text="+",command=lambda :btn_click("+"), font=("time new roman", 15, "bold"), fg="blue").place(x=122, y=220, w=60, h=56)
        btn_eqlto = Button(Cal_Frame, text="=",command=result, font=("time new roman", 15, "bold"), fg="blue").place(x=183, y=220, w=60, h=56)


         #*********salary frame*******
        sal_Frame = Frame(Frame3, bg="white", bd=2, relief=RIDGE)
        sal_Frame.place(x=256, y=2, width=260, height=280)

        sal_tittle = Label(sal_Frame, text="Salary Recipt", font=("times new roman", 20, "bold")
                       , bg="lightgrey", fg="black", anchor="w", padx=10).place(x=0, y=0, relwidth=1)

        sal_Frame2= Frame(sal_Frame, bg="white", bd=2, relief=RIDGE)
        sal_Frame2.place(x=0, y=33, width=255, height=210)
        self.sample=f'''\tCompany Name,XYZ\n\tAddress:Xyz, Floor4
-------------------------------------------------------
Employee ID\t\t:
Salary of\t\t: Mon-YYY
Generated On\t\t:  DD-MM--YYYY
-------------------------------------------------------
Total Days\t\t: DD
Total Present\t\t: DD
Total Absent\t\t: DD
Convence\t\t:  Rs.___
Medical\t\t:  Rs.___
PF\t\t:   Rs.___
Gross Payment\t\t:  Rs.___
Net Salary\t\t:  Ra.___
-------------------------------------------------------
This is computer generated slip,not
required any signature
'''






        scroll_y=Scrollbar(sal_Frame2,orient=VERTICAL)
        scroll_y.pack(fill=Y,side=RIGHT)

        self.txt_salary_recipt=Text(sal_Frame2,font=("times new roman",12),bg="lightgrey",yscrollcommand=scroll_y.set)
        self.txt_salary_recipt.pack(fill=BOTH,expand=1)
        scroll_y.config(command=self.txt_salary_recipt.yview)
        self.txt_salary_recipt.insert(END,self.sample)

        btn_print = Button(sal_Frame, text="Print",command=self.print, font=("time new roman", 20), bg="pink", fg="darkgreen").place(x=150, y=245,widt=100)

        self.check_connection()
#********** all function strts here **************

    def clear(self):
        self.btn_save.config(state=NORMAL)
        self.btn_update.config(state=DISABLED)
        self.btn_delete.config(state=DISABLED)
        self.txt_code.config(state=NORMAL)

        self.var_emp_code.set('')
        self.var_designation.set('')
        self.var_name.set('')
        self.var_age.set('')
        self.var_gender.set('')
        self.var_email.set('')
        self.var_hr_location.set('')
        self.var_doj.set('')
        self.var_dob.set('')
        self.var_exp.set('')
        self.var_proof.set('')
        self.var_contact.set('')
        self.var_status.set('')
        self.txt_address.delete('1.0', END)

        self.var_month.set('')
        self.var_year.set('')
        self.var_basicsalary.set('')
        self.var_totaldays.set('')
        self.var_absent.set('')
        self.var_medical.set('')
        self.var_pf.set('')
        self.var_convence.set('')
        self.var_netsalary.set('')
        self.txt_salary_recipt.delete('1.0',END)
        self.txt_salary_recipt.insert(END,self.sample)



    def delete(self):
        if self.var_emp_code.get()=="":
            messagebox.showerror("Error","employee ID must be required")

        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password='', db="ems")
                cur = con.cursor()
                cur.execute("select * from emp_salary where e_id=%s", (self.var_emp_code.get()))
                row = cur.fetchone()
                # print(row)
                if row == None:
                    messagebox.showerror("Error",
                                         "Invalid Employee ID ,Please try with another employee ID",
                                         parent=self.root)
                else:
                    op = messagebox.askyesno("Confirm", "Do you really want to delete?")
                    if op==True:
                        cur.execute("delete from emp_salary where e_id=%s", (self.var_emp_code.get()))
                        con.commit()
                        con.close()
                        messagebox.showinfo("Delete","employee record deleted succesfully",parent=self.root)
                        self.clear()





            except Exception as ex:
                messagebox.showerror("Error", f'Error due to : {str(ex)}')

    def search(self):
        try:
            con = pymysql.connect(host="localhost", user="root", password='', db="ems")
            cur = con.cursor()
            cur.execute("select * from emp_salary where e_id=%s", (self.var_emp_code.get()))
            row = cur.fetchone()
            # print(row)
            if row == None:
                messagebox.showerror("Error",
                                     "Invalid Employee ID ,Please try with another employee ID",
                                     parent=self.root)
            else:
                print(row)
                self.var_emp_code.set(row[0])
                self.var_designation.set(row[1])
                self.var_name.set(row[2])
                self.var_age.set(row[3])
                self.var_gender.set(row[4])
                self.var_email.set(row[5])
                self.var_hr_location.set(row[6])
                self.var_doj.set(row[7])
                self.var_dob.set(row[8])
                self.var_exp.set(row[9])
                self.var_proof.set(row[10])
                self.var_contact.set(row[11])
                self.var_status.set(row[12])
                self.txt_address.delete('1.0', END)
                self.txt_address.insert( END,row[13])
                self.var_month.set(row[14])
                self.var_year.set(row[15])
                self.var_basicsalary.set(row[16])
                self.var_totaldays.set(row[17])
                self.var_absent.set(row[18])
                self.var_medical.set(row[19])
                self.var_pf.set(row[20])
                self.var_convence.set(row[21])
                self.var_netsalary.set(row[22])
                file_ = open("salary_recipt/"+str(row[23]), "r")
                self.txt_salary_recipt.delete('1.0',END)
                for i in file_:
                    self.txt_salary_recipt.insert(END,i)
                file_.close()
                self.btn_save.config(state=DISABLED)
                self.btn_update.config(state=NORMAL)
                self.btn_delete.config(state=NORMAL)
                self.txt_code.config(state="readonly")



        except Exception as ex:
            messagebox.showerror("Error", f'Error due to : {str(ex)}')




    def add(self):
        if self.var_emp_code.get()=="" or self.var_netsalary.get()=="" or self.var_name.get()=="":
            messagebox.showerror("Error","Employee details are required")
        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password='', db="ems")
                cur = con.cursor()
                cur.execute("select * from emp_salary where e_id=%s", (self.var_emp_code.get()))
                row = cur.fetchone()
                # print(row)
                if row != None:
                    messagebox.showerror("Error",
                                         "This employee ID already avaliable in our record ,try again with another ID",
                                         parent=self.root)
                else:

                    cur.execute( "insert into emp_salary values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                        (
                            self.var_emp_code.get(),
                            self.var_designation.get(),
                            self.var_name.get(),
                            self.var_age.get(),
                            self.var_gender.get(),
                            self.var_email.get(),
                            self.var_hr_location.get(),
                            self.var_doj.get(),
                            self.var_dob.get(),
                            self.var_exp.get(),
                            self.var_proof.get(),
                            self.var_contact.get(),
                            self.var_status.get(),
                            self.txt_address.get('1.0', END),
                            self.var_month.get(),
                            self.var_year.get(),
                            self.var_basicsalary.get(),
                            self.var_totaldays.get(),
                            self.var_absent.get(),
                            self.var_medical.get(),
                            self.var_pf.get(),
                            self.var_convence.get(),
                            self.var_netsalary.get(),
                            f"salary_recipt_{self.var_name.get()}_{self.var_emp_code.get()}.txt"



                        )
                        )
                    con.commit()
                    con.close()

                    file_=open(f"salary_recipt/salary_recipt_{self.var_name.get()}_{self.var_emp_code.get()}.txt","w")


                    file_.write(self.txt_salary_recipt.get("1.0",END))
                    file_.close()
                    messagebox.showinfo("Success", "Record added successfully")

            except Exception as ex:
                messagebox.showerror("Error", f'Error due to : {str(ex)}')


    def update(self):
        if self.var_emp_code.get()=="" or self.var_netsalary.get()=="" or self.var_name.get()=="":
            messagebox.showerror("Error","Employee details are required")
        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password='', db="ems")
                cur = con.cursor()
                cur.execute("select * from emp_salary where e_id=%s", (self.var_emp_code.get()))
                row = cur.fetchone()
                # print(row)
                if row == None:
                    messagebox.showerror("Error",
                                         "This employee ID is invalid ,try again with valid ID",
                                         parent=self.root)
                else:

                    cur.execute( "UPDATE `emp_salary` SET `designation`=%s,`name`=%s,`age`=%s,`gender`=%s,`email`=%s,`hr_location`=%s,`doj`=%s,`dob`=%s,`experience`=%s,`proof_id`=%s,`contact`=%s,`status`=%s,`address`=%s,`month`=%s,`year`=%s,`basic_salary`=%s,`total_days`=%s,`absent`=%s,`medical`=%s,`pf`=%s,`convence`=%s,`net_salary`=%s,`salary_recipt`=%s WHERE `e_id`=%s",
                        (

                            self.var_designation.get(),
                            self.var_name.get(),
                            self.var_age.get(),
                            self.var_gender.get(),
                            self.var_email.get(),
                            self.var_hr_location.get(),
                            self.var_doj.get(),
                            self.var_dob.get(),
                            self.var_exp.get(),
                            self.var_proof.get(),
                            self.var_contact.get(),
                            self.var_status.get(),
                            self.txt_address.get('1.0', END),
                            self.var_month.get(),
                            self.var_year.get(),
                            self.var_basicsalary.get(),
                            self.var_totaldays.get(),
                            self.var_absent.get(),
                            self.var_medical.get(),
                            self.var_pf.get(),
                            self.var_convence.get(),
                            self.var_netsalary.get(),
                            f"salary_recipt_{self.var_name.get()}_{self.var_emp_code.get()}.txt",
                            self.var_emp_code.get()



                        )
                        )
                    con.commit()
                    con.close()

                    file_=open(f"salary_recipt/salary_recipt_{self.var_name.get()}_{self.var_emp_code.get()}.txt","w")


                    file_.write(self.txt_salary_recipt.get("1.0",END))
                    file_.close()
                    messagebox.showinfo("Success", "Record updated successfully")

            except Exception as ex:
                messagebox.showerror("Error", f'Error due to : {str(ex)}')




    def calaculate(self):
        if self.var_month.get()=="" or self.var_year.get()=="" or self.var_basicsalary.get()=="":
            messagebox.showerror("Error","all fields are required")
        else:
            per_day=int(self.var_basicsalary.get())/int(self.var_totaldays.get())
            work_day=int(self.var_totaldays.get())-int(self.var_absent.get())
            sal_=per_day*work_day
            deduct=int(self.var_medical.get())+int(self.var_pf.get())
            addition=int(self.var_convence.get())
            net_sal=sal_-deduct+addition
            self.var_netsalary.set(str(round(net_sal,2)))
            #*********** Update reciept ***********************
            new_sample = f'''\tCompany Name,XYZ\n\tAddress:Xyz, Floor4
-------------------------------------------------------
Employee ID\t\t:  {self.var_emp_code.get()}
Salary of\t\t:     {self.var_month.get()}-{self.var_year.get()}
Generated On\t\t:  {str(time.strftime("%d-%m-%Y"))}
-------------------------------------------------------
Total Days\t\t:  {self.var_totaldays.get()}
Total Present\t\t: {str(int(self.var_totaldays.get())-int(self.var_absent.get()))}
Total Absent\t\t: {self.var_absent.get()}
Convence\t\t:  Rs.{self.var_convence.get()}
Medical\t\t:  Rs.{self.var_medical.get()}
PF\t\t:   Rs.{self.var_pf.get()}
Gross Payment\t\t:  Rs.{self.var_basicsalary.get()}
Net Salary\t\t:  Ra.{self.var_netsalary.get()}
-------------------------------------------------------
This is computer generated slip,not
required any signature
'''

            self.txt_salary_recipt.delete('1.0',END)
            self.txt_salary_recipt.insert( END,new_sample)








            #***************** database connection*******************************
    def check_connection(self):
        try:
            con=pymysql.connect(host="localhost",user="root",password='',db="ems")
            cur=con.cursor()
            cur.execute("select * from emp_salary")
            rows=cur.fetchall()
            print(rows)
        except Exception as ex:
            messagebox.showerror("Error",f'Error due to : {str(ex)}')


    def show(self):
        try:
            con=pymysql.connect(host="localhost",user="root",password='',db="ems")
            cur=con.cursor()
            cur.execute("select * from emp_salary")
            rows=cur.fetchall()
            #print(rows)
            self.employee_tree.delete(*self.employee_tree.get_children())
            for row in rows:
                self.employee_tree.insert('',END,values=row)
            con.close()

        except Exception as ex:
            messagebox.showerror("Error",f'Error due to : {str(ex)}')


    def employee_frame(self):
        self.root2 = Toplevel(self.root)
        self.root2.title("Employee Payrol Management System ")
        self.root2.geometry("1000x500+120+90")
        self.root2.config(bg="white")
        title=Label(self.root2, text="All Employee Details ", font=("times new roman", 30, "bold")
                      , bg="black", fg="white", padx=10).pack(side=TOP,fill=X)
        self.root2.focus_force()

        scrolly=Scrollbar(self.root2,orient=VERTICAL)
        scrollx = Scrollbar(self.root2, orient=HORIZONTAL)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.pack(side=BOTTOM, fill=X)



        self.employee_tree=ttk.Treeview(self.root2,columns=('e_id', 'designation', 'name', 'age', 'gender', 'email', 'hr_location', 'doj', 'dob', 'experience', 'proof_id', 'contact', 'status', 'address', 'month', 'year', 'basic_salary', 'total_days', 'absent', 'medical', 'pf', 'convence','net_salary', 'salary_recipt'),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        self.employee_tree.heading('e_id',text='EID')
        self.employee_tree.heading('designation', text='Designation')
        self.employee_tree.heading('name', text='Name')
        self.employee_tree.heading('age', text='Age')
        self.employee_tree.heading('gender', text='Gender')
        self.employee_tree.heading('email', text='Email')
        self.employee_tree.heading('hr_location', text='Hr_location')
        self.employee_tree.heading('doj', text='D.O.J')
        self.employee_tree.heading('dob', text='D.O.B')
        self.employee_tree.heading('experience', text='Experience')
        self.employee_tree.heading('proof_id', text='Proof_ID')
        self.employee_tree.heading('contact', text='Contact')
        self.employee_tree.heading('status', text='Status')
        self.employee_tree.heading('address', text='Address')
        self.employee_tree.heading('month', text='Month')
        self.employee_tree.heading('year', text='Year')
        self.employee_tree.heading('basic_salary', text='Basic_salary')
        self.employee_tree.heading('total_days', text='Total_days')
        self.employee_tree.heading('absent', text='Absent')
        self.employee_tree.heading('medical', text='Medical')
        self.employee_tree.heading('pf', text='PF')
        self.employee_tree.heading('convence', text='Convence')
        self.employee_tree.heading('net_salary', text='Net_salary')
        self.employee_tree.heading('salary_recipt', text='Salary_recipt')
        self.employee_tree['show']='headings'

        self.employee_tree.column('e_id', width=10)
        self.employee_tree.column('designation', width=100)
        self.employee_tree.column('name', width=100)
        self.employee_tree.column('age',width=100)
        self.employee_tree.column('gender', width=100)
        self.employee_tree.column('email', width=100)
        self.employee_tree.column('hr_location', width=100)
        self.employee_tree.column('doj', width=50)
        self.employee_tree.column('dob', width=50)
        self.employee_tree.column('experience', width=100)
        self.employee_tree.column('proof_id', width=100)
        self.employee_tree.column('contact',  width=100)
        self.employee_tree.column('status',  width=100)
        self.employee_tree.column('address',   width=200)
        self.employee_tree.column('month',  width=30)
        self.employee_tree.column('year',  width=30)
        self.employee_tree.column('basic_salary',  width=100)
        self.employee_tree.column('total_days',  width=100)
        self.employee_tree.column('absent',  width=100)
        self.employee_tree.column('medical',  width=100)
        self.employee_tree.column('pf',  width=100)
        self.employee_tree.column('convence',  width=300)
        self.employee_tree.column('net_salary',  width=100)
        self.employee_tree.column('salary_recipt',  width=100)
        scrollx.config(command=self.employee_tree.xview)
        scrolly.config(command=self.employee_tree.yview)
        self.employee_tree.pack(fill=BOTH,expand=1)
        self.show()




        self.root2.mainloop()


    def print(self):
        file_=tempfile.mktemp(".txt")
        open(file_,'w').write(self.txt_salary_recipt.get('1.0',END))
        os.startfile(file_,"print")



root=Tk()
obj=EmployeeSystem(root)
root.mainloop()