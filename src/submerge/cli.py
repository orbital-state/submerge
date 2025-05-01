import typer
from .utils.logger import get_logger, set_logging_level, is_debug_mode

app = typer.Typer()

# Logger setup
logger = get_logger("submerge")

def _get_version():
    try:
        from importlib import metadata
        return metadata.version("kangaroo")
    except metadata.PackageNotFoundError:
        return "0.1.0" # default version

@app.command()
def version():
    pkg_version = _get_version()
    typer.echo(f"Version: {pkg_version}")

@app.command()
def debug():
    """
    Run submerge in debugging mode.
    """
    logger.debug("Debugging mode activated.")
    typer.echo("Debugging mode is now active.")

@app.command()
def status():
    """
    Check the status of the current thread.
    The root thread corresponds to `<project-root>/dive/` folder.
    """
    from .div.project import DivProject
    try:
        project = DivProject()
        project.load()
        current_node = project.current_node
        typer.echo(f"Current Node: {current_node.name}")
        typer.echo("Properties:")
        for prop_name, prop in current_node.properties.items():
            typer.echo(f"  - {prop_name}: {type(prop).__name__}")
    except Exception as error:
        typer.echo(f"Error checking status: {error}", err=True)
        if is_debug_mode(logger):
            raise error

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
    set_logging_level(logger, verbose)
    logger.info("submerge CLI initialized.")

if __name__ == "__main__":
    app()