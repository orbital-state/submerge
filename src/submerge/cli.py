import typer
import logging
# from config import CONFIG

app = typer.Typer()

# Logger setup
logger = logging.getLogger("submerge")
handler = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)

def set_logging_level(verbosity: int):
    if verbosity == 0:
        logger.setLevel(logging.WARNING)
    elif verbosity == 1:
        logger.setLevel(logging.INFO)
    elif verbosity == 2:
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.NOTSET)
    logger.info(f"Logging level set to {logging.getLevelName(logger.level)}")

@app.command()
def version():
    """
    Display the version of the submerge CLI.
    """
    typer.echo(f"submerge version: {CONFIG['version']}")

@app.command()
def debug():
    """
    Run submerge in debugging mode.
    """
    logger.debug("Debugging mode activated.")
    typer.echo("Debugging mode is now active.")

@app.callback()
def main(
    verbose: int = typer.Option(
        0, "--verbose", "-v", count=True, help="Increase logging verbosity."
    )
):
    """
    submerge CLI: A tool for DIVE development.

    submerge is a prototype of a DIVE system that is:
    - Composable (prompt layering)
    - Context-aware (based on where you call it)
    - Reproducible (full prompt-response chain stored)
    - Human-in-the-loop (slow mode instead of raw agent autonomy)
    - Auditable (you can track prompt lineage and decision paths)
    - Git-friendly (purely file-based, versionable, portable)

    A real AI DevOps stack (without making the human obsolete!).
    """
    set_logging_level(verbose)
    logger.info("submerge CLI initialized.")

if __name__ == "__main__":
    app()