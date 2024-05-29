from tkinter import *
import threading

def is_dict_of_dicts(d):
    if d:
        return all(isinstance(v, dict) for v in d.values())
    else:
        return False

class ReceivingApp:
    def __init__(self, user_email, db_ref):
        self.user_email = user_email
        self.db_ref = db_ref
        self.root = Tk()
        self.root.title(f"Receive Messages[{user_email.replace(',', '.')}]")
        self.root.minsize(400, 300)

        self.messages_text = Text(self.root)
        self.messages_text.pack()

        threading.Thread(target=self.listen_for_messages, daemon=True).start()

    def listen_for_messages(self):
        user_key = self.user_email.replace('.', ',')
        messages_ref = self.db_ref.reference(f"messages/{user_key}")

        def listener(event):
            data = event.data
            if data:
                if is_dict_of_dicts(data):
                    for key, val in data.items():
                        if isinstance(val, dict) and "content" in val:
                            self.update_messages_text(val)
                elif isinstance(data, dict):
                    if "content" in data:
                        self.update_messages_text(data)
                else:
                    self.update_messages_text(data)

        # Listen for database changes
        messages_ref.listen(listener)

    def update_messages_text(self, msg):
        def insert_message():
            self.messages_text.insert(END, f"From: {msg['from'].replace(',', '.')}[{msg['time']}]\nMessage: {msg['content']}\n\n")
            self.messages_text.see(END)

        self.root.after(0, insert_message)

