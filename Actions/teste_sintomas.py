def execute(sintomas: list):
    total = len(sintomas)

    if total == 0:
        return {
            "total_sintomas": total,
            "mensagem": "Nenhum sintoma relatado. Mantenha seus exames de rotina!"
        }
    elif total <= 1:
        return {
            "total_sintomas": total,
            "mensagem": "Aparentemente está tudo bem, mas continue com atenção."
        }
    else:
        return {
            "total_sintomas": total,
            "mensagem": "Foram identificados vários sintomas. Procure um médico para avaliar corretamente."
        }
