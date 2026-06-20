import json
from dataclasses import dataclass
from typing import List

@dataclass
class FileExplanation:
    file_name: str
    explanation: str
    technical_details: str

class CodeCompanion:
    def __init__(self, files: List[FileExplanation]):
        self.files = files
        self.progress = 0

    def get_file_explanation(self, file_name: str):
        for file in self.files:
            if file.file_name == file_name:
                return file.explanation
        return None

    def get_technical_details(self, file_name: str):
        for file in self.files:
            if file.file_name == file_name:
                return file.technical_details
        return None

    def update_progress(self):
        self.progress += 1

    def get_progress_percentage(self):
        return (self.progress / len(self.files)) * 100

def create_code_companion(files: List[FileExplanation]):
    return CodeCompanion(files)
