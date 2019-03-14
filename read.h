int read_vector(FILE *file, const char txt_name[], int vector[], int vector_size)
{	
	file = fopen(txt_name, "r");
	int i = 0;
	
	if (file == NULL)
		printf("Erro, nao foi possivel abrir o arquivo\n");
	else {
		while( (fscanf(file,"%d\n", &vector[i])) !=EOF ){ 
			printf("Valor lido: %d\n", vector[i]);
			i++;
		}
		
		vector_size = i;
		return vector_size;
	}	
	
}

