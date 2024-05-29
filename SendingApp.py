from tkinter import *
from datetime import datetime

class SendingApp:
    def __init__(self, user, db_ref):
        self.user = user
        self.db_ref = db_ref
        self.root = Tk()
        self.root.title(f"Send Message[{user.replace(',', '.')}]")
        self.root.geometry("400x300")

        self.recipient_label = Label(self.root, text="Recipient:")
        self.recipient_label.pack(pady=5)
        self.recipient_entry = Entry(self.root, width=50)
        self.recipient_entry.pack(pady=5)

        self.message_label = Label(self.root, text="Message:")
        self.message_label.pack(pady=5)
        self.message_entry = Entry(self.root, width=50)
        self.message_entry.pack(pady=5)

        self.send_button = Button(self.root, text="Send", command=self.send_message)
        self.send_button.pack(pady=5)

        self.status_label = Label(self.root, text="")
        self.status_label.pack(pady=5)

    def send_message(self):
        recipient = self.recipient_entry.get().replace('.', ',')
        message = self.message_entry.get()

        recipient_ref = self.db_ref.reference(f"messages/{recipient}")
        recipient_data = recipient_ref.get()

        if recipient_data is None:
            self.status_label.config(text="Recipient does not exist.", fg="red")
            return

        if "initialized" in recipient_data:
            recipient_ref.child("initialized").delete()

        if message:
            time = datetime.utcnow().strftime("%m/%d/%Y, %H:%M:%S")
            msg = {
                "content": message,
                "from": self.user,
                "time": time
            }

            recipient_ref.push(msg)
            self.status_label.config(text="Message sent successfully!", fg="green")
            self.message_entry.delete(0, 'end')
        else:
            self.status_label.config(text="Invalid!", fg="red")
            self.message_entry.delete(0, 'end')
