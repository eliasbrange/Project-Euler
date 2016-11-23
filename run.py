import click
from datetime import datetime

import problem_1
import problem_2
import problem_3
import problem_4
import problem_5
import problem_6
import problem_7


@click.group()
def euler():
    pass


@click.command(help='Run all problems')
@click.pass_context
def all(ctx):
    ctx.invoke(p1)
    ctx.invoke(p2)
    ctx.invoke(p3)
    ctx.invoke(p4)
    ctx.invoke(p5)
    ctx.invoke(p6)
    ctx.invoke(p7)


@click.command()
def p1():
    time = datetime.now()
    print_problem_header(1)
    problem_1.run()
    print_elapsed_time(time)


@click.command()
def p2():
    time = datetime.now()
    print_problem_header(2)
    problem_2.run()
    print_elapsed_time(time)


@click.command()
def p3():
    time = datetime.now()
    print_problem_header(3)
    problem_3.run()
    print_elapsed_time(time)


@click.command()
def p4():
    time = datetime.now()
    print_problem_header(4)
    problem_4.run()
    print_elapsed_time(time)


@click.command()
def p5():
    time = datetime.now()
    print_problem_header(5)
    problem_5.run()
    print_elapsed_time(time)


@click.command()
def p6():
    time = datetime.now()
    print_problem_header(6)
    problem_6.run()
    print_elapsed_time(time)


@click.command()
def p7():
    time = datetime.now()
    print_problem_header(7)
    problem_7.run()
    print_elapsed_time(time)


def print_problem_header(problem):
    print("################" + "#" * len(str(problem)))
    print("### Problem " + str(problem) + " ###")
    print("################" + "#" * len(str(problem)) + "\n")


def print_elapsed_time(time):
    elapsed_time = datetime.now() - time
    print("Elapsed time (ms): " + str(elapsed_time.total_seconds() * 1000) + "\n")


euler.add_command(all)
euler.add_command(p1)
euler.add_command(p2)
euler.add_command(p3)
euler.add_command(p4)
euler.add_command(p5)
euler.add_command(p6)
euler.add_command(p7)


if __name__ == '__main__':
    euler()
