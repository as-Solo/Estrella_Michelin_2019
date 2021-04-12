import os
def download_dataset():
    

    web = input("Página web de kaggle: ")
    
    documento = web.split("/")[-1]
    usuario = web.split("/")[-2]
    
    #Download, decompress and leaves only the csv
    download = f"kaggle datasets download -d {usuario}/{documento}"
    decompress = f"tar -xzvf {documento}.zip"
    delete = f"rm -rf {usuario}.zip"
    make_directory = "mkdir data"
    lista = "ls >> archivos.txt"
    
    for i in [download, decompress, delete, make_directory, lista]:
        os.system(i)
    
    move_and_delete = f"mv *.csv data/dataset.csv"
    return os.system(move_and_delete)


download_dataset()