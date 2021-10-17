import os
# from app.db.database import arquivos

def get_current_directory(file_name):
    path = os.path.dirname(file_name)

    dados = os.listdir(path)

    return dados

def list_files_and_generate_em_in_txt():
    path='static/databases/17-10-2021'
    dados=os.listdir(path)
    print(dados)
    dados=list(map(lambda x: "databases/17-10-2021/"+x,dados))
    with open('static/databases.txt', 'w') as file:
        file.write(f'{dados}')
        print('done')
def main():
    list_files_and_generate_em_in_txt()
    # dados=list(map(lambda x: "databases/17-10-2021/"+x,arquivos))
    # print(dados)
    ...
if __name__ == '__main__':
    main()
