from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory database
tasks = []

@app.route("/tasks", methods=["GET"])
def get_tasks():
    """Retrieve all tasks."""
    return jsonify(tasks)

@app.route("/tasks", methods=["POST"])
def add_task():
    """Add a new task."""
    task_data = request.json
    if "task" not in task_data:
        return jsonify({"error": "Task is required"}), 400
    task = {"id": len(tasks) + 1, "task": task_data["task"]}
    tasks.append(task)
    return jsonify(task), 201

@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    """Delete a task by ID."""
    global tasks
    tasks = [task for task in tasks if task["id"] != task_id]
    return jsonify({"message": "Task deleted"}), 200

if __name__ == "__main__":
    app.run(debug=True)
