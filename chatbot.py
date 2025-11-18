import tkinter as tk
from tkinter import scrolledtext
import datetime
import re
import random

class GoogleStyleChatbot:
    def __init__(self, root):
        self.root = root
        self.root.title("AI Chatbot - Google Style")
        self.root.geometry("800x600")
        self.root.configure(bg="#ffffff")

        self.current_lang = 'english'

        # Complete knowledge base
        self.responses = {
            'english': {
                'greetings': ["Hello! 👋 How can I help you?", "Hi there! 😊", "Hey! I'm here to assist!"],
                'identity': ["I'm an AI chatbot built in Python! 🤖", "I'm your virtual assistant!"],
                'jokes': ["Why did the computer get cold? It left its Windows open! ❄️💻", 
                         "Why don't programmers like nature? It has too many bugs! 🐛"],
                'help': ["I can help with: Q&A, jokes, info, and math! 💡"],
                'thanks': ["You're welcome! 😊", "Happy to help! 🌟"],
                'bye': ["Goodbye! 👋", "Take care! 😊"],
                'default': ["I didn't understand that. Can you explain more? 🤔", "Interesting! Tell me more! 💡"]
            },
            'hinglish': {
                'greetings': ["Namaste! 🙏 Kaise madad kar sakta hoon?", "Hello! Aap kaise ho? 😊"],
                'identity': ["Main ek AI chatbot hoon! 🤖", "Main aapka assistant hoon!"],
                'jokes': ["Computer ne coffee pi li... crash kar diya! ☕😄"],
                'help': ["Main Q&A, jokes aur info de sakta hoon! 💡"],
                'thanks': ["Swagat hai! 😊", "Khushi hui! 🌟"],
                'bye': ["Alvida! 👋", "Phir milenge! 😊"],
                'default': ["Samajh nahi aaya. Explain karein? 🤔", "Interesting! Aur bataiye! 💡"]
            }
        }

        self.setup_ui()
        self.add_bot_message("Hello! I'm here to help you. Ask me anything! 😊")

    def setup_ui(self):
        # Header
        header = tk.Frame(self.root, bg="#f8f9fa", height=70)
        header.pack(fill=tk.X)
        header.pack_propagate(False)

        tk.Label(header, text="🤖 AI Assistant", font=("Arial", 16, "bold"), 
                bg="#f8f9fa", fg="#202124").pack(side=tk.LEFT, padx=20, pady=15)

        self.lang_btn = tk.Button(header, text="🌐 English", font=("Arial", 10),
                                 bg="#fff", fg="#202124", relief=tk.FLAT,
                                 cursor="hand2", command=self.toggle_language)
        self.lang_btn.pack(side=tk.RIGHT, padx=20, pady=15)

        # Chat display
        self.chat_display = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, 
                                                      font=("Arial", 11), bg="#fff",
                                                      fg="#202124", state=tk.DISABLED)
        self.chat_display.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Input frame
        input_frame = tk.Frame(self.root, bg="#f8f9fa", height=80)
        input_frame.pack(fill=tk.X)
        input_frame.pack_propagate(False)

        self.message_entry = tk.Entry(input_frame, font=("Arial", 12), bg="#fff", 
                                      fg="#202124", relief=tk.FLAT, bd=2)
        self.message_entry.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, 
                               padx=20, pady=20, ipady=10)
        self.message_entry.bind("<Return>", lambda e: self.send_message())

        tk.Button(input_frame, text="➤", font=("Arial", 16), bg="#1a73e8", 
                 fg="#fff", relief=tk.FLAT, width=4, 
                 command=self.send_message).pack(side=tk.RIGHT, padx=20, pady=20)

        self.message_entry.focus()

    def toggle_language(self):
        if self.current_lang == 'english':
            self.current_lang = 'hinglish'
            self.lang_btn.config(text="🌐 हिंग्लिश")
        else:
            self.current_lang = 'english'
            self.lang_btn.config(text="🌐 English")

    def add_bot_message(self, message):
        self.chat_display.config(state=tk.NORMAL)
        self.chat_display.insert(tk.END, f"Bot: {message}\n\n")
        self.chat_display.config(state=tk.DISABLED)
        self.chat_display.see(tk.END)

    def add_user_message(self, message):
        self.chat_display.config(state=tk.NORMAL)
        self.chat_display.insert(tk.END, f"You: {message}\n\n")
        self.chat_display.config(state=tk.DISABLED)
        self.chat_display.see(tk.END)

    def get_response(self, message):
        msg = message.lower().strip()
        resp = self.responses[self.current_lang]

        if re.search(r'\\b(hi|hello|hey|namaste)\\b', msg):
            return random.choice(resp['greetings'])
        if re.search(r'(who are you|tum kaun|your name)', msg):
            return random.choice(resp['identity'])
        if re.search(r'(joke|hasao|funny)', msg):
            return random.choice(resp['jokes'])
        if re.search(r'(help|madad|kya kar)', msg):
            return random.choice(resp['help'])
        if re.search(r'(time|samay)', msg):
            return f"Current time: {datetime.datetime.now().strftime('%I:%M:%S %p')} ⏰"
        if re.search(r'(thank|shukriya)', msg):
            return random.choice(resp['thanks'])
        if re.search(r'(bye|alvida)', msg):
            return random.choice(resp['bye'])

        # Math
        if re.search(r'\\d+\\s*[\\+\\-\\*\\/]\\s*\\d+', msg):
            try:
                result = eval(re.sub(r'[^0-9+\\-*/().]', '', message))
                return f"Answer: {result} 🔢"
            except:
                pass

        return random.choice(resp['default'])

    def send_message(self):
        message = self.message_entry.get().strip()
        if not message:
            return

        self.add_user_message(message)
        self.message_entry.delete(0, tk.END)

        response = self.get_response(message)
        self.root.after(300, lambda: self.add_bot_message(response))

if __name__ == "__main__":
    root = tk.Tk()
    app = GoogleStyleChatbot(root)
    root.mainloop()
