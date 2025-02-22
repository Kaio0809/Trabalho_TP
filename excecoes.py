
class UJCException(Exception):
    def __init__(self, usuario, *args):
        self.__usuario = usuario
        self.__mensagem = "Usuário Já cadastrado!"
        super().__init__(*args)

    def print_mensagem(self):
        print(f"{self.__mensagem}\nUsuário: {self.__usuario}")

class UNCException(Exception):
    def __init__(self, usuario, *args):
        self.__usuario = usuario
        self.__mensagem = "Usuário Não Cadastrado!"
        super().__init__(*args)
    
    def print_mensagem(self):
        print(f'{self.__mensagem}\nUsuário: {self.__usuario}')

class PPException(Exception):
    def __init__(self, usuario, *args):
        self.__usuario = usuario
        self.__mensagem = "Perfil Já Existente!"
        super().__init__(*args)
    
    def print_mensagem(self):
        print(f'{self.__mensagem}\nUsuário: {self.__usuario}')

class PDException(Exception):
    def __init__(self, usuario, *args):
        self.__usuario = usuario
        self.__mensagem = "Perfil Desativado!"
        super().__init__(*args)
    
    def print_mensagem(self):
        print(f'{self.__mensagem}\nUsuário: {self.__usuario}')

class PIException(Exception):
    def __init__(self, usuario, *args):
        self.__usuario = usuario
        self.__mensagem = "Perfil Inexistente!"
        super().__init__(*args)
    
    def print_mensagem(self):
        print(f'{self.__mensagem}\nUsuário: {self.__usuario}')

class MFPException(Exception):
    def __init__(self, tamanho, *args):
        self.__tamanho = tamanho
        self.__mensagem = "Mensagem Fora do Padrão!"
        super().__init__(*args)
    
    def print_mensagem(self):
        print(f'{self.__mensagem}\nMensagem de tamanho: {self.__tamanho}')

class SIException(Exception):
    def __init__(self, usuario, *args):
        self.__usuario = usuario
        self.__mensagem = "Seguidor Inválido!"
        super().__init__(*args)
    
    def print_mensagem(self):
        print(f'{self.__mensagem}\nSeguidor: {self.__usuario}')

