#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#define pi 3.141592653 


double seriepifor(int cant_terminos, double *term_for){
    double valorserie = 0;
    for(int i = 0; i<=cant_terminos; i++){
        valorserie = valorserie + pow(-1,i)*1/(2*i+1);
        term_for[i] = valorserie;
    }



    return valorserie;
}
double seriepiwhile1(double referencia, double precision, double *term_w1) {
    double valorseriew1 = 0;
    int i = 0;
    double error;
    
    while (1) {
        double termino = pow(-1, i) * 1.0 / (2 * i + 1);
        valorseriew1 += termino;
        term_w1[i] = valorseriew1;
        i++;
        error = fabs(termino);
        if (error <= precision) {
            break;
        }
    }
    
    return valorseriew1;
}



double seriepiwhile2(double precision_w2, double *term_w2){
    double valorseriew2 = 0;
    double referencia = pi/4;
    double error;
    int i = 0;
    while (1)
    {
        valorseriew2 = valorseriew2 + pow(-1,i)*1/(2*i+1);
        term_w2[i] = valorseriew2;
        error = fabs(valorseriew2-referencia);
        if (error<=precision_w2)
        {
            break;
        }
        
        i++;
    }
    return valorseriew2;
}


int main(int argc, char const *argv[])
{   
    //Datos for
    int cant_terminos = 4000;
    //Datos while 1
    int referencia = pi/4;
    //Datos while 2
    double precision = 1e-4;
    double precision_w2 = 1e-5;
    //generando espacio en la memoria para los terminos de cada serie
    double* term_for = (double *)malloc(sizeof(double)*cant_terminos);
    double* term_w1 = (double *)malloc(sizeof(double)*cant_terminos);
    double* term_w2 = (double *)malloc(sizeof(double)*cant_terminos);
    double resultado_for = seriepifor(cant_terminos, term_for);
    double resultado_while1 = seriepiwhile1(referencia,precision,term_w1);
    //double resultado_while2 = seriepiwhile2(precision_w2,term_w2);
    //printf("Resultado serie while2: %f",resultado_while2);
    //Impresion de resultados de la serie calculada por el ciclo for
    for (int i = cant_terminos-50; i <= cant_terminos; i++)
    {
        printf("%f\n",term_for[i]);
    }
    printf("Valor esperado serie for: %f\n",resultado_for);
    //Impresion while1
    printf("Impresion terminos while 1\n--------------------------\n");
    //Ceerca a la iteracion 5000 el valor deja de cambiar
    for (int i = 4950; i <= 5000; i++)
    {
        printf("%f\n",term_w1[i]);
    }
        printf("Resultado esperado: %f\n",resultado_while1);
    
    free(term_for);
    free(term_w1);
    free(term_w2);
    return 0;
}
