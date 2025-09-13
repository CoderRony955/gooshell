# goodshell

A hybrid shell built with C and Python that provides a rich terminal experience. Goodshell supports standard Windows terminal commands and also includes a set of custom commands.

## Features

- **Hybrid Shell**: Core functionality is built with C, while custom commands are powered by Python.
- **Windows Command Support**: Execute standard Windows terminal commands directly within Goodshell.
- **Custom Commands**: A unique set of commands to enhance your shell experience.
- **Rich Output**: Utilizes the `rich` library in Python for styled and colorful output.

## Custom Commands

- `joke`: Fetches and displays a random joke to lighten your mood.
- `roastme`: Roasts you with a random insult (Note: may contain offensive language).
- `curhealth`: Checks and displays the current system health, including memory usage and the number of running processes.
- `q` or `quit`: Exits the Goodshell.

## Prerequisites

Before you begin, ensure you have the following installed:

- A C/C++ Compiler (e.g., GCC, or the compiler included with Visual Studio)
- [CMake](https://cmake.org/download/) (version 3.21 or higher)
- [Python](https://www.python.org/downloads/)
- `pip` (Python package installer)

## How to Build and Run

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd goodshell
    ```

2.  **Install Python dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Build the C code with CMake:**
    ```bash
    mkdir build
    cd build
    cmake ..
    cmake --build .
    ```

4.  **Run Goodshell:**
    After a successful build, the executable will be located in the `build/Debug` or `build` directory.
    ```bash
    ./goodshell.exe
    ```

## Usage

Once Goodshell is running, you can type any of the custom commands or standard Windows commands and press Enter.