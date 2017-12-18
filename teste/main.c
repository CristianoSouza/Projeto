#include <stdio.h>
#include <string.h>

struct voos {
    char codigoId[50];
    char companhiaAerea[200];
    char aeroporto[200];
    char horario[50];
    char situacao[50];
    char estatus[50];
} ;


int main() {
    int i = 0;
    FILE *arquivo;
    struct voos voos_chegada[200];
    if ((arquivo = fopen("chegadas.txt", "r")) == NULL) {
        printf("Erro ao abrir o arquivo.\n");
    } else {
        while (!feof(arquivo)) {
        //while (i<100) {
            fscanf(arquivo, "%[^';'];%[^';'];%[^';'];%[^';'];%[^';'];%[^'\n']\n", voos_chegada[i].codigoId, voos_chegada[i].companhiaAerea, voos_chegada[i].aeroporto, voos_chegada[i].horario, voos_chegada[i].situacao, voos_chegada[i].estatus);
            //fscanf(arquivo, "%[^'\n']\n",  );
            //fscanf(arquivo, "%s", voos_chegada[i].estatus);  voos_chegada[i].estatus
            i++;

        }
        fclose(arquivo);
    }

    int aux;
    for (aux = 0; aux < i; aux++) {
        printf("%s \n", voos_chegada[aux].codigoId);
        printf("%s \n", voos_chegada[aux].companhiaAerea);
        printf("%s \n", voos_chegada[aux].aeroporto);
        printf("%s \n", voos_chegada[aux].horario);
        printf("%s \n", voos_chegada[aux].situacao);
        //printf("%s \n", voos_chegada[aux].estatus); NAO ESTAVA IMPRIMINDO A PRIMEIRA LETRA DO ESTADUS, POR ISSO IMPRIMI CHAR POR CHAR LOGO ABAIXO
        int k = 0;
        while(voos_chegada[aux].estatus[k] != '\0'){
            printf("%c", voos_chegada[aux].estatus[k]);
            k++;
        }
        printf("\n----------------------------------- \n");
    }
    return (0);


}
