"""
Setup script for packaging the chatbot as a Python module.
Run `pip install -e .` to install in editable mode.
"""

from setuptools import setup, find_packages

setup(
    name="ai-chatbot",
    version="1.0.0",
    author="AI-Generated Project",
    description="A simple AI-powered chatbot using Hugging Face Transformers",
    packages=find_packages(),
    install_requires=[
        "torch>=1.9.0",
        "transformers>=4.20.0",
        "numpy>=1.21.0",
        "tqdm"
    ],
    entry_points={
        "console_scripts": [
            "ai-chatbot=chatbot:main"
        ]
    },
    python_requires=">=3.8",
)
