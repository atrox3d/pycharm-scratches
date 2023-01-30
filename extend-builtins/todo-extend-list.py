
def create_todofile(filepath='todo.txt'):
    with open(filepath, 'w') as file:
        for lineno in range(10):
            file.write(f"line number {lineno}\n")
    return filepath


def delete_todofile(filepath='todo.txt'):
    from pathlib import Path
    todofile = Path(filepath)
    todofile.unlink()


class Todo(list):
    def __init__(self, filename):
        super(Todo, self).__init__([])
        self.filename = filename
        self.load()

    def load(self):
        try:
            with open(self.filename, 'r') as file:
                lines = [line.strip('\n') for line in file.readlines()]
                self.clear()
                self.extend(lines)
        except FileNotFoundError:
            print(f"file {self.filename} not found, initializing empty lists")
            self.clear()

    def save(self):
        with open(self.filename, 'w') as file:
            for line in self:
                file.write(f"{line}\n")

    def complete(self, item):
        if isinstance(item, int):
            item = self[item]
        self.remove(item)
        self.save()


todo = Todo("todo.txt")
print(todo)
todo.append("testing testing")
todo.save()
todo.load()
print(todo)

create_todofile()
todo.load()
print(todo)
todo.complete(0)
print(todo)
todo.complete('line number 1')
print(todo)
todo.load()
print(todo)

delete_todofile()
