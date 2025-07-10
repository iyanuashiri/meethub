# Contributing to this project

When contributing to this repository, please first discuss the change you wish to make via issue with the owners of this repository before making a change.
Please note we have a code of conduct, please follow it in all your interactions with the project.

### 2. Welcoming `CONTRIBUTING.md` for First-Timers

This guide is designed to be friendly and walk a new contributor through every step of the process.

```markdown
# Contributing to MeetHub

First off, thank you for considering contributing to MeetHub! 🎉 We're thrilled you're here. This project is a community effort, and every contribution, no matter how small, is valuable.

This guide will help you get started. Please don't hesitate to ask questions if anything is unclear.

## Code of Conduct

We have a [Code of Conduct](CODE_OF_CONDUCT.md) that we expect all contributors to adhere to. Please take a moment to read it. Our goal is to maintain a safe, welcoming, and inclusive environment for everyone.

## How Can I Contribute?

There are many ways to contribute to MeetHub, and many of them don't involve writing a single line of code!

*   **🐛 Reporting Bugs:** If you find a bug, please open an issue and let us know. Provide as much detail as possible, including steps to reproduce it.
*   **💡 Suggesting Enhancements:** Have an idea for a new feature or an improvement to an existing one? Open an issue to start a discussion.
*   **📝 Improving Documentation:** Good documentation is crucial. If you see a typo, an unclear explanation, or a missing section, please feel free to fix it.
*   **✅ Writing Tests:** We aim for high test coverage. Adding tests for existing code is an incredibly helpful contribution.
*   **💻 Writing Code:** Help us fix bugs or implement new features!

## Your First Code Contribution

Ready to write some code? Here’s how to set up your development environment and submit your first pull request.

### 1. Find an Issue to Work On

The best place to start is our [Issues tab](https://github.com/iyanuashiri/meethub/issues). We've labeled issues that are great for new contributors:

*   `good first issue`: These are small, well-defined tasks that are perfect for getting started.
*   `help wanted`: These are tasks that we'd love the community's help with.

If you see an issue you'd like to work on, leave a comment asking to be assigned to it.

### 2. Set Up Your Environment

*   **Fork the repository:** Click the "Fork" button at the top right of this page. This creates a copy of the project in your own GitHub account.
*   **Clone your fork:**
    ```bash
    git clone https://github.com/YOUR_USERNAME/meethub.git
    cd meethub
    ```
*   **Follow the installation instructions** in the [README.md](README.md) to get the project running locally.

### 3. Make Your Changes

*   **Create a new branch:** It's important to create a new branch for each feature or bug fix. This keeps your `main` branch clean.
    ```bash
    # Example branch names:
    # feature/add-social-sharing-buttons
    # fix/login-page-alignment-bug
    git checkout -b your-branch-name
    ```
*   **Write your code:** Make your changes to the code.
*   **Write or update tests:** If you're adding a new feature, please add tests for it. If you're fixing a bug, add a test that proves the bug is fixed.
*   **Run tests and linters:** Before you commit, make sure all tests and quality checks pass.
    ```bash
    # Run tests
    uv run pytest

    # Check for code style issues (if flake8 is configured)
    # uv run flake8 .
    ```

### 4. Submit Your Pull Request

*   **Commit your changes:** Use a clear and descriptive commit message.
    ```bash
    git add .
    git commit -m "feat: Add social sharing buttons to event detail page"
    ```
*   **Push your branch to your fork:**
    ```bash
    git push origin your-branch-name
    ```
*   **Open a Pull Request:** Go to your fork on GitHub and click the "Compare & pull request" button.
    *   Make sure you are opening a PR against the `develop` branch of the `iyanuashiri/meethub` repository.
    *   Provide a clear title and description for your PR. If it resolves an issue, include `Closes #123` in the description.

### 5. Code Review

Once you've submitted your PR, a maintainer will review it. We might ask for changes or improvements. This is a normal part of the process! We'll work with you to get your contribution merged.

Thank you again for your interest in contributing! We can't wait to see what you build.


### Pull Request Process

If you wish to make suggestions to this project's code, please keep this few considerations in mind before pushing your _Pull Requests_:

* Ensure any install or build dependencies are removed before the end of the layer when doing a build.
* Update the README.md with details of changes to the interface, this includes new environment variables, exposed ports, useful file locations and container parameters.
* This project code is a work in progress, so there is always room for improvement, but there is no need to impoverish the code base quality; have that in mind when submitting your suggestions and _Pull Requests_.
* Until a better release cycle is implemented,the branch _master_ is the most recent, most stable code base.
* Always push your _PR_ to _develop_ branch, any other will not be considered, and giving the case is easy to do, we guess there will be no difficulties with that.
* Any code submitted should have it's own UnitTest added inside the same code structure the project has right now.
* This projects uses Unittest, Coverage, Flake8 and PyLint for testing and static analysis, install them and use them for your development process.
* Before submitting code to the project, run Unittest on the code base.
* Before submitting code to the project, run Flake8 and PyLint (which we are still tuning so beware of false alarms there, if you detect them, feel free to fix it through your _PR_), look at the reports and fix those lines where there is need to.
* Try your best to validate your signature on GitHub, that way your commits will be signed and validated by the platform.

### Report Bugs

Report bugs at the issues section of [this project](https://github.com/iyanuashiri/meethub/issues).

If you find a bug, try your best to provide the necessary information to replicate the resulting error, the expected result and the actual one, if there is additional information you think will be useful, please add it, please include at least:

* Your operating system name and version.
* Any details about your local setup that might be helpful in troubleshooting.
* Detailed steps to reproduce the bug.

### Fix Bugs

Look through the GitHub issues for bugs. Anything tagged with "bug" is open to whoever wants to implement it.

### Implement Features

Look through the GitHub issues for features. Anything tagged with "feature" is open to whoever wants to implement it.

### Write Documentation

MeetHub could always use more documentation, whether as part of the official docs, in docstrings, or even on the web in blog posts, articles, and such.

### Submit Feedback

The best way to send feedback is to file an issue at the issues section of [this project](https://github.com/iyanuashiri/meethub/issues).

If you are proposing a feature:

* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.
* Remember that this is a volunteer-driven project, and that contributions are welcome :)

### Issues and support

We will try our best to provide help and orientation with this project implementation, but keep in mind than this is done in our spare time, and that has a lot of implications, please, be patient.
