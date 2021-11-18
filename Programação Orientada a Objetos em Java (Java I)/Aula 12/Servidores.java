package Aula12;

public class Servidores implements Runnable{
    private int i;
    private static int cont = 0;

    public void run() {
    while ( i <= 10 ) {
            System.out.println("Servidor: " + i++);
        }
    }
    public Servidores() {
        cont++;
    }
}
