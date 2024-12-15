import tkinter as tk
from tkinter import scrolledtext
from chatbot import get_bot_response, bot_name

class ChatbotGUI:
    def __init__(self, root):
        self.root = root
        self.root.title(f"Chatbot - {bot_name}")
        self.root.geometry("600x400")
        self.root.resizable(True, True)

        # Create main container
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        # Create chat display area
        self.chat_display = scrolledtext.ScrolledText(self.main_frame, wrap=tk.WORD, 
                                                    width=50, height=20)
        self.chat_display.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        self.chat_display.config(state=tk.DISABLED)

        # Create input frame
        self.input_frame = tk.Frame(self.main_frame)
        self.input_frame.pack(fill=tk.X, pady=5)

        # Create input field
        self.input_field = tk.Entry(self.input_frame)
        self.input_field.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))
        self.input_field.bind("<Return>", self.send_message)

        # Create send button
        self.send_button = tk.Button(self.input_frame, text="Send", 
                                   command=self.send_message)
        self.send_button.pack(side=tk.RIGHT)

        # Welcome message
        self.display_message(f"{bot_name}: Hello! How can I help you today?")

    def display_message(self, message):
        """Display a message in the chat display"""
        self.chat_display.config(state=tk.NORMAL)
        self.chat_display.insert(tk.END, message + "\n")
        self.chat_display.see(tk.END)
        self.chat_display.config(state=tk.DISABLED)

    def send_message(self, event=None):
        """Send user message and get bot response"""
        message = self.input_field.get().strip()
        if message:
            # Display user message
            self.display_message(f"You: {message}")
            
            # Get and display bot response
            bot_response = get_bot_response(message)
            self.display_message(bot_response)

            # Clear input field
            self.input_field.delete(0, tk.END)

def main():
    root = tk.Tk()
    app = ChatbotGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()