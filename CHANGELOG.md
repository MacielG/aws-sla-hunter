# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Planned Features
- [ ] AWS Organizations support (multi-account scanning)
- [ ] JSON/CSV export formats
- [ ] Custom date range filtering (--days 30, --since 2025-01-01)
- [ ] Slack/Teams integration for alerts
- [ ] Email notifications
- [ ] Caching layer for faster re-runs
- [ ] Configuration file support (.sla-hunterrc)
- [ ] Docker image for containerized deployment
- [ ] Web UI (separate project)
- [ ] Performance optimizations for large accounts

---

## [0.1.0] - 2025-01-08

### Added
- Initial release of AWS SLA Hunter
- CLI tool to detect AWS Health events with SLA credit potential
- AWS Health API integration via boto3
- Beautiful terminal output using Rich library
- Error handling for common issues:
  - Missing AWS credentials
  - Access denied errors
  - AWS Health subscription requirements
- Event filtering (issue type, open/closed status)
- Event formatting (date, service, region, status, type)
- Call-to-action panel linking to awscostguardian.com
- Comprehensive unit tests with mock AWS data
- Screenshot generation for README
- Complete documentation:
  - README.md with badges and comparisons
  - QUICKSTART.md for fast setup
  - SETUP.md for installation help
  - CONTRIBUTING.md for community
  - LAUNCH_PLAN.md for growth strategy
- Marketing materials for multiple platforms:
  - Hacker News post template
  - Reddit r/aws post template
  - Reddit r/devops post template
  - Discord FinOps Brasil message
- Pre-written objection responses
- 7-day launch strategy with budget
- MIT License for open-source distribution
- Setup.py for PyPI distribution (future)

### Technical Details
- Python 3.8+ compatible
- ~550 lines of application code
- ~400 lines of test code
- 13 unit test cases
- Mock AWS Health API for testing
- No external API calls for authentication
- Respects AWS credential chain
- Zero data collection or telemetry

### Documentation Quality
- 400+ lines of README documentation
- Step-by-step quick start guide
- AWS permissions requirements documented
- Troubleshooting section with common errors
- Contributing guidelines
- Clear feature comparison with SaaS offering

### Launch Ready
- All files prepared for GitHub
- Marketing posts ready for community posting
- Growth strategy defined (organic + paid)
- Analytics framework (UTM parameters) ready
- Budget breakdown for R$100 ads campaign

---

## [0.2.0] - Planned (Month 1)

### Planned Features
- Multi-account AWS Organization support
- JSON export format
- CSV export format
- Advanced filtering (--service EC2, --region us-east-1)
- Performance improvements
- Additional error messages and help
- GitHub Actions CI/CD pipeline
- More comprehensive AWS Health event details

### Improvements
- Reduce startup time
- Better error messages
- More AWS service mappings
- Caching for faster re-runs

---

## [0.3.0] - Planned (Month 2)

### Planned Features
- Slack webhook integration for alerts
- Email notifications
- Configuration file support
- Scheduled execution (cron-like)
- History tracking (which events were claimed)
- Custom date ranges

### Improvements
- Web UI mockups
- API endpoint design
- Database schema for multi-account
- Performance benchmarks

---

## [1.0.0] - Planned (Month 3)

### Target Features
- Complete multi-account support
- All export formats (JSON, CSV, PDF mockup)
- Multiple notification channels
- Configuration management
- History and tracking
- Documentation website
- Community feedback integration

---

## Known Issues

### Current Release (0.1.0)
- No known issues. This is the initial release.

### To Report Issues
Please open a GitHub issue with:
1. Steps to reproduce
2. Expected behavior
3. Actual behavior
4. Your Python version and OS
5. Relevant error messages

---

## Security

### Reporting Security Issues
Please do **NOT** open a public issue for security vulnerabilities.

Instead, email security concerns to: `security@yourdomain.com` (TODO: Update)

We take security seriously and will respond promptly.

---

## Migration Guide

### From 0.1.0 to 0.2.0 (Planned)
- No breaking changes expected
- New features will be additive
- CLI parameters may be extended with `--flags`
- Existing scripts will continue to work

---

## Contributors

### 0.1.0
- Your Name (Initial release and project launch)

### Contributions Welcome!
See CONTRIBUTING.md for how to contribute.

---

## Version History Reference

| Version | Date | Type | Status |
|---------|------|------|--------|
| 0.1.0 | 2025-01-08 | Initial | ✅ Released |
| 0.2.0 | ~2025-02-08 | Features | 📋 Planned |
| 0.3.0 | ~2025-03-08 | Integration | 📋 Planned |
| 1.0.0 | ~2025-04-08 | Stable | 📋 Planned |

---

## Feedback & Suggestions

We're constantly improving. If you have ideas for:
- New features
- Performance improvements
- Better documentation
- UX enhancements
- Security improvements

Please open an issue or discussion!

---

## License

This project is licensed under the MIT License - see LICENSE file for details.

## Changelog Format

We follow [Keep a Changelog](https://keepachangelog.com/) format:
- `Added`: New features
- `Changed`: Changes in existing functionality
- `Deprecated`: Soon-to-be removed features
- `Removed`: Removed features
- `Fixed`: Bug fixes
- `Security`: Security updates

---

**Last Updated:** 2025-01-08

**Next Review:** 2025-02-08 (for 0.2.0 planning)
