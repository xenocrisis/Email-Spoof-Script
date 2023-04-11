# config.conf data
import configparser
config = configparser.ConfigParser()
config.read('config.conf')
credentials = config['credentials']

# send email function
def sendMail(sender, target, subject, message, name='', username=credentials['email'], password=credentials['api_master_key']):

    from subprocess import check_output
    if name == '':
        exec = check_output('sendemail -xu \"'+username+'\" -xp \"'+password+'\" -f \"'+sender+'\" -t \"'+target+'\" -u \"'+subject+'\" -m \"'+message+'\" -s "smtp-relay.sendinblue.com:587" &>/dev/null'
                            ,shell=True)
    else:
        exec = check_output('sendemail -xu \"'+username+'\" -xp \"'+password+'\" -f \"'+sender+'\" -t \"'+target+'\" -u \"'+subject+'\" -m \"'+message+'\" -s "smtp-relay.sendinblue.com:587" -o message-header="From: '+name+' <'+sender+'>" &>/dev/null'
                            ,shell=True)

    from tkinter import messagebox
    messagebox.showinfo(title=None, message=exec)

# open settings window
def openSettings():

    def saveSettings():
        config.set('credentials', 'email', euser.get())
        with open('config.conf', 'w') as f:
            config.write(f)
        settingsWindow.destroy()

    # Toplevel object which will
    # be treated as a new window
    from customtkinter import CTkToplevel
    settingsWindow = CTkToplevel(root)
 
    settingsWindow.title("Settings")
    settingsWindow.geometry("300x300")
    
    # labels
    luser = CTkLabel(master=settingsWindow, text='Username:', font=('', 25))
    lpasswd = CTkLabel(master=settingsWindow, text='Password:', font=('', 25))

    # inputs
    bullet = "\u2022" #specifies bullet character
    euser = CTkEntry(master=settingsWindow, show=bullet)
    epasswd = CTkEntry(master=settingsWindow, show=bullet)


    def on_checkbox_selected():
        if checkbox_var.get():
            euser.configure(show=bullet)
            epasswd.configure(show=bullet)
        else:
            euser.configure(show="")
            epasswd.configure(show="")

    from tkinter import BooleanVar
    checkbox_var = BooleanVar()

    from customtkinter import CTkCheckBox
    checkbox = CTkCheckBox(master=settingsWindow, text="Hide credentials", variable=checkbox_var, command=on_checkbox_selected)
    checkbox.select()

    euser.insert(0, credentials['email'])
    epasswd.insert(0, credentials['api_master_key'])
    
    # buttons
    save = CTkButton(master=settingsWindow, text="Save", command=lambda: saveSettings())

    luser.grid(row=1, column=0)
    euser.grid(row=1, column=1)

    lpasswd.grid(row=2, column=0)
    epasswd.grid(row=2, column=1)

    checkbox.grid(row=3, column=0)
    save.grid(row=4, column=1)

# main window gui structure ( inputs, labels... )
from customtkinter import CTk, CTkLabel, CTkButton, CTkEntry, CTkTextbox

root = CTk()
root.title('ZSPOOFER 🪲')
root.geometry("600x400")

# label texts
ltarget = CTkLabel(master=root, text='To:', font=('', 25))
lname = CTkLabel(master=root, text='Name:', font=('', 25))
lsender = CTkLabel(master=root, text='From:', font=('', 25))
lsubject = CTkLabel(master=root, text='Subject:', font=('', 25))
lmessage = CTkLabel(master=root, text='Message:', font=('', 25))

# data inputs
etarget = CTkEntry(master=root, width=150)
ename = CTkEntry(master=root, width=150)
esender = CTkEntry(master=root, width=150)
esubject = CTkEntry(master=root, width=150)
emessage = CTkTextbox(master=root, width=400, height=300)

# buttons
send = CTkButton(master=root, text="SEND", command=lambda: sendMail(
    esender.get(),
    etarget.get(),
    esubject.get(),
    emessage.get("0.0", "end"),
    ename.get()
))

settings = CTkButton(master=root, text="Settings", command=lambda: openSettings())


def main():
    
    ltarget.grid(row=0, column=0)
    etarget.grid(row=0, column=1)

    lsender.grid(row=0, column=2)
    esender.grid(row=0, column=3)

    lsubject.grid(row=1, column=0)
    esubject.grid(row=1, column=1)

    lname.grid(row=1, column=2)
    ename.grid(row=1, column=3)

    lmessage.grid(row=2, column=0)
    emessage.grid(row=2,column=1, columnspan=3)

    send.grid(row=3, column=3)
    settings.grid(row=3, column=2)

    root.mainloop()

if __name__ == '__main__':
    main()