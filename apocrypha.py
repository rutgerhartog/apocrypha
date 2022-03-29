import typer
import modules.chisquare
import modules.entropy
import modules.montecarlo

app = typer.Typer()


@app.command()
def main(text: str):
    typer.echo(modules.entropy.shannon_entropy(text.encode("latin-1")))


app()
