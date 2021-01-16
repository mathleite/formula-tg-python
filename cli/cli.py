import click


@click.group()
def cli():
    """A CLI wrapper for the API of Public APIs."""


@click.option('--driver', 'is_command', flag_value='driver', help='Create a Racer to the Race')
@click.option('--car', 'is_command', flag_value='car', help='Create a Car to the Race')
@cli.command()
def make(command: str):
    """List all Make APIs."""
    print(command)


if __name__ == "__main__":
    cli(prog_name='cli')
