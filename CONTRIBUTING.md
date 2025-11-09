# Contributing to AWS SLA Hunter

Thanks for your interest in contributing! We welcome all contributions.

## Ways to Contribute

### 1. Report Bugs
Create a GitHub issue with:
- What you expected to happen
- What actually happened
- Steps to reproduce
- Your Python version and OS

### 2. Suggest Features
Open an issue with:
- Problem the feature solves
- Proposed solution
- Use cases

### 3. Improve Documentation
- Fix typos
- Add clarifications
- Create tutorials

### 4. Submit Code

---

## Development Setup

### 1. Clone Repository
```bash
git clone https://github.com/yourusername/aws-sla-hunter.git
cd aws-sla-hunter
```

### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. Install Dev Dependencies
```bash
pip install -r requirements.txt
pip install pytest pytest-cov black flake8
```

### 4. Make Changes
```bash
git checkout -b feature/your-feature-name

# Make changes
python test_hunter.py
black main.py test_hunter.py
flake8 main.py test_hunter.py
```

### 5. Run Tests
```bash
python test_hunter.py
pytest test_hunter.py --cov=main --cov-report=html
```

### 6. Commit and Push
```bash
git add .
git commit -m "feat: brief description"
git push origin feature/your-feature-name
```

### 7. Create Pull Request
- Go to https://github.com/yourusername/aws-sla-hunter/pulls
- Click "New Pull Request"
- Write a clear description
- Reference any related issues

---

## Code Style

We follow PEP 8:

```python
# Good
def fetch_health_events() -> List[Dict[str, Any]]:
    """Fetch AWS Health events from last 90 days."""
    events = []
    return events

# Avoid
def fetchHealthEvents():
    events = []
    return events
```

**Guidelines:**
- Use `black` for formatting
- Max line length: 100 characters
- Use type hints
- Add docstrings to all functions
- Write tests for new features
- Use mock for AWS API calls
- Aim for 80%+ coverage

---

## Commit Message Format

```
Type: Brief description (50 chars max)

Longer explanation if needed (72 chars per line).

Fixes #123
Related to #456
```

**Types:**
- `feat` - New feature
- `fix` - Bug fix
- `docs` - Documentation
- `test` - Test additions
- `refactor` - Code reorganization
- `perf` - Performance improvement

---

## High Priority Improvements

- [ ] AWS Organizations support (multi-account)
- [ ] JSON/CSV export formats
- [ ] Custom date range filtering
- [ ] More error handling
- [ ] Better documentation

---

## Review Process

1. **Automated Checks** - Tests must pass, code style checked
2. **Code Review** - Constructive feedback from maintainers
3. **Approval** - Merge and release

---

## Community Guidelines

### Be Respectful
- Assume good intentions
- Welcome different perspectives
- Help each other learn

### Be Constructive
- Focus on code, not people
- Provide specific feedback
- Offer solutions

### Be Professional
- No spam
- Follow platform rules
- Report abuse

---

## Getting Help

- **Questions:** Create issue with "question" label
- **Setup issues:** See SETUP.md
- **Ideas:** Create issue with "enhancement" label
- **Bugs:** Create issue with "bug" label

---

## Recognition

Contributors will be:
- Added to README.md
- Mentioned in release notes
- Credited in CHANGELOG.md

---

## License

By contributing, you agree your contributions will be licensed under the MIT License.

---

## Questions?

Feel free to open a "question" issue or reach out to maintainers.

**We're here to help! 👋**

**Thank you for contributing to AWS SLA Hunter.**

Together we're building tools that help teams recover lost money and optimize cloud costs. Every contribution makes a difference.

Happy contributing! 🎉
