let dados = "dados.json"
let menor;
let maior;

dados.forEach(valores => {
    if (valores < 1) {
        console.log("Sem faturamento")
    }

    menor = Math.min(valores)
    maior = Math.max(valores)
});

console.log("Menor valor: ", menor)
console.log("Maior valor: ", maior)