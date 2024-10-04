
# Command-Line Calculator

This is a simple command-line calculator built using Python. It allows users to perform basic arithmetic operations such as addition, subtraction, multiplication, division, and exponentiation interactively.

## Features

- Addition (`+`)
- Subtraction (`-`)
- Multiplication (`*`)
- Division (`/`)
- Power (`**`)

## How to Use

1. Run the Python file.
2. Enter the first number when prompted.
3. Choose the arithmetic operation you want to perform:
   - `+` for addition
   - `-` for subtraction
   - `*` for multiplication
   - `/` for division
   - `**` for exponentiation
4. Enter the second number for the operation.
5. To see the result and end the operation, press `=`.

### Example

```bash
Enter the first number: 5
What you want 
 addition(+) 
 subtract(-) 
 multiplication(*) 
 divide(/) 
 (=) 
 power(**)   
: +
Enter the second number: 3
8  # Result
```

### Error Handling

- Division by zero will show an "invalid" message and terminate the program.
- If an invalid data type is entered (e.g., a string), the program will terminate with an appropriate error message.

## Requirements

- Python 3.x

## Running the Calculator

```bash
python calculator.py
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
