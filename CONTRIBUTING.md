# Contributing to AWS SLA Hunter

Thanks for your interest in contributing! We welcome all contributions, from bug reports to feature implementations.

## Ways to Contribute

### 1. Report Bugs
Found an issue? Create a GitHub issue with:
- What you expected to happen
- What actually happened
- Steps to reproduce
- Your Python version and OS
- Output of `python main.py --version` (if applicable)

### 2. Suggest Features
Have an idea? Open an issue with:
- Problem the feature solves
- Proposed solution
- Alternatives you've considered
- Use cases where this would help

### 3. Improve Documentation
- Fix typos in README, SETUP.md, etc.
- Add clarifications
- Create tutorials or examples
- Translate documentation

### 4. Submit Code
See "Development Setup" below.

---

## Development Setup

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/aws-sla-hunter.git
cd aws-sla-hunter
```

### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Development Dependencies
```bash
pip install -r requirements.txt
pip install pytest pytest-cov black flake8  # Dev dependencies
```

### 4. Make Your Changes
```bash
# Create a feature branch
git checkout -b feature/your-feature-name

# Make changes
# Test your changes
python test_hunter.py

# Format code
black main.py test_hunter.py

# Check code style
flake8 main.py test_hunter.py
```

### 5. Run Tests
```bash
# Run all tests
python test_hunter.py

# Run with coverage
pytest test_hunter.py --cov=main --cov-report=html
```

### 6. Commit and Push
```bash
git add .
git commit -m "Add: brief description of your change"
git push origin feature/your-feature-name
```

### 7. Create Pull Request
- Go to https://github.com/yourusername/aws-sla-hunter/pulls
- Click "New Pull Request"
- Select your branch
- Write a clear description
- Reference any related issues (#123)

---

## Code Style

We follow PEP 8 with these additions:

### Python Style
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

### Formatting
- Use `black` for formatting
- Max line length: 100 characters
- Use type hints where practical
- Add docstrings to all functions

### Testing
- Write tests for new features
- Use mock for AWS API calls
- Aim for 80%+ coverage
- Test both success and error paths

---

## Commit Message Format

```
Type: Brief description (50 chars or less)

Longer explanation if needed (72 chars per line).

Fixes #123
Related to #456
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation
- `style`: Formatting
- `test`: Test additions
- `refactor`: Code reorganization
- `perf`: Performance improvement
- `chore`: Build, deps, etc.

---

## What We're Looking For

### High Priority
- [ ] AWS Organizations support (multi-account)
- [ ] JSON/CSV export formats
- [ ] Custom date range filtering
- [ ] Error handling improvements
- [ ] Documentation improvements

### Medium Priority
- [ ] Slack/Teams integration
- [ ] Email notifications
- [ ] Caching layer for performance
- [ ] Additional AWS services
- [ ] Configuration file support

### Nice to Have
- [ ] Docker image
- [ ] Web UI (separate project)
- [ ] API server version
- [ ] Performance optimizations
- [ ] More AWS services

---

## Review Process

1. **Automated Checks**
   - Tests must pass
   - Code style (black, flake8)
   - Coverage shouldn't decrease

2. **Code Review**
   - At least one maintainer review
   - Constructive feedback
   - Discussion of approach

3. **Approval**
   - Merge into main
   - Tag as release
   - Update changelog

---

## Release Process

We use semantic versioning (MAJOR.MINOR.PATCH):
- **MAJOR**: Breaking changes
- **MINOR**: New features (backward compatible)
- **PATCH**: Bug fixes

Releases happen approximately every 2 weeks.

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

### Be Inclusive
- Welcome all experience levels
- Be patient with questions
- Help new contributors

### Be Professional
- No spam or self-promotion
- Follow platform rules
- Report abuse to maintainers

---

## Getting Help

- **Questions:** Create an issue with "question" label
- **Setup issues:** See SETUP.md
- **Ideas:** Create issue with "enhancement" label
- **Bugs:** Create issue with "bug" label
- **Chat:** Join our Discord (if available)

---

## Recognition

Contributors will be:
- Added to README.md contributors list
- Mentioned in release notes
- Recognized in GitHub insights
- Credited in CHANGELOG.md

---

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

## Troubleshooting

### Tests failing?
```bash
# Make sure you have all dependencies
pip install -r requirements.txt

# Check Python version (need 3.8+)
python --version

# Run with verbose output
python -m pytest test_hunter.py -v
```

### Import errors?
```bash
# Make sure you're in the right directory
pwd  # Should be aws-sla-hunter/

# Make sure virtual environment is activated
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

### Code style issues?
```bash
# Auto-fix with black
black main.py test_hunter.py

# Check with flake8
flake8 main.py test_hunter.py --max-line-length=100
```

---

## Questions?

Feel free to:
- Open a "question" issue
- Comment on existing discussions
- Reach out to maintainers

We're here to help! 👋

---

## Thanks!

Thank you for contributing to AWS SLA Hunter. Together we're building tools that help teams recover lost money and optimize cloud costs. Every contribution, no matter how small, makes a difference.

Happy contributing! 🎉
