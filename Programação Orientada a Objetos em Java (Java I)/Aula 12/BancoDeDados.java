package Aula12;

public class BancodeDados implements Runnable{
    private int i;
    private static int cont = 0;

    public void run() {
        while( i <= 10) {
            System.out.println("Banco de dados: " + i++);
        }
    }
    public BancodeDados() {
        cont++;
    }
}
