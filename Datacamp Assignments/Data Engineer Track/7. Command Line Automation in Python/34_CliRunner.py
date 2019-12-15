# Invoking command line tests

# Not only has your department widely adopted click, but you are writing 
# click applications so quickly that you need to ensure you know how to 
# test them as well. The click framework has the ability to test itself 
# using the CliRunner method. Lead by example and extend this click 
# application so it can be tested properly and integrated into your 
# continuous integration system.

# Remember that click flags like --something need to be passed into 
# functions as something to use them in the function.

#define the click command
@click.command()
@click.option("--num", default=2, help="Number of clusters")
def run_cluster(num):
    result = main(num)
    click.echo(f'Cluster assignments: {result} for total clusters [{num}]')

# Create the click test runner
runner = CliRunner()

# Run the click app and assert it runs without error
result = runner.invoke(run_cluster, ['--num', '2'])
assert result.exit_code == 0
print(result.output)

# <script.py> output:
#     Cluster assignments: [1 1 0 1 1 0 1 0 0 1] for total clusters [2]

# Impressive work! You were able to use the CliRunner in click to programatically 
# invoke click and ensure it is behaving the way you expect it to. 
# You accomplished this by passing in a cluster number of 2 and 
# then asserting it returned exit status of 0. Click is a powerful 
# tool for both building and testing command-line applications in 
# Python and it was created by the author of the web framework Flask.

