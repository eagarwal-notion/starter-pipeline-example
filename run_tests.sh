#!/bin/bash
set -e

echo "🧪 Setting up Python environment with uv..."
uv sync

echo "🚀 Running rocket tests with JUnit XML output..."
uv run python -m pytest test_rocket.py --junitxml=test-results.xml --verbose

echo "✅ Tests completed! JUnit XML report generated at test-results.xml"