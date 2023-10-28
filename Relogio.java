public class Relogio{
    
    public static int hora(){
        int min = 0;
        int max_h = 12;

        int range_h = max_h - min +1;
        int hora = (int)(Math.random()*range_h + min);

        return hora;
    }

    public static int minuto(){
        int min = 0;
        int max_m = 60;

        int range_m = max_m - min +1;
        int minuto = (int)(Math.random()*range_m + min);

        return minuto;
    }

    public static int retornaAnguloRelogio(int hora, int minuto){

        int angulo = Math.abs((60*hora - 11*minuto)/2);

        if (angulo>180){
            int ang_2 = 360 - angulo;
            return ang_2;
        }
        else{
            return angulo;
        }
    }
    public static void main(String[] args){
        int ang;
        int hora_r;
        int minuto_r;

        hora_r = hora();
        minuto_r = minuto();
        ang = retornaAnguloRelogio(hora_r,minuto_r);
        System.out.print("Hora:" + hora_r + ":" + minuto_r + "\n");
        System.out.println("Ângulo:" + ang + "°");
    }
}