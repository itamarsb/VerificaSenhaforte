# VerificaSenhaforte
Verificador básico para garantir senha forte - Desafio Escola da Nuvem - Módulo Python + Inteligência Artificial + AWS

Verifica se uma senha é forte:
    - Pelo menos 8 caracteres;
    - Contém pelo menos um número;
    - Contém pelo menos um caractere que não seja número (letra ou símbolo).

O núcleo da verificação reside no caractere.isdigit()
Retorna True se o caractere for um número (0 a 9).

Já o not caractere.isdigit() inverte o resultado:
Se o caractere for número, o resultado será False.

Se o caractere for letra, símbolo, espaço, etc., o resultado será True.
