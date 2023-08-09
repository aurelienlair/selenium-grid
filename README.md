# Selenium Grid with Python and Docker experimentation project

This project is designed to provide a hands-on learning experience for using Selenium Grid, Python, and Docker to perform automated browser testing across multiple machines and browsers simultaneously. Selenium Grid is a powerful tool that enables distributed test execution, making it ideal for testing web applications at scale. By combining it with Python and Docker, we create a versatile and scalable testing environment that can be easily set up and deployed.

In this repository, you will find step-by-step instructions, code samples, and configurations to set up your own Selenium Grid infrastructure using Docker containers. 

## Disclaimer

**Note: The Docker images used in this project are specifically designed for ARM64 architectures. Please ensure that your system supports ARM64 before proceeding with the installation.**

## Table of Contents

1. [Pre-requirements](#pre-requirements)
2. [Installation](#installation)
6. [Monitoring the Selenium Grid](#monitoring-the-selenium-grid)
3. [Running Docker Images](#running-docker-images)
4. [Running Google Search](#running-google-search)
5. [Viewing Logs](#viewing-logs)

## Pre-requirements

To get started with this project, you'll need to install the following tools:

- [Python](https://www.python.org/): Python is a programming language used for writing test scripts and managing dependencies.
- [pyenv](https://github.com/pyenv/pyenv): pyenv is a tool that allows you to install and manage multiple versions of Python on your system.
- [pipenv](https://pipenv.pypa.io/): pipenv is a virtual environment manager and package installer for Python, ensuring dependency management and reproducibility.
- [Docker](https://www.docker.com/): Docker is a platform that allows you to develop, ship, and run applications inside containers, ensuring consistent environments across different machines.
- [Docker Compose](https://docs.docker.com/compose/): Docker Compose is a tool for defining and running multi-container Docker applications, simplifying the management of multiple Docker containers.
- [Visual Studio Code](https://code.visualstudio.com/): Visual Studio Code is a lightweight and powerful code editor with great support for Python development and a wide range of extensions.
- [Git](https://git-scm.com/): Git is a version control system used for tracking changes in your code and collaborating with others.

Please follow the links provided for each tool to access the respective installation instructions for your specific operating system. Once you have these tools installed, you'll be ready to proceed with the experimentation project.

## Installation

This chapter guides you through the installation process, ensuring that you have all the necessary tools and dependencies to run the project.

### Set Up Pipenv

Instructions for setting up Pipenv and creating a virtual environment within the project directory.

```bash
make install-virtual-env
```

And to activate the virtual environment

```bash
activate-virtual-env
```

## Running Docker Images

To launch the required Docker containers, use the following command:

```bash
make compose-up
```

## Monitoring the Selenium Grid

Before proceeding, make sure to add the following entry to your `/etc/hosts` file:

```bash
127.0.0.1 selenium-hub
```

Once done, you can monitor the Selenium Grid dashboard by executing the following command:

```bash
make open-selenium-grid-dashboard
```

## Running Google Search

This chapter provides instructions on running the Google search tests using different browsers, namely [Chrome](https://www.google.com/chrome) and [Firefox](https://www.mozilla.org/en-US/firefox/new/).

### Chrome

Execute the Google search tests with the Chrome browser.

```bash
BROWSER=chrome pytest tests/test_google_search.py
```

### Firefox

Run the Google search tests with the Firefox browser.

```bash
BROWSER=firefox pytest tests/test_google_search.py
```

## Viewing Logs

Find out how to view the logs of the Chrome and Firefox containers for troubleshooting and debugging.

### All Container logs

To view logs for all containers, you can use the following command:

```bash
make compose-logs
```

### Chrome Container Logs

Commands to view the logs of the Chrome container.

```bash
make compose-logs chrome
```

### Firefox Container Logs

Commands to view the logs of the Firefox container.

```bash
make compose-logs firefox 
```
