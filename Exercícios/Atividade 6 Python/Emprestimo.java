import java.util.Scanner;

public class Emprestimo {
    public static void main(String[] args) {
        // Criar o scanner para ler a entrada do usuário
        Scanner scanner = new Scanner(System.in);

        // Solicitar o salário bruto
        System.out.print("Digite o salário bruto: ");
        double salarioBruto = scanner.nextDouble();

        // Solicitar o valor da prestação
        System.out.print("Digite o valor da prestação: ");
        double valorPrestacao = scanner.nextDouble();

        // Calcular o limite máximo de 30% do salário bruto
        double limitePrestacao = salarioBruto * 0.30;

        // Verificar se o valor da prestação está dentro do limite permitido
        if (valorPrestacao <= limitePrestacao) {
            System.out.println("Empréstimo pode ser concedido.");
        } else {
            System.out.println("Empréstimo NÃO pode ser concedido.");
        }

        // Fechar o scanner
        scanner.close();
    }
}
