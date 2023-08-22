#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <float.h>
#define PI 3.141592653589793
void impresion_suma_term(double suma,double cant_terminos, double *terminos){
	printf("\n");
	printf("%lf\n", suma);
    printf("Impresión de términos\n");
    for (int i = 0; i < cant_terminos; i++) {
        printf("%lf\n", terminos[i]);
    }

}
double sumatoria_for(double cant_terminos,double *t_for){
	int i;
	double suma = 0;
    double epsilon = 1e-10; // Valor de epsilon para comparación

    for (i = 0; i < cant_terminos; i++) {
        double termino = pow(-1, (double)(i + 2)) / (double)(2 * i + 1);
        suma = suma + termino;
        t_for[i] = suma;

        // Verificar si la diferencia es menor que epsilon
        if (fabs(termino) <= epsilon) {
            break;
        }
    }
    return suma;
}

double sumatoria_while1(double referencia,double precision , double *t_while1){
	int i=0;
	double suma = 0;
	while(1){
		double termino = pow(-1, (double)(i + 2)) / (double)(2 * i + 1);
        suma = suma + termino;	
        t_while1[i]= suma;
		if (fabs((referencia - suma)/referencia) < precision){
			break;
		}
        i++;
	}
	return suma;
}
double sumatoria_while2(double precision , double *t_while2){
	double suma = 0;
    int i = 0;
    double err;
	double s_ant;
    while(1){

        suma = suma + (pow(-1.0,(double)(i+2)))/(double)(2*i+1);

        if (i>0){
            err = fabs(s_ant - suma) / s_ant;
        }
		t_while2[i] = suma;
        if (err < precision){
            break;
        }

        s_ant = suma;
        i++;
    }
	return suma;

}
int main() {
    int n=4000;
    double *t_for = (double *)malloc(sizeof(double) * n);
    double *t_while1 = (double *)malloc(sizeof(double) * n);
    double *t_while2 = (double *)malloc(sizeof(double) * n);
    
    double suma1 = sumatoria_for(n,t_for);
    impresion_suma_term(suma1,4, t_for);
    
    double suma2 = sumatoria_while1(PI/4,1e-4, t_while1);
    impresion_suma_term(suma2,4, t_while1);
    
    double suma3 = sumatoria_while2(1e-5, t_while2);
    impresion_suma_term(suma3,4, t_while2);
    
    free(t_for);
    free(t_while1);
    free(t_while2);

    return 0;
}