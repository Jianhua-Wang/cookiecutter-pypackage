"""Console script for {{cookiecutter.pkg_name}}."""

{% if cookiecutter.command_line_interface|lower == 'click' -%}
import click


@click.command()
def main():
    """Main entrypoint."""
    click.echo("{{ cookiecutter.project_slug }}")
    click.echo("=" * len("{{ cookiecutter.project_slug }}"))
    click.echo("{{ cookiecutter.project_short_description }}")


if __name__ == "__main__":
    main()  # pragma: no cover

{% elif cookiecutter.command_line_interface|lower == 'typer' -%}
import typer

app = typer.Typer()

def main():
    """Main entrypoint."""
    typer.echo("{{ cookiecutter.project_slug }}")
    typer.echo("=" * len("{{ cookiecutter.project_slug }}"))
    typer.echo("{{ cookiecutter.project_short_description }}")


if __name__ == "__main__":
   app(main)
{%- endif %}