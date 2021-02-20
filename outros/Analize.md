# Analizar 2 informações

# Informação 1

> formato: **texto**

porco

# Informação 2

> formato: **texto**

forno

## processamento da informação

* Manter em formato texto


## Maneiras de analizar

### Caracteres

p   o   r   c   o
                    - 
f   o   r   n   o
---------------------
f   -   -   n   -

> 2 Caracteres mudaram: f, n

##### posição 1
-p
+f

##### posição 4
-c
+n

#### Possíveis Analizes

* Quantidade e posição dos caracteres
* Formato de caracteres

### Análize Fonética

> Pré processo *Fonemas*
> * resgata cada caracter. Ex: f
> * transforma em fonema. (Adiciona informações como: Fricativo, etc...)
> * Gerar um **token** para comparação
> * <code>
    Ex:
        # cria o fonema
        fricativo = 10;
        abertura_vertical = 12;

        # soma as propriedades do fonema
        total = fricativo + abertura_vertical + ...;

        # token é um inteiro que pode ser comparado
        token = geraTokenDeComparacao(total);
</code>

O processamento (comparação) começa aqui:

Compara dos Tokens de P e F: 
<code>
    diferença = token_p - token_f;
</code>

