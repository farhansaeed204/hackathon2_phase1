# Hackathon-2 Phase-1: Todo In-Memory Python Console App

A hackathon project for Phase I: Building a CLI todo app with in-memory storage using spec-driven, AI-only coding approach.

## Project Overview

This project implements a console-based todo application with the following features:
- Add new tasks
- Delete tasks
- Update task details
- View all tasks
- Mark tasks as complete/incomplete

Built using an agentic development approach with Claude Code as the primary implementation engine.

## Features

- **Interactive Console Interface**: Command-line interface that accepts user commands through input() and displays output via print()
- **Task Management**: Add, list, update, delete, and toggle tasks
- **In-Memory Storage**: All tasks are stored in memory with sequential ID assignment
- **Error Handling**: Comprehensive error handling for edge cases
- **Clean Exit**: Application exits cleanly when the "quit" command is entered

## Commands

- `add` - Add a new task with title and optional description
- `list` - Display all tasks with formatted output
- `update <id>` - Modify title and/or description of existing task
- `delete <id>` - Remove specified task with confirmation
- `toggle <id>` - Switch completion status of a task
- `quit` - Exit the application

## Getting Started

1. Ensure you have Python 3.13+ installed on your system
2. Clone this repository
3. Navigate to the project directory
4. Run the application:

```bash
python src/todo_app.py
```

The application will start an interactive console where you can manage your todo tasks.

## Example Usage

```
> add Buy groceries
Added task #1: Buy groceries

> add Complete project proposal Important project for work
Added task #2: Complete project proposal

> list

--- Todo List ---
  1 [ ] Buy groceries -
  2 [ ] Complete project proposal - Important project for work
-----------------

> toggle 1
Task #1 marked as completed.

> list

--- Todo List ---
  1 [x] Buy groceries -
  2 [ ] Complete project proposal - Important project for work
-----------------

> quit
Goodbye!
```

## Architecture

This project follows a specification-driven, AI-first development methodology:
1. **Specification**: All features begin with detailed specifications
2. **Planning**: Implementation plans are generated from specs
3. **Tasks**: Work is broken down into executable tasks
4. **AI Implementation**: Claude Code generates all code

## Project Structure

```
├── .specify/                 # Spec-Kit Plus configuration and templates
│   └── memory/
│       └── constitution.md   # Project constitution (governing principles)
├── specs/                    # Feature specifications
│   └── todo-app-spec.md      # Todo app feature specification
├── src/                      # Source code
│   └── todo_app.py          # Main application file
├── history/                  # Historical records
│   └── prompts/             # Prompt history records
├── README.md               # This file
├── CLAUDE.md               # Claude Code rules and instructions
└── requirements.txt        # Dependencies
```

## Prerequisites

- Python 3.13+
- Claude Code environment (for development)

## Development Approach

This project operates under the principles defined in [constitution.md](.specify/memory/constitution.md), which establishes:
- Spec-driven development mandate
- AI-only implementation approach
- Clean code and transparency requirements
- Innovation-focused hackathon objectives

## License

This project is part of a hackathon and is open source for educational purposes.