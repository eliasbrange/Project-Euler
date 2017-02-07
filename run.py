import fnmatch
import os
import importlib
import click


@click.group()
def main():
    pass


@click.command(help='Run all problems')
@click.pass_context
def all(ctx):
    for file in os.listdir('.'):
        if fnmatch.fnmatch(file, 'p*.py'):
            module = importlib.import_module(file.replace('.py', ''))
            module.run()


@click.command(help='Run a single problem')
@click.option('--problem', help='Which problem to run')
def run(problem):
    module = importlib.import_module("p{:03d}".format(int(problem)))
    module.run()


main.add_command(all)
main.add_command(run)


if __name__ == "__main__":
    main()
