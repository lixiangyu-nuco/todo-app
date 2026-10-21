from flask import Flask, render_template, request, redirect, url_for 

app = Flask(__name__)

# 1件のタスクを管理する
class Todo:
    def __init__(self, name):
        self.name = name
        self.done = False

# 複数のタスクを管理する
class TodoList:
    def __init__(self):
        self.tasks = []
        self.deleted_tasks = [] 

    # 新しいタスクを追加する
    def add(self, task_name):
        task = Todo(task_name)
        self.tasks.append(task)

    # タスクを完了状態にする
    def complete(self, task_id):
        self.tasks[task_id].done = True

    # タスクを削除する
    def delete(self, task_id):
        deleted_task = self.tasks.pop(task_id)
        self.deleted_tasks.append(deleted_task)

    # 完了したタスクを未完了に戻す
    def undo(self, task_id):
        self.tasks[task_id].done = False 

    # 削除したタスクを元に戻す
    def restore(self, task_id):
        restored_task = self.deleted_tasks.pop(task_id)
        self.tasks.append(restored_task)

# TodoListのインスタンスを作成する
todo_list = TodoList()

# トップページを表示する
@app.route("/")
def index():
    return render_template(
        "index.html", 
        tasks=todo_list.tasks,
        deleted_tasks=todo_list.deleted_tasks
    )

# タスクを削除する
@app.route("/delete/<int:task_id>", methods=["POST"])
def delete_task(task_id):
    todo_list.delete(task_id)
    return redirect("/")

# タスクを完了状態にする
@app.route("/complete/<int:task_id>", methods=["POST"])
def complete_task(task_id):
    todo_list.complete(task_id)
    return redirect("/")


#完了したタスクを未完了に戻す
@app.route("/undo/<int:task_id>",methods=["POST"])
def undo_task(task_id):
    todo_list.undo(task_id)
    return redirect("/")

# 新しいタスクを追加する
@app.route("/add", methods=["POST"])
def add_task():
    task_name = request.form.get("task_name")
    if task_name and task_name.strip():
        todo_list.add(task_name.strip())
    return redirect("/")

# 削除したタスクを元に戻す
@app.route("/restore/<int:task_id>", methods=["POST"])
def restore_task(task_id):
    todo_list.restore(task_id)
    return redirect("/")

# アプリを起動する
if __name__ == "__main__":
    app.run(debug=True)