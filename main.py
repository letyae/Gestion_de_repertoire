import typer
from typing import Optional
from pathlib import Path

from Organiser_repertoire import Organiser_repertoire

app=typer.Typer()

@app.command('run')
def main(extention: str="",
         directory: Optional[str]=typer.Argument(None, help="Repertoire ds lequel chercher"),
         delete: bool=typer.Option(False,help="Supprime les fichiers trouvées")):

    """Affiche les fichiers trouvés avec son extension"""
    print(f"*** {directory} ********")

    if  directory:
        directory=Path(directory)
    else:
        directory=Path.cwd()
    if not directory.exists():
       typer.secho(f"Le dossier '{directory}' n'existe pas.", fg=typer.colors.RED)
       raise typer.Exit()
    files=directory.rglob(f"*.{extention}")

    if delete:
        typer.confirm("Voulez vs vraiment supprimer tous les fichiers trouvés ?", abort=True)
        for file in files:
            file.unlink() #suppression du fichier
            typer.secho(f"Suppression du fichier {file}.",fg=typer.colors.RED)
    else:
        typer.secho(f"Fichier trouvé avec l'extension {extention} :",bg=typer.colors.BLUE, fg=typer.colors.WHITE)
        for file in files:
            typer.echo(file)


@app.command()
def search(extension:str,directory:str):
    """ Recherche de fichier avec l'extension donné"""
    
    main(extension, directory, delete=False)
    
@app.command()
def delete(extension:str, directory:str):
    """ Suppression de fichier avec l'extension donné"""
    
    main(extension, directory, delete=True,)

@app.command()      
def trie(directory:str):
    """ Organiser tous les fichiers de meme extension ds un meme repertoire"""  

    Organiser_repertoire(directory)

if __name__=="__main__":
   #typer.run(main)
   app()

