from tkinter import *
Template = open("SE.html","r")

App = Tk()
######

Title = Label(App,text="-{Web Maker}-\n--------")
Title.pack()

Results = {}

def Section(Field,Question):
    Label(App,text=Question+"\n--------").pack()   
    Results[Field] = Entry(App)
    Results[Field].pack()
    Label(App,text="--------").pack()

Section("Name","Name of site.")
Section("Title","Title of site.")
Section("Text","Text to go on site.")
Section("Color","Enter #hex color value.")

BT = False

def MakeSite():
    NewSite = open("Output\-"+Results["Name"].get()+".html","w+")
    Total = ""
    for LINE in Template:
        Finished = LINE.replace("Results(Name)",Results["Name"].get())
        Finished = Finished.replace("Results(Title)",Results["Title"].get())
        Finished = Finished.replace("Results(Text)",Results["Text"].get())
        Finished = Finished.replace("Results(Color)",Results["Color"].get())
        Total = Total + "\n" + Finished

    NewSite.write(Total)

    

BT = Button(App,text="Make site.",command=MakeSite).pack()

######
App.mainloop()