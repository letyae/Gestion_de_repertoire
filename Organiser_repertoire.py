from pathlib import Path
import typer 


def Organiser_repertoire(directory:str):
        """ Organiser  les fichiers de meme extension ds un meme repertoire"""  

        dict_rep={
            ".mp3":"Musique",
            ".wav":"Musique",
            ".flac" :"Musique",

            ".mp3":"Videos",
            ".avi":"Videos",
            ".mp4":"Videos",
            ".gif" : "Videos",

            ".bmp":"Images",
            ".png":"Images",
            ".jpg" :"Images",

            ".pdf":"Documents",
            ".docx":"Documents",
            ".txt":"Documents",
            ".pptx":"Documents",
            ".csv":"Documents",
            ".xls":"Documents",
            ".odp": "Documents",
            ".pages":"Documents"
        }

        #data_tree=Path.cwd()/'data' 

        data_tree = Path(directory)
        files = [f for f in data_tree.iterdir() if f.is_file]
       
        tree = data_tree.parent / "REPERTOIRE_TRIE" 
        tree.mkdir(exist_ok=True)
        typer.secho(f"Creation du repertoire: {tree}", bg=typer.colors.WHITE, fg=typer.colors.GREEN)
         

        for f in files:
            tree=data_tree.parent / "REPERTOIRE_TRIE" / dict_rep.get(f.suffix,"Autres")
            tree.mkdir(exist_ok=True)
            f.rename(tree/f.name)

