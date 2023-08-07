# noqa: INP001
from subprocess import check_call


def format() -> None:
    check_call(["ruff", "check", "--fix", "."])
    check_call(["black", "."])
    check_call(["isort", "."])
    check_call(
        [
            "autoflake",
            "--in-place",
            "--recursive",
            "--remove-all-unused-imports",
            "--remove-unused-variables",
            "--ignore-init-module-imports",
            ".",
        ]
    )


def lint() -> None:
    check_call(["ruff", "check", "."])
    check_call(["flake8", "."])
    check_call(["pylint", "src/lambda", "tests"])
    check_call(["mypy", "src", "tests"])
    check_call(["bandit", "-r", "src"])


def test() -> None:
    check_call(["pytest"])


def test_ci() -> None:
    check_call(
        [
            "pytest",
            "-v",
            "--cov=src",
            "--cov-branch",
            "--cov-report=xml:build/coverage.xml",
            "--cov-report=html:build/htmlcov",
            "--junitxml=build/tests.xml",
        ]
    )
