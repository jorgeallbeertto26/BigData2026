
dado_a = 30
dado_b = 10
dado_c = 20

if dado_a <= dado_b and dado_b <= dado_c:
    primeiro, segundo, terceiro = dado_a, dado_b, dado_c
elif dado_a <= dado_c and dado_c <= dado_b:
    primeiro, segundo, terceiro = dado_a, dado_c, dado_b
elif dado_b <= dado_a and dado_a <= dado_c:
    primeiro, segundo, terceiro = dado_b, dado_a, dado_c
elif dado_b <= dado_c and dado_c <= dado_a:
    primeiro, segundo, terceiro = dado_b, dado_c, dado_a
elif dado_c <= dado_a and dado_a <= dado_b:
    primeiro, segundo, terceiro = dado_c, dado_a, dado_b
else:
    primeiro, segundo, terceiro = dado_c, dado_b, dado_a

print(f"Ordem crescente: {primeiro}, {segundo}, {terceiro}")