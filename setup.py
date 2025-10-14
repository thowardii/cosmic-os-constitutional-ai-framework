"""
Cosmic OS Constitutional AI Framework
======================================

Setup configuration for the package.
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read README for long description
readme_path = Path(__file__).parent / "README.md"
long_description = readme_path.read_text(encoding="utf-8") if readme_path.exists() else ""

setup(
    name="cosmic-os-constitutional-ai",
    version="1.0.0",
    author="Cosmic OS Community",
    description="Constitutional AI governance framework with local-first architecture, zero-knowledge encryption, and Byzantine consensus",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/thowardii/cosmic-os-constitutional-ai-framework",
    packages=find_packages(exclude=["tests", "examples"]),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Security :: Cryptography",
        "Topic :: System :: Distributed Computing",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.9",
    install_requires=[
        "numpy>=1.24.0",
        "cryptography>=41.0.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.4.0",
            "pytest-asyncio>=0.21.0",
            "pytest-cov>=4.1.0",
            "black>=23.0.0",
            "mypy>=1.5.0",
            "flake8>=6.1.0",
            "isort>=5.12.0",
        ],
        "docs": [
            "mkdocs>=1.5.0",
            "mkdocs-material>=9.4.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "cosmic-os-validate=cosmic_os.cli:validate",
        ],
    },
    project_urls={
        "Bug Reports": "https://github.com/thowardii/cosmic-os-constitutional-ai-framework/issues",
        "Source": "https://github.com/thowardii/cosmic-os-constitutional-ai-framework",
        "Documentation": "https://github.com/thowardii/cosmic-os-constitutional-ai-framework/blob/main/README.md",
        "Discussions": "https://github.com/thowardii/cosmic-os-constitutional-ai-framework/discussions",
    },
    keywords="ai governance constitutional privacy encryption consensus democracy",
    package_data={
        "cosmic_os": ["py.typed"],
    },
    include_package_data=True,
    zip_safe=False,
)
