from navegador import NavegadorWebSimulado
from interface import exibir_interface

if __name__ == "__main__":
    navegador = NavegadorWebSimulado("urls_validas.txt")
    
    print("\nOlá! Bem-vindo!")
    
    while True:
        url = exibir_interface(navegador.historico_navegacao, navegador.url_atual)
        
        if url.startswith("#"):
            if not navegador.executar_comando(url):
                break
        else:
            navegador.navegar_para(url)