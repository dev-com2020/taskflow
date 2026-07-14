from flask import Blueprint, jsonify, request, abort

bp = Blueprint("tasks", __name__)

# In-memory storage
tasks = []


@bp.route("/tasks", methods=["GET"])
def get_tasks():
    items = [{"id": i + 1, "content": task} for i, task in enumerate(tasks)]
    return jsonify(items)


@bp.route("/tasks", methods=["POST"])
def create_task():
    data = request.get_json(silent=True) or {}
    content = data.get("content")
    if not content:
        return jsonify({"error": "Content is required"}), 400

    # create and store the task
    tasks.append(content)
    new_task = {"id": len(tasks), "content": content}
    return jsonify(new_task), 201


@bp.route("/tasks/<int:task_id>", methods=["PATCH"])
def update_task(task_id):
    if task_id < 1 or task_id > len(tasks):
        return jsonify({"error": "Task not found"}), 404

    data = request.get_json(silent=True) or {}
    content = data.get("content")
    if content is None:
        return jsonify({"error": "Content is required"}), 400

    tasks[task_id - 1] = content
    updated = {"id": task_id, "content": content}
    return jsonify(updated)
