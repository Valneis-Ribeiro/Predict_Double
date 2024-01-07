import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
import requests
import time
import os


# MODELO KNN TAXA DE ACERTO 51.80 %

class PredictDouble:

    def __init__(self):
        self.previsores = pd.read_csv(self.choice_file(r'previsores.csv'), header=None)
        self.alvo = pd.read_csv(self.choice_file('alvo.csv'), header=None)
        self.url = 'https://blaze.com/api/roulette_games/recent'
        self.historico_model_dbl = []

    # Exporta os double correspondente, conforme a quantidade escolhida
    def export_roll_fish(self, amount_roll_fish):
        API = requests.get(self.url).json()
        all_rolls = [roll['roll'] for roll in API]
        if amount_roll_fish:
            rolls_choice = [
                0 if roll >= 8 and roll > 0 else 1 if roll <= 7 and roll > 0 else 2 for i, roll in
                enumerate(all_rolls[:amount_roll_fish])]
            return rolls_choice

    # Prever as qual sera o proximo double
    def predict_double_with_3_finish(self):
        # configuração do modelo
        knn = KNeighborsClassifier(n_neighbors=7, metric='minkowski', p=3)
        # Treinando o modelo
        knn.fit(self.previsores, self.alvo)
        # realizando a predicção
        prev_double = knn.predict([self.export_roll_fish(3)])
        # self.historico_predict.append()
        return prev_double

    # Tranforma os previsores exportados + predição_erra + result_alvo em CSV
    def export_data_predict_csv(self, historico_model):
        # Em desenvolvimento...
        status_erro = []
        for his_mod in historico_model:
            for his_mod2 in his_mod:
                if his_mod2 == 'Errou':
                    status_erro.append(his_mod)
        def_lista_erro = []
        for st_er in status_erro:
            def_lista_erro.append(st_er[0])
        for df_erro in def_lista_erro:
            df_erro.append(st_er[2])
        # gerar_plan_erro = pd.DataFrame(def_lista_erro, columns=['Cor1', 'C'])
        return def_lista_erro

    # Verificar a quantidade de erros e acertos do bet
    def check_bet_status(self, predicao):
        # mini historico double
        hist_three = self.export_roll_fish(3)
        # previsao do resultado
        predicao_double = predicao
        # levado para proxima rodada
        time.sleep(23)
        # Resultado
        double_3_result = self.export_roll_fish(3)[0]
        # status
        status = [hist_three, predicao_double[0], double_3_result,None]
        # Verificando se a predição está igual ao resultado dbl
        if predicao_double == double_3_result:
            status[3] = 'Ganhou'
        else:
            status[3] = 'Errou'
        # Adicionando em uma lista  o processo
        self.historico_model_dbl.append(status)
        return self.historico_model_dbl

    def choice_file(self, file):
        my_projects_folder = os.listdir(os.getcwd())
        for folder in my_projects_folder:
            if folder == 'predict_double':
                path_folder_file = os.path.join(os.getcwd(), folder )
                list_files = os.listdir(path_folder_file)
                if file in list_files:
                    return os.path.join(path_folder_file, list_files[list_files.index(file)])












