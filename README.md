# Trio --- A Minimal, Weakly Typed, Interpreted Programming Language

Trio is a lightweight, experimental programming language built from
scratch to explore the fundamentals of language design, parsing, and
interpreter development. It focuses on simplicity, flexibility, and easy
execution --- making it ideal for learning, experimentation, and
extending with new features.

## 🚀 Features

- Weakly Typed --- variables can hold any value without strict type
  rules
- Interpreted Execution --- no compilation step; run code directly
- Minimal Syntax --- easy to read and write
- Unix-style behavior --- returns `0` for successful execution
- Expandable Core --- designed to be enhanced with custom features

## 💡 Example (hello.trio)

    print("Hello from Trio!")
    a = 10
    b = 20
    print(a + b)

Run it via:

    python main.py examples/hello.trio

## 🛠️ How to Run

1. Clone the repository

   git clone https://github.com/Anujsharma002/Trio.git
2. Navigate into the project

   cd Trio
3. Run any Trio file

   python main.py <file.trio>

## 🧠 Learning Goals Behind Trio

- How lexers tokenize raw source code\
- How parsers build syntax trees\
- How interpreters evaluate expressions\
- Scope handling, runtime design, and minimal language architecture\
- Error handling and designing a clean execution flow

## 🌱 Planned Improvements

- Functions\
- Better error messages\
- Control flow improvements\
- A small standard library\
- Packaging Trio as a pip-installable tool

## Demo

[🎥 Watch Demo](trio.mp4)

## 🤝 Contributing

Trio is experimental --- contributions, ideas, or feedback are all
welcome!
Feel free to open an issue or submit a pull request.
