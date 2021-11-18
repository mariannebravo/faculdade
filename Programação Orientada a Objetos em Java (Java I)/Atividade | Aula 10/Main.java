// Marianne Lourenço Bravo
// 202002496754

package Atividade10;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Produto[] produtos = new Produto[9];
        Scanner coletor = new Scanner(System.in);
        Boolean system = false;
        int indice = 8;

        do {
            System.out.println("Digite 0 para sair do programa");
            System.out.println("Digite 1 para cadastrar produto");
            System.out.println("Digite 2 para listar os produtos existentes");
            int opcao = coletor.nextInt();

            switch(opcao) {
                case 0:
                    system = true;
                    break;
                case 1:
                    //incluindo
                    try {
                        produtos[indice] = new Produto();
                        System.out.println("Digite o nome do produto: ");
                        String nome = coletor.next();
                        produtos[indice].setNome(nome);

                        System.out.println("Digite a descrição do produto: ");
                        String descricao = coletor.next();
                        produtos[indice].setDescricao(descricao);

                        System.out.println("Digite o preço do produto: ");
                        double preco = coletor.nextDouble();
                        produtos[indice].setPreco(preco);
                        indice++;
                        break;
                    } catch (Exception e) {
                        System.out.println("Numero de itens foi excedido.");
                    }

                case 2:
                    // listando itens
                    try {
                        System.out.println(produtos);
                        break;
                    } catch (Exception e) {
                        System.out.println("Ocorreu um erro ao listar itens.");
                    }
                }

        } while(system == false);

        coletor.close();
    }
}
