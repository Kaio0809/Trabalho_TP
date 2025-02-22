import datetime
from funcoes_aux import gerador, ordenar_pela_data
from excecoes import UJCException, UNCException, PPException, PDException, PIException, MFPException, SIException

gerador_id = gerador()

class Tweet():
    def __init__(self, usuario: str, mensagem: str) -> None:
        self.__id = next(gerador_id)
        self.__usuario = usuario
        self.__mensagem = mensagem
        self.__data_postagem = datetime.datetime.now()
    
    def get_id(self) -> int:
        return self.__id
    
    def get_usuario(self) -> str:
        return self.__usuario
    
    def get_mensagem(self) -> str:
        return self.__mensagem
    
    def get_data_postagem(self):
        return self.__data_postagem

class Perfil():
    def __init__(self, usuario: str):
        self.__usuario = usuario
        self.__seguidos = []
        self.__seguidores = []
        self.__tweets = []
        self.__ativo = True
    
    def add_seguidor(self, seguidor):
        self.__seguidores.append(seguidor)

    def seguidores(self):
        return self.__seguidores

    def add_seguidos(self, seguido):
        self.__seguidos.append(seguido)

    def seguidos(self):
        return self.__seguidos
    
    def add_tweet(self, tweet):
        self.__tweets.append(tweet)
    
    def get_tweets(self):
        tweets = ordenar_pela_data(self.__tweets)
        return tweets
    
    def get_tweet(self, id):
        for tweet in self.__tweets:
            if id == tweet.get_id():
                return tweet
        return None
    
    def get_timeline(self):
        tweets = self.__tweets
        for perfil in self.__seguidos:
            tweets += perfil.get_tweets()
        
        timeline = ordenar_pela_data(tweets)
        return timeline
    
    def set_usuario(self, usuario):
        self.__usuario = usuario
    
    def get_usuario(self):
        return self.__usuario
    
    def set_ativo(self, ativo: bool):
        self.__ativo = ativo
    
    def is_ativo(self):
        return self.__ativo
    
class PessoaFisica(Perfil):
    def __init__(self, usuario, cpf):
        super().__init__(usuario)
        self.__cpf = cpf
    
    def get_cpf(self):
        return self.__cpf
    
class PessoaJuridica(Perfil):
    def __init__(self, usuario, cnpj):
        super().__init__(usuario)
        self.__cnpj = cnpj
    
    def get_cnpj(self):
        return self.__cnpj

class RepositoriosUsuarios():
    def __init__(self):
        self.__usuarios = []
    
    def cadastrar(self, perfil: Perfil):
        if self.buscar(perfil.get_usuario()) is not None:
            raise UJCException(perfil.get_usuario())
        self.__usuarios.append(perfil)
    
    def buscar(self, usuario):
        for perfil in self.__usuarios:
            if perfil.get_usuario() == usuario:
                return perfil
        return None
    
    def atualizar(self, perfil: Perfil):
        usuario = self.buscar(perfil.get_usuario())
        if usuario is None:
            raise UNCException(perfil.get_usuario())
        else:
            self.__usuarios.remove(usuario)
            self.__usuarios.append(perfil)
        

class MyTwitter():
    def __init__(self):
        self.__repositorios = RepositoriosUsuarios()
    
    def criar_perfil(self, perfil: Perfil):
        if self.__repositorios.buscar(perfil.get_usuario()) is not None:
            raise PPException(perfil.get_usuario())
        else:
            self.__repositorios.cadastrar(perfil)
    
    def cancelar_perfil(self, usuario):
        perfil = self.__repositorios.buscar(usuario)
        if perfil is not None:
            if perfil.is_ativo():
                perfil.set_ativo(False)
            else:
                raise PDException(usuario)
        else:
            raise PIException(usuario)
        
    def tweetar(self, usuario, texto):
        perfil = self.__repositorios.buscar(usuario)
        if perfil is not None:
            if perfil.is_ativo():
                if (len(texto) > 0) and (len(texto) < 141):
                    tweet = Tweet(usuario, texto)
                    perfil.add_tweet(tweet)
                else:
                    raise MFPException(len(texto))
            else:
                raise PDException(usuario)
        else:
            raise PIException(usuario)
    
    def timeline(self, usuario):
        perfil = self.__repositorios.buscar(usuario)
        if perfil is not None:
            if perfil.is_ativo():
                return perfil.get_timeline()
            else:
                raise PDException
        else:
            raise PIException
    
    def tweets(self, usuario):
        perfil = self.__repositorios.buscar(usuario)
        if perfil is not None:
            if perfil.is_ativo():
                return perfil.get_tweets()
            else:
                raise PDException(usuario)
        else:
            raise PIException(usuario)
    
    def seguir(self, seguidor, seguido):
        perfil_seguidor = self.__repositorios.buscar(seguidor)
        perfil_seguido = self.__repositorios.buscar(seguido)

        if seguidor != seguido:
            if perfil_seguidor is not None:
                if perfil_seguido is not None:
                    if perfil_seguido.is_ativo():
                        if perfil_seguidor.is_ativo():
                            perfil_seguido.add_seguidor(perfil_seguidor)
                            perfil_seguidor.add_seguidos(perfil_seguido)
                        else:
                            raise PDException(seguidor)
                    else:
                        raise PDException(seguido)
                else:
                    raise PIException(seguido)
            else:
                raise PIException(seguidor)
        else:
            raise SIException(seguidor)
    
    def numero_seguidores(self, usuario):
        perfil = self.__repositorios.buscar(usuario)
        if perfil is not None:
            if perfil.is_ativo():
                seguidores = 0
                for seguidor in perfil.seguidores():
                    if seguidor.is_ativo():
                        seguidores += 1
                return seguidores
            else:
                raise PDException(usuario)
        else:
            raise PIException(usuario)
    
    def seguidores(self, usuario):
        perfil = self.__repositorios.buscar(usuario)
        if perfil is not None:
            if perfil.is_ativo():
                seguidores = []
                for seguidor in perfil.seguidores():
                    if seguidor.is_ativo():
                        seguidores.append(seguidor)
                return seguidores
            else:
                raise PDException(usuario)
        else:
            raise PIException(usuario) 
    
    def seguidos(self, usuario):
        perfil = self.__repositorios.buscar(usuario)
        if perfil is not None:
            if perfil.is_ativo():
                seguidos = []
                for seguidor in perfil.seguidos():
                    if seguidor.is_ativo():
                        seguidos.append(seguidor)
                return seguidos
            else:
                raise PDException(usuario)
        else:
            raise PIException(usuario)
    
    