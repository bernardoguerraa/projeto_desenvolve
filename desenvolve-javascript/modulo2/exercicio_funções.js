const soma = (a, b) => a + b;
const subtrai = (a, b) => a - b;
const multiplica = (a, b) => a * b;
const divide = (a, b) => b !== 0 ? a / b : 'Divisão por zero';

const mostraResultado = (num1, num2) => {
  console.log(`[SOMA] entre ${num1} e ${num2}:`, soma(num1, num2));
  console.log(`[SUBTRAI] entre ${num1} e ${num2}:`, subtrai(num1, num2));
  console.log(`[MULTIPLICA] entre ${num1} e ${num2}:`, multiplica(num1, num2));
  console.log(`[DIVIDE] entre ${num1} e ${num2}:`, divide(num1, num2));
};

mostraResultado(10, 5);
