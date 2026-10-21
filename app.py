from flask import Flask, render_template, redirect

app = Flask(__name__)

# タスクを保存するリスト
tasks = [
    {"name": "pythonの勉強", "done": False},
    {"name": "Flaskの勉強", "done": False},
    {"name": "ToDoリストの作成", "done": False}
]
@app.route("/")
def index():
    return render_template("index.html", tasks=tasks)

@app.route("/delete/<int:task_id>", methods=["POST"])
def delete_task(task_id):
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
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

