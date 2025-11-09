from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="aws-sla-hunter",
    version="0.1.0",
    author="Your Name",
    author_email="your@email.com",
    description="Find missed AWS SLA credits in your account with a single command",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/aws-sla-hunter",
    py_modules=["main"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: System :: Monitoring",
        "Topic :: Office/Business :: Financial",
        "Intended Audience :: System Administrators",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Environment :: Console",
    ],
    python_requires=">=3.8",
    install_requires=[
        "boto3>=1.26.0",
        "botocore>=1.29.0",
        "rich>=13.0.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0",
            "pytest-cov>=4.0",
            "black>=23.0",
            "flake8>=6.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "aws-sla-hunter=main:main",
        ],
    },
    keywords="aws sla credit cloud cost monitoring devops finops",
    project_urls={
        "Bug Reports": "https://github.com/yourusername/aws-sla-hunter/issues",
        "Source": "https://github.com/yourusername/aws-sla-hunter",
        "Documentation": "https://github.com/yourusername/aws-sla-hunter#readme",
    },
)
