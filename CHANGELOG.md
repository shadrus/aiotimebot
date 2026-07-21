# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project follows [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.1] - 2026-07-21

### Added

- Complete generated async coverage for all 470 Time Messenger API v4 REST
  operations.
- High-level `TimeClient`, WebSocket event runtime, routing, middleware,
  bounded dispatch, retries, and optional in-memory state.
- Compatibility workarounds for the observed Time 7.8 protocol behavior.
- User documentation, strict static checks, reproducible API generation, and
  automated PyPI release workflows.

### Changed

- Require Python 3.13 or newer and test the package on Python 3.13 and 3.14.

[Unreleased]: https://github.com/shadrus/aiotimebot/compare/v0.1.1...HEAD
[0.1.1]: https://github.com/shadrus/aiotimebot/compare/v0.1.0...v0.1.1
