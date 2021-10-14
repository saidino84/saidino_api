import os
# from app.db.database import arquivos

def get_current_directory(file_name):
    path = os.path.dirname(file_name)

    dados = os.listdir(path)

    return dados

def list_files_and_generate_em_in_txt():
    path='static/databases'
    # dados=os.listdir(path)
    # print(dados)
    # dados=list(map(lambda x: "databases/"+x,arquivos))
    # with open('static/databases.txt', 'a') as file:
    #     file.write(f'{dados}')
    #     print('done')
def main():
    # list_files_and_generate_em_in_txt()
    # dados=list(map(lambda x: "databases/"+x,arquivos))
    # print(dados)
    ...
if __name__ == '__main__':
    main()
