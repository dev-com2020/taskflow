from flask import Blueprint, jsonify, request

bp = Blueprint("tasks", __name__)

# In-memory storage
tasks = []


@bp.route("/tasks", methods=["GET"])
def get_tasks():
    pass


@bp.route("/tasks", methods=["POST"])
def create_task():
    content = request.json.get("content")
    if not content:
        return jsonify({"error": "Content is required"}), 400


@bp.route("/tasks/<int:task_id>", methods=["PATCH"])
def update_task(task_id):
    pass
