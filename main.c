#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <x86intrin.h>
#include <time.h>

int* Crear_arreglo(int N){
    int* arreglo = (int*)malloc(N*sizeof(int));
    for(int i = 0; i<N;i++){
        arreglo[i] = rand() % 10;
    }
    return arreglo;
}
int suma_cubos(int N, int *puntero){
    int suma=0;
    for(int i = 0; i<=N; i++){
        int n = puntero[i];
        int cubo = pow(n,3);
        suma = suma + cubo;
    }

    return suma;
}

int numero_instrucciones(int N){
    //Se inicializa cant_inst por si el valor ingresado por N no esta entre 0 y 3
    int cant_inst = N*9+7;
    return cant_inst;
}

double cpi_clc(int ciclos, int instrucciones){
    double cpi = (double)(ciclos/instrucciones);
    return cpi;
}

double mips_clc(double cpi, double frec){
    double mips = frec/(cpi*pow(10,6));
    return mips;
}

void test (int N){
    double cpi_min, cpi_max, cpi_avg, mips_max, mips_min, mips_avg;
    long int tic, toc, ciclos;
    double cpi,mips;
    int instrucciones = numero_instrucciones(N);
    double frecuencia = 2200000000.0;
    int suma_cpi = 0;
    int suma_mips = 0;
    int max = 1000000;
    for(int i = 0; i<max; i++){
        srand(time(NULL));
        int *arreglo = Crear_arreglo(N);
        tic = __rdtsc();
        suma_cubos(N,arreglo);
        toc = __rdtsc();
        free(arreglo);
        ciclos = toc-tic;
        cpi = cpi_clc(ciclos,instrucciones);

        //Inicializacion maximos y minimos
        if(i == 0){
            cpi_max  = cpi;
            cpi_min = cpi;
        }

        //Asignacion maximos y minimos
        if(i>0){
            if(cpi<cpi_min){
                cpi_min = cpi;
            }
            if(cpi>cpi_max){
                cpi_max = cpi;
            }
        }
        suma_cpi = suma_cpi + cpi;
        suma_mips = suma_mips + mips;
    }
    cpi_avg = suma_cpi/max;
    //calculo mips
    mips_min = mips_clc(cpi_min,frecuencia);
    mips_max = mips_clc(cpi_max,frecuencia);
    mips_avg = mips_clc(cpi_avg,frecuencia);
    printf("El valor minimo de CPI es: %f, para el cual se ejecutan %f MIPS\n",cpi_min, mips_min);
    printf("El valor maximo de CPI es: %f, para el cual se ejecutan %f MIPS\n",cpi_max, mips_max);
    printf("El valor promedio de CPI es: %f, para el cual se ejecutan %f MIPS\n",cpi_avg, mips_avg);

}
int main(int argc, char const *argv[])
{
    int N;
    int exe = 1;
    switch(argc){
        case 1:
            N = 16384;
            break;
        case 2:
            N = atoi(argv[1]);
            break;
        default:
            printf("Se están ingresando más argumentos de los necesarios. Debe introducir un solo número de entrada luego del comando de ejecución.");
            exe = 0;
            break;
    }
    if(exe == 1){
        test(N);
    }
    return 0;
}

//ejecutar y crear .o
//! gcc -os -c main.c -o main.o
//Desensamblar
//objdump -M intel -j .text -D suma_cubos.o
