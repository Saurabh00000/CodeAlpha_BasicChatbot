# 🤖 BasicChatbot

A professional, feature-rich chatbot built with Python and Tkinter, designed with a modern Google-style interface. This chatbot supports bilingual conversations (English & Hinglish) and provides intelligent responses to user queries.

![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)

## ✨ Features

- 🎨 **Modern Google-Style UI** - Clean and attractive interface
- 🌐 **Bilingual Support** - Switch between English and Hinglish
- 💬 **Smart Responses** - Pattern-based intelligent replies
- 🔢 **Math Calculations** - Solve mathematical expressions
- ⏰ **Real-Time Information** - Get current time and date
- 😄 **Entertainment** - Built-in jokes and fun responses
- 🚀 **Fast & Responsive** - Instant message handling
- 🎯 **User-Friendly** - Simple and intuitive interface

## 📸 Screenshots

### Main Interface
![Chatbot Interface](https://via.placeholder.com/800x600.png?text=Chatbot+Interface)

### Bilingual Support
![Language Toggle](https://via.placeholder.com/800x600.png?text=Language+Toggle)

## 🚀 Quick Start

### Prerequisites

- Python 3.7 or higher
- tkinter (usually comes pre-installed with Python)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/basicchatbot.git
   cd basicchatbot
   ```

2. **Install Python** (if not already installed)
   - Download from [python.org](https://www.python.org/downloads/)
   - Make sure to check "Add Python to PATH" during installation

3. **Verify tkinter installation**
   ```bash
   python -m tkinter
   ```
   If a small window appears, tkinter is installed correctly.

### Running the Chatbot

```bash
python chatbot.py
```

The chatbot GUI window will open automatically!

## 💻 Usage

### Basic Commands

- **Greetings**: `hi`, `hello`, `namaste`
- **Identity**: `who are you?`, `your name`
- **Help**: `help`, `what can you do?`
- **Jokes**: `tell me a joke`, `funny`
- **Time**: `what time is it?`, `current time`
- **Math**: `5+5`, `100*2`, `50/2`
- **Thanks**: `thank you`, `thanks`
- **Exit**: `bye`, `goodbye`

### Language Switching

Click the **🌐 English** / **🌐 हिंग्लिश** button in the header to switch between English and Hinglish modes.

## 📁 Project Structure

```
basicchatbot/
│
├── chatbot.py          # Main application file
├── README.md           # Project documentation
└── requirements.txt    # Python dependencies (if any)
```

## 🛠️ Technical Details

### Built With

- **Python 3.x** - Core programming language
- **Tkinter** - GUI framework
- **Regular Expressions (re)** - Pattern matching
- **datetime** - Time functionality
- **random** - Response variation

### Key Components

1. **GoogleStyleChatbot Class** - Main chatbot class
   - `__init__()` - Initialize chatbot and UI
   - `setup_ui()` - Create GUI elements
   - `toggle_language()` - Switch between languages
   - `get_response()` - Generate intelligent responses
   - `send_message()` - Handle user input
   - `add_bot_message()` - Display bot messages
   - `add_user_message()` - Display user messages

2. **Response System** - Dictionary-based knowledge base
   - Pattern matching using regex
   - Multiple responses per category
   - Bilingual support

3. **UI Components**
   - Header with title and language toggle
   - Scrollable chat display area
   - Input field with Enter key support
   - Send button

## 🎨 Customization

### Adding New Responses

Edit the `responses` dictionary in `chatbot.py`:

```python
self.responses = {
    'english': {
        'your_category': ["Response 1", "Response 2"],
        # Add more categories
    },
    'hinglish': {
        'your_category': ["Response 1", "Response 2"],
        # Add more categories
    }
}
```

### Adding New Patterns

Add pattern matching in `get_response()` method:

```python
if re.search(r'your_pattern', msg):
    return random.choice(resp['your_category'])
```

### Changing UI Colors

Modify the color values in `setup_ui()`:

```python
header = tk.Frame(self.root, bg="#your_color", height=70)
```

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Ideas for Contributions

- Add more language support
- Implement AI/ML for better responses
- Add voice recognition
- Create a web version
- Add database integration
- Implement chat history
- Add emoji support

## 🐛 Bug Reports

If you find a bug, please open an issue with:
- Bug description
- Steps to reproduce
- Expected behavior
- Screenshots (if applicable)
- Your environment (OS, Python version)

## 📝 License

This project is licensed under the MIT License - see below for details:

```
MIT License

Copyright (c) 2025 [Your Name]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## 👨‍💻 Author

**Your Name**
- GitHub: [@yourusername](https://github.com/yourusername)
- Email: your.email@example.com

## 🙏 Acknowledgments

- Inspired by Google Assistant's clean interface
- Built with Python's powerful Tkinter library
- Thanks to the open-source community

## 📞 Support

For support, email your.email@example.com or open an issue in the GitHub repository.

## 🔮 Future Enhancements

- [ ] Add AI/ML integration (OpenAI, Gemini)
- [ ] Voice input/output support
- [ ] Multi-language support (Hindi, Spanish, French)
- [ ] Chat history and export
- [ ] Dark mode theme
- [ ] Custom themes
- [ ] Plugin system
- [ ] Web API integration
- [ ] Mobile app version

## 📊 Stats

![GitHub stars](https://img.shields.io/github/stars/yourusername/basicchatbot?style=social)
![GitHub forks](https://img.shields.io/github/forks/yourusername/basicchatbot?style=social)
![GitHub watchers](https://img.shields.io/github/watchers/yourusername/basicchatbot?style=social)

---

⭐ **Star this repo if you find it helpful!** ⭐

Made with ❤️ and Python
