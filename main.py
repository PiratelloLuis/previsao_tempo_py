##Provavelmente este código não ira funcionar pois não paguei a API premium, então deixarei uma foto de como ele funcionou
import requests
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as messagebox
from files import api_key


def centrajanela(window):  # Centralizar o aplicativo
    window.update_idletasks()
    width = window.winfo_width()  # Largura da janela
    height = window.winfo_height()  # Altura da janela
    x = (window.winfo_screenwidth() // 2) - (width // 2)  # Calcula o X para centralizar
    y = (window.winfo_screenheight() // 2) - (height // 2)  # Calcula o Y para centralizar
    window.geometry(f"{width}x{height}+{x}+{y}")


def obter_previsao_tempo():
    cidade = cidade_entry.get()
    api_k = api_key  # COLOQUE SUA API AQUI
    url = f'http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_key}'

    response = requests.get(url)
    dados = response.json()

    if response.status_code == 200:
        temperatura_kelvin = dados['main']['temp'] #Temperatura
        temperatura_celsius = temperatura_kelvin - 273.15 #Transforma Kelvin em celsius
        umidade = dados['main']['humidity'] #umidade
        velocidade_vento_ms = dados['wind']['speed'] #velocidade do vento
        velocidade_vento_kmh = velocidade_vento_ms * 3.6

        resultado_label.config(text=f'Temperatura: {temperatura_celsius:.2f} °C\n'
                                    f'Velocidade do Vento: {velocidade_vento_kmh:.2f} km/h\n'
                                    f'Umidade: {umidade}%')
    else:
        messagebox.showerror('Erro', 'Não foi possível obter os dados.')


# criando a janela principal
janela = tk.Tk()  # criar a janela usando a biblioteca tk
janela.title('Pervesão do Tempo')  # colocar titulo na janela

# centralizando a janela
centrajanela(janela)  # chama a função centralizar

# criando os elementos da interface
cidade_label = ttk.Label(janela, text='Cidade:') #exibe o texto "cidade"
cidade_entry = ttk.Entry(janela) #campo onde o usuario escolhe a cidade
cidade_entry.focus()
mostrar_button = ttk.Button(janela, text='Mostrar', command=obter_previsao_tempo) #Botão para mostrar resultados
resultado_label = ttk.Label(janela, text='') #rotulo vazio que sera usado para mostrar dados

# todas essas linhas são para organizar usando o metoddo pack
cidade_label.pack()
cidade_entry.pack()
mostrar_button.pack()
resultado_label.pack()

# iniciando o loop da interface
janela.mainloop()
