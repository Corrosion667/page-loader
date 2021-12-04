# Page loader

[![Actions Status](https://github.com/Corrosion667/python-project-lvl3/workflows/hexlet-check/badge.svg)](https://github.com/Corrosion667/python-project-lvl3/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/9c10bf2782c008661ef5/maintainability)](https://codeclimate.com/github/Corrosion667/python-project-lvl3/maintainability)
[![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-000000.svg)](https://github.com/wemake-services/wemake-python-styleguide)
[![linter-and-test-check](https://github.com/Corrosion667/python-project-lvl3/actions/workflows/linter-and-test-check.yml/badge.svg)](https://github.com/Corrosion667/python-project-lvl3/actions/workflows/linter-and-test-check.yml)
[![Test Coverage](https://api.codeclimate.com/v1/badges/9c10bf2782c008661ef5/test_coverage)](https://codeclimate.com/github/Corrosion667/python-project-lvl3/test_coverage)

---

## Basic information

**Page loader** downloads the web page allowing user to open it offline. This is achieved due to the fact that the program also downloads local resources of the web page to the computer. Web page is downloaded to the directory chosen by user or by default to the current working directory.

## Quickstart

**Page loader** at the moment is stored only at *github* so the quickest and the easiest way to install it is to use *pip* with URL of repository.
```bash
pip install git+https://github.com/Corrosion667/python-project-lvl3.git
```

## Running

Basic **Page loader** syntax looks like this:
```bash
page-loader --output url
```
*output* is an optional argument which means a folder where to download the page. By default it is to current working directory.

You can also recall about main features and syntax of a program using *help command*:
```bash
page-loader -h
```

## Asciinema demonstration:

Installing the whole package and main features of the programm are demonstrated in the asciinema below: