from dataclasses import dataclass
import re
from typing import List


@dataclass
class Explanation:
    line_number: int
    content: str
    description: str


class CodeCompanion:
    """
    Provides simple, rule‑based explanations for Python code snippets.
    """

    _def_pattern = re.compile(r'^\s*def\s+([a-zA-Z_]\w*)\s*\(')
    _assign_pattern = re.compile(r'^\s*([a-zA-Z_]\w*)\s*=')

    def explain(self, code: str) -> List[Explanation]:
        """
        Analyse the given Python source code and return a list of
        Explanation objects, one per non‑empty line.

        Parameters
        ----------
        code: str
            Multiline Python source.

        Returns
        -------
        List[Explanation]

        Raises
        ------
        ValueError
            If ``code`` is empty or contains only whitespace.
        """
        if not code or not code.strip():
            raise ValueError("Code snippet must contain at least one non‑empty line.")

        explanations: List[Explanation] = []
        lines = code.splitlines()
        for idx, raw_line in enumerate(lines, start=1):
            line = raw_line.rstrip()
            if not line.strip():
                # skip blank lines but keep line numbers for consistency
                continue

            description = self._describe_line(line)
            explanations.append(Explanation(idx, line, description))
        return explanations

    def _describe_line(self, line: str) -> str:
        """Return a human‑readable description for a single line of code."""
        # Function definition
        m = self._def_pattern.match(line)
        if m:
            func_name = m.group(1)
            return f"Defines a function named '{func_name}'."

        # Variable assignment
        m = self._assign_pattern.match(line)
        if m:
            var_name = m.group(1)
            return f"Assigns a value to variable '{var_name}'."

        # Return statement
        if line.strip().startswith("return"):
            return "Returns a value from the current function."

        # Import statement
        if line.strip().startswith("import ") or line.strip().startswith("from "):
            return "Imports modules or objects."

        # Control flow
        if line.strip().startswith(("if ", "elif ", "else:", "for ", "while ")):
            return "Control flow statement."

        # Fallback
        return "Executes a statement."
