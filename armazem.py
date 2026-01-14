import pprint

ruas = "ABCDEFGHIJKLMNOPQRSTU"
nivel = ("A","B","C","D")
armazem = {}

def gerar_armazem(armazem):
    for letra in ruas: 
        for colunas in range(1, 71): 
            for andar in nivel:
                visual = (f"{letra} - {colunas} - {andar}")
                armazem [letra,colunas,andar] = {
                        "Rua": letra,
                        "Coluna": colunas,
                        "Andar": andar,
                        "Visual": visual
                        }
    # Feedback para o Usuário (Fora do Loop)
    print(f"\nItens criados:",len(armazem))
    
    # Simulação de Consulta (Teste de Sanidade)
    # Vamos ver se o endereço A-1-A foi criado corretamente?
    print("\n--- Auditoria de Amostra (A-1-A) ---")
    pprint.pprint(armazem['A', 1, 'A'])

gerar_armazem(armazem)
