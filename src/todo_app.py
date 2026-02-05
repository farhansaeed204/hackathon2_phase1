#!/usr/bin/env python3
"""
Todo In-Memory Python Console App
Implementation based on the specification v1.0
"""

import sys
from typing import Dict, List, Optional


class Task:
    """Represents a single task in the todo list."""

    def __init__(self, task_id: int, title: str, description: str = "", completed: bool = False):
        self.id = task_id
        self.title = title.strip()
        self.description = description
        self.completed = completed

    def __repr__(self):
        status = "[x]" if self.completed else "[ ]"
        desc_preview = self.description[:50]
        if len(self.description) > 50:
            desc_preview += "..."
        return f"{self.id:3d} {status} {self.title} - {desc_preview}"


class TodoApp:
    """Main todo application class."""

    def __init__(self):
        self.tasks: Dict[int, Task] = {}
        self.next_id = 1
        self.running = True

    def _validate_title(self, title: str) -> bool:
        """Validate that the title is not empty or whitespace only."""
        return bool(title.strip())

    def _get_next_id(self) -> int:
        """Get the next available ID and increment the counter."""
        current_id = self.next_id
        self.next_id += 1
        return current_id

    def _parse_command(self, user_input: str) -> tuple:
        """Parse user command into action and parameters."""
        parts = user_input.strip().split()
        if not parts:
            return "unknown", []

        command = parts[0].lower()
        params = parts[1:]

        return command, params

    def add_task(self, title: str, description: str = "") -> None:
        """Add a new task to the todo list."""
        if not self._validate_title(title):
            print("Title cannot be empty. Please enter a valid title.")
            return

        task_id = self._get_next_id()
        task = Task(task_id, title, description)
        self.tasks[task_id] = task
        print(f"Added task #{task_id}: {title}")

    def list_tasks(self) -> None:
        """Display all tasks in the todo list."""
        if not self.tasks:
            print("No tasks found.")
            return

        print("\n--- Todo List ---")
        for task_id in sorted(self.tasks.keys()):
            task = self.tasks[task_id]
            status = "[x]" if task.completed else "[ ]"
            desc_preview = task.description[:50]
            if len(task.description) > 50:
                desc_preview += "..."
            print(f"{task.id:3d} {status} {task.title} - {desc_preview}")
        print("-----------------\n")

    def update_task(self, task_id: int, title: Optional[str] = None, description: Optional[str] = None) -> None:
        """Update an existing task."""
        if task_id not in self.tasks:
            print(f"Task ID {task_id} not found.")
            return

        task = self.tasks[task_id]

        if title is not None:
            if not self._validate_title(title):
                print("Title cannot be empty.")
                return
            task.title = title.strip()

        if description is not None:
            task.description = description

        print(f"Updated task #{task_id}")

    def delete_task(self, task_id: int) -> None:
        """Delete a task from the todo list."""
        if task_id not in self.tasks:
            print(f"Task ID {task_id} not found.")
            return

        # Ask for confirmation
        confirmation = input(f"Are you sure you want to delete task {task_id}? (y/n): ").strip().lower()
        if confirmation in ['y', 'yes']:
            del self.tasks[task_id]
            print(f"Deleted task #{task_id}")

            # Adjust IDs if needed (decrement higher IDs)
            new_tasks = {}
            new_id_counter = 1
            for old_id in sorted(self.tasks.keys()):
                task = self.tasks[old_id]
                task.id = new_id_counter
                new_tasks[new_id_counter] = task
                new_id_counter += 1

            self.tasks = new_tasks
            self.next_id = new_id_counter
        else:
            print("Deletion cancelled.")

    def toggle_task(self, task_id: int) -> None:
        """Toggle the completion status of a task."""
        if task_id not in self.tasks:
            print(f"Task ID {task_id} not found.")
            return

        task = self.tasks[task_id]
        task.completed = not task.completed
        status = "completed" if task.completed else "incomplete"
        print(f"Task #{task_id} marked as {status}.")

    def handle_add_command(self, params: List[str]) -> None:
        """Handle the add command."""
        if not params:
            title = input("Enter task title: ").strip()
        else:
            title = " ".join(params)

        description = ""
        if len(params) == 0:
            description = input("Enter task description (optional): ")

        self.add_task(title, description)

    def handle_list_command(self, params: List[str]) -> None:
        """Handle the list command."""
        if params:
            print("The list command doesn't take any parameters.")
            return
        self.list_tasks()

    def handle_update_command(self, params: List[str]) -> None:
        """Handle the update command."""
        if len(params) < 1:
            print("Usage: update <id> [title] [description]")
            return

        try:
            task_id = int(params[0])
        except ValueError:
            print("Invalid task ID. Please provide a numeric ID.")
            return

        if len(params) < 2:
            # If only ID is provided, ask for new title
            new_title = input(f"Enter new title for task {task_id} (leave blank to keep current): ").strip()
            new_desc = input(f"Enter new description for task {task_id} (leave blank to keep current): ")

            title_param = new_title if new_title else None
            desc_param = new_desc if new_desc else None

            self.update_task(task_id, title_param, desc_param)
        else:
            # Update with provided title and description
            title_param = " ".join(params[1:]) if params[1:] else None
            self.update_task(task_id, title_param, None)

    def handle_delete_command(self, params: List[str]) -> None:
        """Handle the delete command."""
        if len(params) != 1:
            print("Usage: delete <id>")
            return

        try:
            task_id = int(params[0])
            self.delete_task(task_id)
        except ValueError:
            print("Invalid task ID. Please provide a numeric ID.")

    def handle_toggle_command(self, params: List[str]) -> None:
        """Handle the toggle command."""
        if len(params) != 1:
            print("Usage: toggle <id>")
            return

        try:
            task_id = int(params[0])
            self.toggle_task(task_id)
        except ValueError:
            print("Invalid task ID. Please provide a numeric ID.")

    def handle_quit_command(self, params: List[str]) -> None:
        """Handle the quit command."""
        if params:
            print("The quit command doesn't take any parameters.")
            return
        self.running = False
        print("Goodbye!")

    def handle_unknown_command(self, command: str) -> None:
        """Handle unknown commands."""
        print("Unknown command. Available commands: add, list, update, delete, toggle, quit")

    def run(self) -> None:
        """Main application loop."""
        print("Welcome to the Todo App!")
        print("Available commands: add, list, update, delete, toggle, quit")

        while self.running:
            try:
                user_input = input("> ").strip()

                if not user_input:
                    continue

                command, params = self._parse_command(user_input)

                if command == "add":
                    self.handle_add_command(params)
                elif command == "list":
                    self.handle_list_command(params)
                elif command == "update":
                    self.handle_update_command(params)
                elif command == "delete":
                    self.handle_delete_command(params)
                elif command == "toggle":
                    self.handle_toggle_command(params)
                elif command == "quit":
                    self.handle_quit_command(params)
                else:
                    self.handle_unknown_command(command)

            except KeyboardInterrupt:
                print("\nGoodbye!")
                break
            except EOFError:
                print("\nGoodbye!")
                break


def main():
    """Entry point for the application."""
    app = TodoApp()
    app.run()


if __name__ == "__main__":
    main()