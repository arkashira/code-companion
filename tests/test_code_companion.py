import pytest
from code_companion import CodeCompanion, Explanation


def test_explain_happy_path():
    code = """
def add(a, b):
    result = a + b
    return result
"""
    companion = CodeCompanion()
    explanations = companion.explain(code)

    # Expect three explanations (skip the leading blank line)
    assert len(explanations) == 3

    # Check each explanation content and description
    assert explanations[0].line_number == 2
    assert explanations[0].content.strip() == "def add(a, b):"
    assert "Defines a function named 'add'" in explanations[0].description

    assert explanations[1].line_number == 3
    assert explanations[1].content.strip() == "result = a + b"
    assert "Assigns a value to variable 'result'" in explanations[1].description

    assert explanations[2].line_number == 4
    assert explanations[2].content.strip() == "return result"
    assert "Returns a value" in explanations[2].description


def test_explain_edge_empty_string():
    companion = CodeCompanion()
    with pytest.raises(ValueError) as exc:
        companion.explain("")
    assert "must contain at least one non‑empty line" in str(exc.value)


def test_explain_ignores_blank_lines():
    code = "\n\nx = 1\n\n"
    companion = CodeCompanion()
    explanations = companion.explain(code)
    # Only one non‑blank line should be explained
    assert len(explanations) == 1
    assert explanations[0].content.strip() == "x = 1"
    assert "Assigns a value to variable 'x'" in explanations[0].description
