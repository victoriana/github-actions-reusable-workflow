# GitHub Actions Reusable Workflow

A parameterized, reusable GitHub Action for standardizing CI/CD pipelines across an organization.

## Purpose
Organizations often struggle with inconsistent CI/CD practices across teams. This reusable workflow ensures that every repository follows the same security and testing standards by default.

## Features
- **Composite Action:** Combines testing, Docker building, and security scanning (Trivy) into a single step.
- **Parameterized:** Allows consumers to define Dockerfile paths, image names, and security severity thresholds.
- **OIDC Federation:** Demonstrates secure, passwordless authentication to cloud providers.

## Usage
1. Import this workflow into your `.github/workflows` directory.
2. Call the reusable workflow from your main CI file.
3. Customize parameters as needed.

## Status
This repo serves as a practical example of GitHub Actions governance and is part of the 12-week preparation plan for GitHub Staff.

## Related
- [agentic-eval-harness](https://github.com/victoriana/agentic-eval-harness) — evaluated by this template's governance
- [acrochoreo](https://github.com/victoriana/acrochoreo) — governed by this template
