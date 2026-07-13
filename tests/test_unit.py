import pytest
from app.models import Task


class TestTaskCreation:
    def test_valid_title_creates_task(self):
        task = Task(title="Test Task")
        assert task.title == "Test Task"
        assert task.done is False

    def test_title_is_stripped_of_whitespace(self):
        pass

    def test_empty_title_raises_value_error(self):
        pass

    def test_title_over_200_chars_raises_value_error(self):
        pass


class TestTaskCompletion:
    def test_complete_sets_done_to_true(self):
        pass

    def test_to_dict_contains_all_keys(self):
        pass
