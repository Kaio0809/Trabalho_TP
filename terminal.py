from Twitter import Tweet, Perfil, PessoaFisica, PessoaJuridica, RepositoriosUsuarios, MyTwitter
from excecoes import PPException, PDException, PIException, MFPException, UJCException, UNCException, SIException

def terminal():
    mytwitter = MyTwitter()
    while True:
        print("[0] - Criar Perfil\n[1] - Cancelar Perfil\n[2] - Tweetar\n[3] - Mostrar Timeline\n[4] - Mostrar Tweets\n[5] - Seguir\n[6] - Numero de seguidores\n[7] - Seguidores \n[8] - Seguidos\n[9] - Sair")
        opcao = int(input("\nDigite uma opção: "))

        if opcao == 0:
            try:
                usuario = "@" + str(input("Digite o Usuário: @"))
                tipo = str(input("PF - Pessoa Fisica | PJ - Pessoa Juridica\nDigite o Tipo de Perfil: "))
                if tipo == "PF":
                    cpf = str(input("Digite o seu CPF: "))
                    perfil = PessoaFisica(usuario, cpf)
                elif tipo == "PJ":
                    cnpj = str(input("Digite o seu CNPJ: "))
                    perfil = PessoaJuridica(usuario, cnpj)
                else:
                    print("Tipo Inválido!")
                    continue
                mytwitter.criar_perfil(perfil)
                print("Perfil Criado!\n")
            except PPException as ex:
                ex.print_mensagem()
            except UJCException as ex:
                ex.print_mensagem()

        elif opcao == 1:
            try:
                usuario = "@" + str(input("Digite o usuário: @"))
                mytwitter.cancelar_perfil(usuario)
                print("Perfil Cancelado!\n")
            except PDException as excecao:
                excecao.print_mensagem()
            except PIException as excecao:
                excecao.print_mensagem()
        
        elif opcao == 2:
            try:
                usuario = "@" + str(input("Digite o usuário: @"))
                mensagem = str(input("Digite seu texto (max - 140 caracteres): "))
                mytwitter.tweetar(usuario, mensagem)
                print("Tweetado!\n")
            except MFPException as ex:
                ex.print_mensagem()
            except PDException as ex:
                ex.print_mensagem()
            except PIException as ex:
                ex.print_mensagem()
        
        elif opcao == 3:
            try:
                usuario = "@" + str(input("Digite o usuário: @"))
                linha_do_tempo = mytwitter.timeline(usuario)
                print("Timeline:\n")
                for tweet in linha_do_tempo:
                    print(f"usuário: {tweet.get_usuario()}\nTweet: {tweet.get_mensagem()}\nData: {tweet.get_data_postagem()}\n\n")
            except PDException as ex:
                ex.print_mensagem()
            except PIException as ex:
                ex.print_mensagem()
        
        elif opcao == 4:
            try:
                usuario = "@" + str(input("Digite o usuário: @"))
                tweets = mytwitter.tweets(usuario)
                print(f"Tweets {usuario}:")
                for tweet in tweets:
                    print(f"Tweet: {tweet.get_mensagem()}\nData: {tweet.get_data_postagem()}\n")
            except PDException as ex:
                ex.print_mensagem()
            except PIException as ex:
                ex.print_mensagem()
        
        elif opcao == 5:
            try:
                usuario = "@" + str(input("Digite o usuário: @"))
                seguir = "@" + str(input("Perfil seguido: @"))
                mytwitter.seguir(usuario, seguir)
                print("Seguido!\n")
            except PDException as ex:
                ex.print_mensagem()
            except PIException as ex:
                ex.print_mensagem()
            except SIException as ex:
                ex.print_mensagem()
        
        elif opcao == 6:
            try:
                usuario = "@" + str(input("Digite o usuário: @"))
                print(f"Você tem {mytwitter.numero_seguidores(usuario)} seguidores!\n")
            except PDException as ex:
                ex.print_mensagem()
            except PIException as ex:
                ex.print_mensagem()
        
        elif opcao == 7:
            try:
                usuario = "@" + str(input("Digite seu usuario: @"))
                seguidores = mytwitter.seguidores(usuario)
                print("Seus Seguidores:")
                for seguidor in seguidores:
                    print(f"{seguidor.get_usuario()}")
            except PDException as ex:
                ex.print_mensagem()
            except PIException as ex:
                ex.print_mensagem()
        
        elif opcao == 8:
            try:
                usuario = "@" + str(input("Digite seu usuario: @"))
                seguidos = mytwitter.seguidos(usuario)
                print("Seus Seguidos:")
                for seguidor in seguidos:
                    print(f"{seguidor.get_usuario()}")
            except PDException as ex:
                ex.print_mensagem()
            except PIException as ex:
                ex.print_mensagem()

        elif opcao == 9:
            print("Rede Social Encerrada!")
            break
        else:
            print("Digito Inválido!")
            continue

terminal()