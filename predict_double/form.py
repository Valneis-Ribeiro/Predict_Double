import PySimpleGUI as sg
from previsor_double import PredictDouble


sg.theme('DarkGray11')

double = [[sg.Button('Gerar Previsão Double',font=("arial", 15),size=(100,2))],
          [sg.Image(key='-DOUBLE-',size=(40,30))]]

window_dbl = sg.Window('previsão double', double,size=(240,300))

while True:

    event, value = window_dbl.read()

    if event == sg.WIN_CLOSED:
        break

    if event == 'Gerar Previsão Double':

        # Treinamento do modelo
        prev_bl = PredictDouble()

        # predicação
        predicao = prev_bl.predict_double_with_3_finish()

        if predicao == 0.0:
            sg.popup_quick_message('Carregando predição...')
            window_dbl['-DOUBLE-'].update(filename=prev_bl.choice_file('black.png'))
        if predicao == 1.0:
            sg.popup_quick_message('Carregando predição...')
            window_dbl['-DOUBLE-'].update(filename=prev_bl.choice_file('red.png'))


        # # historico de verificação de status bet
        # status = prev_bl.check_bet_status(predicao)

        # print(status)

window_dbl.close()




            
            