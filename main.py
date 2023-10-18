import typer
from typing import Optional
from pathlib import Path

app=typer.Typer()

@app.command('run')
def main(extention: str,
         directory: Optional[str]=typer.Argument(None, help="Repertoire ds lequel chercher"),
         delete: bool=typer.Option(False,help="Supprime les fichiers trouvées")):
    """Affiche les fichiers trouvés avec son extension"""

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
        # puis lancer en ligne de cmde:  python main_01typer.py delete


if __name__=="__main__":
   #typer.run(main)
   app()

#en cmd taper les commande: 
#   python main run extension nom_repertoire 
#   python main search extension nom_repertoire 
#   python main delete extension nom_repertoire 