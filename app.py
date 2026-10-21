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
        def add(self, task):
            self.tasks.append(task)

        # タスクを完了状態にする
        def complete(self, task_id):
            self.tasks[task_id].done = True

        # タスクを削除する
        def delete(self, task_id):
            deleted_task = self.tasks.pop(task_id)
            self.deleted_tasks.append(deleted_task)




# トップページを表示する
@app.route("/")
def index():
    return render_template(
        "index.html", 
        tasks=tasks,
        deleted_tasks=deleted_tasks 
    )

# タスクを削除する
@app.route("/delete/<int:task_id>", methods=["POST"])
def delete_task(task_id):
    if 0 <= task_id < len(tasks):
        deleted_task = tasks.pop(task_id)
        deleted_tasks.append(deleted_task)
    
    return redirect("/")

# タスクを完了・未完了に切り替える
@app.route("/complete/<int:task_id>", methods=["POST"])
def complete_task(task_id):
    if 0 <= task_id < len(tasks):
        tasks[task_id]["done"] = not tasks[task_id]["done"]
    return redirect("/")

#完了したタスクを未完了に戻す
@app.route("/undo/<int:task_id>",methods=["POST"])
def undo_task(task_id):
    if 0 <= task_id < len(tasks):
        tasks[task_id]["done"] = False 
    return redirect("/")

# 新しいタスクを追加する
@app.route("/add", methods=["POST"])
def add_task():
    task_name = request.form.get("task_name")

    if task_name and task_name.strip():
        tasks.append({
            "name": task_name.strip(),
            "done": False
        })

    return redirect("/")


# 削除したタスクを元に戻す
@app.route("/restore/<int:task_id>", methods=["POST"])
def restore_task(task_id):
    if 0 <= task_id < len(deleted_tasks):
        restored_task = deleted_tasks.pop(task_id)
        tasks.append(restored_task)

    return redirect("/")

# アプリを起動する
if __name__ == "__main__":
    app.run(debug=True)