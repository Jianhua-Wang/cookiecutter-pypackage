{% set is_open_source = cookiecutter.open_source_license != 'Not open source' -%}
# {{ cookiecutter.project_name }}

{% if is_open_source %}
[![pypi](https://img.shields.io/pypi/v/{{ cookiecutter.project_slug }}.svg)](https://pypi.org/project/{{ cookiecutter.project_slug }}/)
[![python](https://img.shields.io/pypi/pyversions/{{ cookiecutter.project_slug }}.svg)](https://pypi.org/project/{{ cookiecutter.project_slug }}/)
[![Build Status](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/actions/workflows/dev.yml/badge.svg)](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/actions/workflows/dev.yml)
[![codecov](https://codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/branch/main/graphs/badge.svg)](https://codecov.io/github/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }})

{%- if cookiecutter.open_source_license == 'MIT' %}
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
{%- elif cookiecutter.open_source_license == 'BSD-3-Clause' %}
[![License](https://img.shields.io/badge/License-BSD_3--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)
{%- elif cookiecutter.open_source_license == 'ISC' %}
[![License: ISC](https://img.shields.io/badge/License-ISC-blue.svg)](https://opensource.org/licenses/ISC)
{%- elif cookiecutter.open_source_license == 'Apache-2.0' %}
[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
{%- elif cookiecutter.open_source_license == 'GPL-3.0-only' %}
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
{% else %}
{%- endif %}

{% else %}
{% endif %}

{{ cookiecutter.project_short_description }}

{% if is_open_source %}
* Documentation: <https://{{ cookiecutter.github_username }}.github.io/{{ cookiecutter.project_slug }}>
* GitHub: <https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}>
* PyPI: <https://pypi.org/project/{{ cookiecutter.project_slug }}/>
* Free software: {{ cookiecutter.open_source_license }}
{% endif %}

## Features

* TODO

## Credits

This package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) and the [waynerv/cookiecutter-pypackage](https://github.com/waynerv/cookiecutter-pypackage) project template.
