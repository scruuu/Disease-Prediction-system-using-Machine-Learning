#disease prediction using machine learning project 

#essential libraries for the project 
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from tkinter import *
from tkinter import messagebox

#reading the data set
data = pd.read_csv("main.csv")

symptoms = list(data.columns.values)
symptoms.pop()

disease=list(set(data.loc[:,"prognosis"]))

#splitting the dataset
x_train,x_test,y_train, y_test = train_test_split(data[symptoms],data[["prognosis"]],random_state=104,test_size=0.25,shuffle=True)  

#training and checking the accuracy of the model
from sklearn.naive_bayes import MultinomialNB
obj=MultinomialNB()
obj=obj.fit(x_train,np.ravel(y_train))
from sklearn.metrics import accuracy_score
y_pred=obj.predict(x_test)
print(accuracy_score(y_test,y_pred))      
                             
def disease_predict():
    
    if sym1.get()=="None" and sym2.get()=="None" and sym3.get()=="None" and sym4.get()=="None":
        messagebox.showinfo("ERROR", "PLEASE ENTER SYMPTOMS")
        
    else:
        #input symptoms list
        l=list()
        for x in range(len(symptoms)):
            l.append(0)
        input_symp=[sym1.get(),sym2.get(),sym3.get(),sym4.get()]
        for y in input_symp:
            if y in symptoms:
                l[symptoms.index(y)]=1
        predict=obj.predict([l])
        t1.delete("1.0",END)
        t1.insert(END,predict[0])
    

#GUI 

main=Tk()
main.title("Disease Prediction System")
main.configure()
main.geometry('800x600')


bg=PhotoImage(file="bg.png")
lbg=Label(main,i=bg,bg="grey")
lbg.pack()

sym1=StringVar()
sym1.set(None)
sym2=StringVar()
sym2.set(None)
sym3=StringVar()
sym3.set(None)
sym4=StringVar()
sym4.set(None)

heading=Label(main,text="Disease Prediction System")
heading.config(font=("Times New Roman",30),bg="#ADD8E6")
heading.place(x=190,y=10)

l1=Label(main,text="Enter the symptoms")
l1.config(font=("Times New Roman",22),bg="#ADD8E6")
l1.place(x=30,y=100)

l2=Label(main,text="Symptom 1")
l2.config(font=("Times New Roman",18),bg="#ADD8E6")
l2.place(x=200,y=200)

l3=Label(main,text="Symptom 2")
l3.config(font=("Times New Roman",18),bg="#ADD8E6")
l3.place(x=200,y=250)

l4=Label(main,text="Symptom 3")
l4.config(font=("Times New Roman",18),bg="#ADD8E6")
l4.place(x=200,y=300)

l5=Label(main,text="Symptom 4")
l5.config(font=("Times New Roman",18),bg="#ADD8E6")
l5.place(x=200,y=350)

button = Button(main, text="Predict",height=0, width=15,command=disease_predict)
button.config(font=("Times New Roman", 22),bg="#ADD8E6")
button.place(x=280,y=420)

l6=Label(main,text="Predicted Disease: ")
l6.config(font=("Times New Roman",20),bg="#ADD8E6")
l6.place(x=120,y=520)

t1=Text(main,height=1,width =20)
t1.config(font=("Times New Roman",18))
t1.place(x=350,y=520)

options=sorted(symptoms)

op1=OptionMenu(main,sym1,*options)
op1.place(x=500,y=200)

op2=OptionMenu(main,sym2,*options)
op2.place(x=500,y=250)

op3=OptionMenu(main,sym3,*options)
op3.place(x=500,y=300)

op4=OptionMenu(main,sym4,*options)
op4.place(x=500,y=350)



main.mainloop()