from setuptools import setup, find_packages

setup(
    name="insecure-llm-tester",
    version="0.2.0",
    packages=find_packages(),
    install_requires=[
        "fastapi",
        "uvicorn",
        "pydantic>=2",
        "python-dotenv",
        "httpx",
        "requests",
        "openai>=1.0.0",
        "Flask==3.1.2",
    ],
    entry_points={
        "console_scripts": [
            "llm-tester = insecure_llm_tester.cli:main",
        ],
    },
)
