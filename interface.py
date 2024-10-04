def exibir_interface(historico_navegacao, url_atual):
    print(f"\nHistórico de visitas: {historico_navegacao}")
    print(f"Página atual: [{url_atual}]")
    print("\nDigite #help para ver as opções.")
    
    url = input("\nURL (ou comando): ").strip()
    return url