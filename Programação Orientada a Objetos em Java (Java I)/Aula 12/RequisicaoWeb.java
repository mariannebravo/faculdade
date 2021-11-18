package Aula12;

public class RequisicaoWeb implements Runnable{
    private int i;
    private static int cont = 0;
    public void run() {
        while(true) {
            try {
                System.out.println("Servidores: " + i++);
                Thread.sleep(5000);
            } catch (InterruptedException e) {

            }
        }
    }
    public RequisicaoWeb() {
        cont++;
    }
}
