import hashlib
import os

def cifra_cesar(texto, chave=5):
    """Cifra uma string deslocando os caracteres na tabela ASCII."""
    texto_cifrado = ""
    for caractere in str(texto):
        texto_cifrado += chr(ord(caractere) + chave)
    return texto_cifrado

def decifra_cesar(texto_cifrado, chave=5):
    """Decifra uma string subtraindo o deslocamento na tabela ASCII."""
    texto_decifrado = ""
    for caractere in str(texto_cifrado):
        texto_decifrado += chr(ord(caractere) - chave)
    return texto_decifrado

def troca(L, i, j):
    """Função auxiliar para trocar dois elementos de posição na lista."""
    L[i], L[j] = L[j], L[i]

def empurra_maximo(L, n):
    """Desloca o item máximo da lista L para o final (Ordem Crescente)."""
    i = 0
    while i < n-1:
        if L[i][1][0].lower() > L[i+1][1][0].lower():
            troca(L, i, i+1)
        i += 1

def empurra_minimo(L, n):
    """Desloca o item mínimo da lista L para o final (Ordem Decrescente)."""
    i = 0
    while i < n-1:
        if L[i][1][0].lower() < L[i+1][1][0].lower():
            troca(L, i, i+1)
        i += 1

def bubble_sort(L, crescente=True):
    """Ordena a lista baseada no Bubble Sort."""
    if crescente:
        empurra = empurra_maximo
    else:
        empurra = empurra_minimo

    n = len(L)
    while n > 1:
        empurra(L, n)
        n -= 1

def mescla(L, i, m, f):
    T = []
    k = i
    j = m + 1

    while k <= m and j <= f:
        if L[k][1][0].lower() <= L[j][1][0].lower():
            T.append(L[k])
            k += 1
        else:
            T.append(L[j])
            j += 1

    while k <= m:
        T.append(L[k])
        k += 1

    while j <= f:
        T.append(L[j])
        j += 1

    for a in range(len(T)):
        L[i] = T[a]
        i += 1

def merge_sort(L, i, f):
    if i >= f:
        return
    m = (i + f) // 2
    merge_sort(L, i, m)
    merge_sort(L, m + 1, f)
    mescla(L, i, m, f)

def cadastro():
    print("\n" + "="*40)
    print(f"{'🆕 CADASTRAR NOVO USUÁRIO':^40}")
    print("="*40)

    while True:
        usuario = input("Digite o nome do novo usuário: ").strip()
        senha = input("Digite a senha de acesso: ").strip()

        if usuario == "" or senha == "":
            print("\n[!] Erro: Usuário ou senha não podem ser vazios. Tente novamente.")
            print("-" * 40)
        else:
            break

    usuario_hash = hashlib.sha256(usuario.encode()).hexdigest()
    senha_hash = hashlib.sha256(senha.encode()).hexdigest()

    with open("login.txt", "w", encoding="utf-8") as cadastrar:
        cadastrar.write(f"{usuario_hash}\n{senha_hash}")

    print("\n[✓] Usuário cadastrado e salvo com sucesso!")
    print("="*40)

def verifica_login():
    print("\n" + "="*40)
    print(f"{'🔐 ACESSAR SISTEMA (LOGIN)':^40}")
    print("="*40)

    if not os.path.exists("login.txt") or os.path.getsize("login.txt") == 0:
        print("\n[!] Nenhum usuário cadastrado no sistema ainda.")
        print("[!] Por favor, crie uma conta primeiro.")
        print("="*40)
        return False

    try:
        with open('login.txt', 'r', encoding="utf-8") as confirmacao:
            ver = confirmacao.readlines()
            usuario_login = ver[0].strip()
            senha_login = ver[1].strip()
    except (FileNotFoundError, IndexError):
        print("[!] Erro crítico: Arquivo de autenticação inválido.")
        return False

    u = input('Usuário: ').strip()
    s = input('Senha: ').strip()
    
    u_hash = hashlib.sha256(u.encode()).hexdigest()
    s_hash = hashlib.sha256(s.encode()).hexdigest()

    if u_hash == usuario_login and s_hash == senha_login:
        print('\n[✓] Conexão estabelecida com sucesso! Bem-vindo.')
        print("="*40)
        return True
    else:
        print('\n[❌] Login ou senha incorretos!')
        print("="*40)
        return False

def atualiza(d):
    print('\n' + '='*40)
    print(f"{'✏️  MENU DE ATUALIZAÇÃO':^40}")
    print('='*40)
            
    if not d:
        print("[!] A Pokédex está vazia. Nada para atualizar.")
        print('='*40)
    else:
        id_atualizar = int(input("Digite o ID do Pokémon que deseja editar: "))
                
        if id_atualizar in d:
                
            nome = d[id_atualizar]
                    
            print(f"\n📢 Pokémon Selecionado: {nome}")
            print("─" * 40)
            print(" [1] 🏷️  Nome")
            print(" [2] 🧬 Tipo")
            print(" [3] ✨ Status Shine")
            print(" [4] 🍃 Natureza")
            print(" [5] 💰 Preço")
            print(" [6] 📦 Quantidade")
            print("─" * 40)
                    
            escolha = int(input("O que você deseja alterar? "))
            print("─" * 40)
            
            if escolha == 1:
                novo_nome = input("Qual o novo nome? ")
                d[id_atualizar][0] = novo_nome

            elif escolha == 2:
                novo_tipo = input("Qual o novo tipo? ")
                d[id_atualizar][1] = novo_tipo

            elif escolha == 3:
                resp_shine = input("Novo status Shine (sim/nao): ").lower()
                if resp_shine == "sim": resp_shine == True
                else: resp_shine == False
                d[id_atualizar][2] = resp_shine

            elif escolha == 4:
                novo_natureza = input("Qual a nova natureza? ")
                d[id_atualizar][3] = novo_natureza

            elif escolha == 5:
                novo_preco = float(input("Qual o novo preço? R$ "))
                d[id_atualizar][4] = novo_preco

            elif escolha == 6:
                novo_qtd = int(input("Qual a nova quantidade? "))
                d[id_atualizar][5] = novo_qtd
            
            else:
                print("\n[!] Opção inválida. Nenhuma alteração foi feita.")
                print('='*40)
                
            if escolha > 0 and escolha < 7:
                print(f"\n[✓] Sucesso: Dado modificado na memória RAM!")
                print('='*40)

def busca_linear(d, nome_busca):
    """Busca direta no dicionário por correspondência de nome."""
    encontrados = []
    for id_p, dados in d.items():
        if nome_busca.lower() in dados[0].lower():
            encontrados.append((id_p, dados))
    return encontrados        

def remover(d):
    if not d:
        print("\n[!] A Pokédex está vazia. Nada para remover.")
    else:
        id_remover = int(input("Digite o ID do Pokémon que deseja remover: "))
        if id_remover in d:
            nome_pokemon = d[id_remover][0]
            del d[id_remover]
            print(f"\n Pokémon: {nome_pokemon} ID: {id_remover} removido com sucesso!")
    

def salva_inventario(d):
    arquivo = open("inventario.csv", "w", encoding="utf-8")
    for id_pokemon, dados in d.items():
        nome, tipo, shine, natureza, preco, qtd = dados
        
        id_cifrado = cifra_cesar(str(id_pokemon))
        nome_cifrado = cifra_cesar(str(nome))
        tipo_cifrado = cifra_cesar(str(tipo))
        shine_cifrado = cifra_cesar(str(shine))
        natureza_cifrado = cifra_cesar(str(natureza))
        preco_cifrado = cifra_cesar(str(preco))
        qtd_cifrado = cifra_cesar(str(qtd))
        
        linha = f"{id_cifrado};{nome_cifrado};{tipo_cifrado};{shine_cifrado};{natureza_cifrado};{preco_cifrado};{qtd_cifrado}\n"
        arquivo.write(linha)
    
    arquivo.close()
    print("\n[✓] Inventário criptografado e salvo com sucesso!")

def carrega_inventario():
    pokedex = {}

    try:
        arquivo = open("inventario.csv", "r", encoding="utf-8")

        for linha in arquivo:
            linha = linha.strip()

            if linha:
                dados_cifrados = linha.split(";")

                try:
                    id_pokemon = int(decifra_cesar(dados_cifrados[0]))
                    nome = decifra_cesar(dados_cifrados[1])
                    tipo = decifra_cesar(dados_cifrados[2])
                    
                    status_shine = decifra_cesar(dados_cifrados[3])
                    shine = True if status_shine == "True" else False

                    natureza = decifra_cesar(dados_cifrados[4])
                    preco = float(decifra_cesar(dados_cifrados[5]))
                    qtd = int(decifra_cesar(dados_cifrados[6]))

                    pokedex[id_pokemon] = [nome, tipo, shine, natureza, preco, qtd]
                
                except (ValueError, IndexError):
                    continue

        arquivo.close()

    except FileNotFoundError:
        print("\n[!] Arquivo 'inventario.csv' não encontrado.")
        opcao = input("Deseja criar um novo inventário vazio? (sim/nao): ").lower()
        if opcao != "sim":
            print("Encerrando o programa para ajuste do arquivo...")
            exit()

    return pokedex

def add_pokemon(d):
    while True:
        
        print('\n' + '='*40)
        print(f"{'SISTEMA DE GESTÃO - POKÉDEX':^40}")
        print('='*40)
        print(' [1] ➕ Cadastrar Novo Pokémon')
        print(' [2] 📋 Exibir Inventário Completo')
        print(' [3] 🔍 Buscar Pokémon (Nome/ID)')
        print(' [4] ✏️  Atualizar Dados de um Pokémon')
        print(' [5] ❌ Remover Pokémon do Estoque')
        print(' [6] 🔐 Alterar Usuário/Senha do Sistema')
        print(' [7] 💾 Salvar Lote e Sair')
        print('='*40)

        try:
            selecao = int(input('\nPara onde quer ir? '))
        except ValueError:
            print("\n[!] Opção Inválida! Entre apenas com o número da opção.")
            continue

        if selecao == 1:
            id_digitado = int(input('Digite o id do pokemon '))
            if id_digitado in d:
                print('Erro ja existe o pokemon cadastrado')
            else:
                nome = input('Qual o pokemon: ')
                
                tipo = input('Qual o tipo: ')
                shine = bool(input('Shine (sim/nao): '))
                natureza = input('Qual a natureza: ')
                preco = float(input(f'Qual o valor do {nome}: '))
                qtd = int(input(f'Quantos {nome} têm: '))
                d[id_digitado] = [nome,tipo,shine,natureza,preco,qtd]
    
        elif selecao == 2:
            if not d:
                print("\n[!] A Pokédex está vazia no momento.")
            else:
                # Transforma o dicionário em lista de tuplas para ordenar por nome: [(id, [dados]), ...]
                lista_ordenada = list(d.items())
                
                # Escolha automática do algoritmo conforme a quantidade de itens
                if len(lista_ordenada) <= 100:
                    bubble_sort(lista_ordenada, crescente=True)
                else:
                    merge_sort(lista_ordenada, 0, len(lista_ordenada) - 1)

                print("\n" + "="*95)
                print(f"{'SISTEMA DE GESTÃO DE INVENTÁRIO - POKÉDEX':^95}")
                print("="*95)
                print(f"{'ID':<6} | {'Nome':<15} | {'Tipo':<12} | {'Shine':<6} | {'Natureza':<12} | {'Preço':<12} | {'Quantidade':<10}")
                print("-" * 95)

                for id_p, mostrar in lista_ordenada:
                    nome, tipo, shine, natureza, preco, qtd = mostrar
                    status_shine = "Sim" if shine else "Não"
                    print(f"{id_p:<6} | {nome:<15} | {tipo:<12} | {status_shine:<6} | {natureza:<12} | R$ {preco:<9.2f} | {qtd:<10}")
                print("="*95)
        elif selecao == 3:
            nome_busca = input("Digite o nome do Pokémon: ")   
        
        elif selecao == 4:
            atualiza(d)

        elif selecao == 5:
            remover(d)

        elif selecao == 6:
            print('\n' + '='*40)
            print(f"{'🔐 ALTERAR USUÁRIO E SENHA':^40}")
            print('='*40)
            
            novo_usuario = input("Digite o novo nome de usuário: ")
            nova_senha = input("Digite a nova senha: ")
            
            if novo_usuario.strip() == "" or nova_senha.strip() == "":
                print("\n[!] Erro: Usuário ou senha não podem ser vazios.")
                print('='*40)
            else:
                novo_usuario_hash = hashlib.sha256(novo_usuario.encode()).hexdigest()
                nova_senha_hash = hashlib.sha256(nova_senha.encode()).hexdigest()
                
                with open("login.txt", "w") as atualizar_login:
                    atualizar_login.write(f"{novo_usuario_hash}\n{nova_senha_hash}")
                
                print("\n[✓] Usuário e senha alterados com sucesso!")
                print('='*40)

        elif selecao == 7:
            salva_inventario(d)
            print('\n[✓] Alterações gravadas com sucesso!')
            return



def main():
    logado = False

    while not logado:
        print("\n" + "="*40)
        print(f"{' BEM-VINDO AO SISTEMA POKÉDEX':^40}")
        print("="*40)
        print(" [1] Criar Novo Login")
        print(" [2] Entrar com Login Existente")
        print(" [3] Sair do Programa")
        print("="*40)
        
        try:
            opcao_inicial = int(input("Escolha uma opção: "))
        except ValueError:
            print("\n[!] Opção inválida! Digite apenas números.")
            continue
            
        if opcao_inicial == 1:
            cadastro()
        elif opcao_inicial == 2:
            logado = verifica_login()
        elif opcao_inicial == 3:
            print("\nEncerrando o programa de segurança...")
            return
        else:
            print("\n[!] Opção inválida! Tente novamente.")

    pokedex = carrega_inventario()
    add_pokemon(pokedex)
    print("\n[✓] Programa encerrado com segurança. Até logo!")

main()