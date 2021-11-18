package Aula12;

public class Estoque {
    public static void main(String[] args) {
        Runnable r1 = new Servidores();
        Runnable r2 = new BancodeDados();
        Runnable r3 = new RequisicaoWeb();

        new Thread(r1).start();
        new Thread(r2).start();
        new Thread(r3).start();
    }
}
