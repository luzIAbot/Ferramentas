import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from fuzzywuzzy import process

def classificador_ia(lista_strings, df):

    keys = df.iloc[:, 0].astype(str).tolist() # Get the values from the first column as keys
    values = df.iloc[:, 1:].astype(str).values.tolist()  # Get the values from the remaining columns as values

    treinamento = []
    rotulos = []

    for i, key in enumerate(keys):
        for value in values[i]:
            treinamento.append(value.lower())
            rotulos.append(key)

    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(treinamento)

    classifier = MultinomialNB()
    classifier.fit(X, rotulos)

    lista_strings = [str(item) for item in lista_strings]  # Convert lista_strings elements to string
    X_test = vectorizer.transform(lista_strings)
    classificacoes = classifier.predict(X_test)

    return classificacoes

def setorizacao_ia(lista_strings):
    """
    Com as classes CountVectorizer e MultinomialNB da biblioteca scikit-learn, necessárias para vetorizar os dados de texto e treinar o classificador Naive Bayes.
    Essa função recebe uma lista de strings a serem classificadas. 
    A variável grupos é um dicionário que contém os grupos pré-definidos e suas palavras-chave correspondentes.
    Com as palavras-chave treinamos o classificador Naive Bayes.
    Após o treinamento ocorre a setorização.

    Exemplo:

    # Importando bibliotecas próprias do G&I
    user_path = os.path.expanduser("~")
    os.chdir(user_path)
    user_path = os.getcwd()
    caminho = user_path+"\\luminae.com.br\\GI - General\\5 Desenvolvimento de Diretorio\\0_Gestao_da_Area"
    
    sys.path.append(caminho)
    import bibGI.classificadores as cl

    df = pd.read_csv('arquivo.csv')
    coluna_strings = df['Nome_da_Coluna'].tolist()

    resultado = cl.setorizacao_ia(coluna_strings) # o retorno é um array

    df['Nome_da_nova_coluna'] = resultado

    print(df.head(20))
    """

    grupos = {
        "Iluminação SDV": ["Iluminação", "SLV", "SDV", "SDV", "SDV", "1/3", "2/3", "Iluminacao","Salão de Vendas","Fundo da Loja","ILUMINAÇÃO 2/3", "ILUMINAÇÃO 1/3","IL","ILUMI","SV","ilumi 2/3","ilumi 1/3","PV2","Mezanino","SLV1","SLV2","SLV3","Iluminacao 1/3","Iluminacao 2/3","ILUMINAÇÃO 2/3","ILUMINAÇÃO 2/3","ILUMINAÇÃO 2/3","ILUMINAÇÃO 1/3","ILUMINAÇÃO 1/3","Iluminação 2/3","Iluminação 2/3","Iluminação 1/3","Iluminação 1/3","ILUMINAÇÃO","ILUMINAÇÃO"],
        "Climatização": ["Ar condicionado", "RTU", "AC", "Chiller", "Bomba", "Fancoil", "Maquina","A/C","A/C Maq","A/C Máq","SPLITAO", "Split","Ar-condicionado","Ar","AR CONDICIONADO FUNDO DE LOJA","ELETRO","RT","AC SLV","FAN-C0IL","FAN-C0IL","FAN-COIL","FAN C0IL","FAN COIL", "RTU3 e RTU4", "RTU3 e RTU4"],
        "Iluminação Estacionamento": ["Iluminação Vas ESCIONA","Estacionamento", "EC","Iluminação Estacionamento","ILUMINACAO VAGAS ESTCIO(C2)","ILUMINACAO EC","ILUMINACAO ESTACIONAMENENTO","ILUMINAÇÃO ESTAC. COBERTO","Iluminação Estacionamento Coberto","ILUMINACAO EC1","ILUMINACAO EC2","ILUMI ESTACIONAMENTO","IL. ESTACIONAMENTO  SUPERIOR","IL. ESTACIONAMENTO INFERIOR","ILM Estac","Iluminação Estaciamento","Iluminação Estaciamento Vigia","Iluminação Estacinamento","Iluminação Estacinamento","Iluminação Estacinamento","Iluminação Estacinamento","[24] Iluminação Estacinamento","[24] Iluminação Estacinamento"],
        "Iluminação Externa": ["Externa", "Ext","Iluminação Externa","ILUMINAÇÃO EXTERNA / TOTEM","Iluminacao Totem","ILUMI. LETREIRO E FACHADA","ILUMI EXTERNA","Iluminacao Totem", "Postes","Fachada","Totem","Tot","Iluminação Externo","Iluminação Externo","ILUMINAÇÃO EXTERNA","ILUMINAÇÃO EXTERNA","ILUMINAÇÃO EXTERNA","ILUMINAÇÃO EXTERNO","ILUMINAÇÃO EXTERNO","ILUMINAÇÃO EXTERNO"],
        "Iluminação Docas":["Iluminacao Docas", "Docas","ILUMINAÇÃO DOCAS ESTOQUE","ILUMINAÇÃO DOCAS","Recebimento","RECEBIMENTO","Iluminação Recebimento","ILUM RECEBIMENTO","Ilum recebimento","Iluminação Docas","Iluminação Docas","Iluminação Docas"],
        "Iluminação Depósito":["ILUMINACAO DEPOSITO","ILUMINAÇÃO DEPÓSITO","Deposito","ILUM. DEPOSITO","deposito","ILUMI DEPOSITO","ILUMINAÇÃO DEPÓSITO","Deposito","ILUM. DEPOSITO","deposito","ILUMI DEPOSITO","ILUMINAÇÃO DEPÓSITO 02","ILUMINAÇÃO DEPÓSITO 02","ILUMINAÇÃO DEPÓSITO"],
        "Banco de Capacitores":["Banco de Capacitor","BC","BC","BC","BC","Banco", "Capacitor"," BC"],
        "Outros":['Reserva',"Saída Digital","Saida Digital","Saida","MARQUIS LOJA","Marquis Loja"]
    }
 
    treinamento = []
    rotulos = []

    for grupo, palavras_chave in grupos.items():
        for palavra_chave in palavras_chave:
            treinamento.append(palavra_chave.lower())
            rotulos.append(grupo)

    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(treinamento)

    classifier = MultinomialNB()
    classifier.fit(X, rotulos)

    X_test = vectorizer.transform(lista_strings)
    classificacoes = classifier.predict(X_test)

    return classificacoes

def setorizacao(nome_de_col_das_medicoes,relatorio):
    """
    Essa função é utilizada para setorizar as medições de energia nas categorias definidas pela Luminae.
    
    Para usar essa função é necessário inserir o nome da coluna do dataframe que contêm o nome das medições e
    inserir o dataframe analisado. A saída será um dataframe com uma nova coluna definindo os setores.
    
    Exemplo:
    import sys
    sys.path.append("C:/Users/leonardo.gomes/luminae.com.br/GI - General/5 Desenvolvimento de Diretorio/0_Gestao_da_Area")
    import bibGI.mod as gi
    
    cons_diario = gi.setorizacao(coluna_medicoes, cons_diario)
    """
    df1 = relatorio[nome_de_col_das_medicoes] # filtrando as medições e armazenando na variável df1, dessa forma não corrompemos o df

    classificador = [] # lista auxiliar para asetorização, nela será armazenado a categorização de cada medição

    sc = df1.str.lower() # o conteúdo do DataFrame df1 terá as string convertidas em caixa baixa

    for i in sc:
        if (('slv' in i) | ('ilumina' in i)) & ('total' not in i) & ('dep' not in i) & ('ext' not in i) & ('esta' not in i):
            classificador.append('Iluminação SDV')

        elif (('slv' in i) | ('ilumina' in i)) & ('total' in i) & ('dep' not in i) & ('ext' not in i) & ('esta' not in i):
            classificador.append('Iluminação SDV Total')

        elif (('ext' in i) | ('externa' in i)) & ('total' not in i):
            classificador.append('Iluminação Externa')

        elif (('est' in i) | ('estacionamento' in i)) & ('total' not in i) & ('slv' not in i):
            classificador.append('Iluminação Estacionamento')

        elif (('dep' in i) | ('depósito' in i) | ('deposito' in i)) & ('total' not in i) & ('slv' not in i):
            classificador.append('Iluminação Depósito')

        elif (('doc' in i) | ('docas' in i) | ('recebimento' in i)) & ('total' not in i) & ('slv' not in i):
            classificador.append('Iluminação Docas')

        elif (('condicionado' in i) | ('bomba' in i) | ('chiller' in i) | ('fancoi' in i) | ('split' in i) | ('roof' in i)) & ('total' not in i):
            classificador.append('Climatização')

        elif (('alimentar' in i) | ('frio' in i) | ('refrige' in i) | ('conge' in i) | ('ilhas' in i) | ('resfriad' in i) | ('congela' in i) | ('câmara' in i) | ('camara' in i)) & ('total' not in i):
            classificador.append('Frio Alimentar')

        elif ('qgbt' in i) | ('trafo' in i) | ('geral' in i) | ('rede' in i):
            classificador.append('QGBT')

        elif (('qgbt' in i) | ('trafo' in i) | ('geral' in i) | ('rede' in i)) & ('total' in i):
            classificador.append('QGBT Total')

        elif (('concessionária' in i) | ('concessionaria' in i)) & ('total' not in i):
            classificador.append('Concessionária')

        elif (('gerador' in i) | ('qta' in i) | ('Gerador' in i)) & ('total' in i):
            classificador.append('Gerador')

        elif ('ga_' in i) | ('_ag_' in i) | ('_O' in i) & ('total' not in i) & ('gerador' not in i)  & ('demais cargas' not in i):
            classificador.append('Galerias')
        else:
            classificador.append('Outros')
        
    relatorio.insert(2,'Setorizacao',classificador) # inserindo em df uma coluna com a classifiucação de cada medição
    new_relatorio = relatorio
    return new_relatorio

def cod_luminae(nome_de_col_das_medicoes, id_loja, relatorio_setor):
    """
    Essa função tem como finalidade atribuir o Código Identificador da Luminae para cada loja identificando através
    dos nomes das medições.

    Essa função busca no banco de dados que contêm um dê-para das medições e códigos. Em seguida, compara os valores
    da coluna que contem as medições e atribui o valor do código equivalente a essa medição.

    Como saída temos um dataframe com um coluna definindo os códigos Luminae para cada medição.

    Para usar essa função é necessário inserir o nome da coluna do dataframe que contêm o nome das medições, o dataframe
    referente que contêm os id's das lojas e inserir o dataframe analisado.

    Exemplo:
    import sys
    sys.path.append("C:/Users/leonardo.gomes/luminae.com.br/GI - General/5 Desenvolvimento de Diretorio/0_Gestao_da_Area")
    import bibGI.mod as gi
    
    cons_diario = gi.cod_luminae(nome_de_col_das_medicoes, id_loja, relatorio_setor)
    """
    id = []
    medicoes_do_consolidado = []
    medicoes_do_id_loja = []
    id_banco =[]

    for i in relatorio_setor[nome_de_col_das_medicoes]: medicoes_do_consolidado.append(i)

    for i in id_loja[nome_de_col_das_medicoes]: medicoes_do_id_loja.append(i)

    for i in id_loja['ID_Filial']: id_banco.append(i)

    for i in medicoes_do_consolidado:
        if i in medicoes_do_id_loja:

                indice = medicoes_do_id_loja.index(i)
                id.append(id_banco[indice])
        else:
                id.append(0)

    relatorio_setor.insert(0,'Codigo Luminae',id)

    relatorio_com_cod = relatorio_setor

    return relatorio_com_cod

def setorizacao_temp(nome_de_col_das_medicoes,relatorio):
    df1 = relatorio[nome_de_col_das_medicoes] # filtrando as medições e armazenando na variável df1, dessa forma não corrompemos o df

    classificador = [] # lista auxiliar para asetorização, nela será armazenado a categorização de cada medição

    sc = df1.str.lower() # o conteúdo do DataFrame df1 terá as string convertidas em caixa baixa

    for i in sc:
        if ('sdv' in str(i)) or ('salão de vendas' in str(i)) or ('salao de vendas' in str(i)):
            classificador.append('Salão de Vendas')
        elif ('frente' in str(i)) or ('caixa' in str(i)):
            classificador.append('Frente de Caixa')
        elif (('hortifruti' not in str(i)) or ('horti' in str(i)) or ('fruti' in str(i))) and ('açougue' not in str(i)) and ('meio de loja' not in str(i)):
            classificador.append('Hortifruti')
        elif ('açougue' in str(i)) or ('açou' in str(i)) or ('gue' in str(i)):
            classificador.append('Açougue')
        elif (('meio de loja' in i) or ('meio' in i)):
            classificador.append('Meio de Loja')
        elif ('congelados' in i):
            classificador.append('Congelados')
        else:
            classificador.append('Não Identificado')
        
    relatorio.insert(2,'Setorizacao Temp',classificador) # inserindo em df uma coluna com a classifiucação de cada medição
    new_relatorio = relatorio
    return new_relatorio

def encontrando_valor_similar_fuzzy(df, coluna_alvo):
    # Verifica se a coluna alvo já existe no DataFrame
    if coluna_alvo in df.columns:
        # Se existir, retorna o nome da coluna alvo
        return coluna_alvo
    else:
        # Se não existir, encontra colunas similares usando Fuzzy String Matching
        colunas_similares, score = process.extractOne(coluna_alvo, df.columns)
        coluna_similar_nome = colunas_similares

        # Define um limiar de similaridade como número inteiro
        limiar_similaridade = 90

        # Verifica se a similaridade é um número antes de comparar
        if isinstance(score, int) and score >= limiar_similaridade:
            return coluna_similar_nome
        else:
            # Caso contrário, imprime uma mensagem e retorna None
            print("Nenhuma coluna similar encontrada.")
            return None
        
def encontrando_valor_similar_rede_neural(df, coluna_alvo):
    if coluna_alvo in df.columns:
        return coluna_alvo
    else:

        # Cria um DataFrame de treinamento com rótulos indicando se a coluna é a alvo
        df_treinamento = pd.DataFrame({'Coluna': df.columns, 'Alvo': (df.columns == coluna_alvo).astype(int)})
        
        # Se não houver colunas com o nome da coluna alvo, imprime uma mensagem e retorna None
        if df_treinamento['Alvo'].sum() == 0:
            print("Nenhuma coluna com o nome da coluna alvo encontrada.")
            return None

        # Codifica os nomes das colunas como números
        label_encoder = LabelEncoder()
        df_treinamento['Coluna'] = label_encoder.fit_transform(df_treinamento['Coluna'])

        # Divide os dados em treinamento e teste
        X_train, X_test, y_train, y_test = train_test_split(df_treinamento[['Coluna']], df_treinamento['Alvo'], test_size=0.2, random_state=42)

        # Cria e treina o modelo de rede neural
        modelo = MLPClassifier(hidden_layer_sizes=(100,), max_iter=500, random_state=42)
        modelo.fit(X_train, y_train)

        # Faz previsões no conjunto de teste
        previsoes = modelo.predict(X_test)
        precisao = accuracy_score(y_test, previsoes)

        # Adiciona previsões ao DataFrame de treinamento
        df_treinamento['Predicao'] = modelo.predict(df_treinamento[['Coluna']])

        # Verifica se há alguma previsão igual a 1 antes de tentar acessar o índice 0
        if 1 in df_treinamento['Predicao'].values:
            coluna_similar_nome = label_encoder.inverse_transform(df_treinamento[df_treinamento['Predicao'] == 1]['Coluna'])[0]

            # Se a coluna similar existe no DataFrame original, retorna o nome
            if coluna_similar_nome in df.columns:
                return coluna_similar_nome
            else:
                # Caso contrário, imprime uma mensagem e retorna None
                print("Nenhuma coluna similar encontrada.")
                return None
        else:
            print("Nenhuma previsão igual a 1 encontrada.")
            return None