import os
import shutil

pasta = "./fakefiles"

for arquivo in os.listdir(pasta):
    if arquivo.endswith(".doc"):
        shutil.move(f"{pasta})/{arquivo}",
                    f"{pasta})/doc/{arquivo}")
    elif arquivo.endswith(".pdf"):
        shutil.move(f"{pasta})/{arquivo}",
                    f"{pasta})/pdf/{arquivo}")
    elif arquivo.endswith(".html"):
        shutil.move(f"{pasta})/{arquivo}",
                    f"{pasta})/html/{arquivo}")
    elif arquivo.endswith(".xml"):
        shutil.move(f"{pasta})/{arquivo}",
                    f"{pasta})/xml/{arquivo}")



