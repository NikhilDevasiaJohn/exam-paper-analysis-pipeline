import os

structure = [
    "data/raw",
    "data/processed",
    "data/labeled",
    "data/outputs",
    "config",
    "src/ingestion",
    "src/segmentation",
    "src/classification",
    "src/aggregation",
    "src/utils",
    "notebooks",
    "tests"
]

files = {
    "config/topics.json": '{\n  "topics": ["Calculus", "Algebra", "Geometry", "Probability"]\n}',
    "requirements.txt": "",
    "README.md": "# Exam Topic Classifier\n",
    "main.py": "from src.pipeline import run_pipeline\n\nif __name__ == '__main__':\n    run_pipeline()\n",
    "src/pipeline.py": "# Main pipeline logic\n\ndef run_pipeline():\n    print('Pipeline started')\n",
    "src/ingestion/pdf_loader.py": "",
    "src/ingestion/ocr.py": "",
    "src/segmentation/question_splitter.py": "",
    "src/classification/embedder.py": "",
    "src/classification/classifier.py": "",
    "src/classification/llm_fallback.py": "",
    "src/aggregation/aggregator.py": "",
    "src/utils/config_loader.py": "",
    "src/utils/logger.py": "",
    "src/utils/helpers.py": "",
    "tests/test_segmentation.py": "",
    "tests/test_classification.py": ""
}

# Create folders
for folder in structure:
    os.makedirs(folder, exist_ok=True)

# Create files (only if not exists)
for file_path, content in files.items():
    if not os.path.exists(file_path):
        with open(file_path, "w") as f:
            f.write(content)

print("✅ Project structure created inside current folder!")