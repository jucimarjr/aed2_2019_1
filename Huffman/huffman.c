#include <stdio.h>
#include <stdlib.h>
#include <string.h>
 
#define BYTES 256
 
struct huffman_code 
{
	int nbits;
	int code;
};

typedef struct huffman_code huffman_code_t;
 
struct huffheap 
{
	int *h;
	int n, s, cs;
	long *f;
};
typedef struct huffheap heap_t;
 
/* heap handling funcs */
static heap_t *_heap_create(int s, long *f)
{
	heap_t *h;
	h = malloc(sizeof(heap_t));
	h->h = malloc(sizeof(int)*s);
	h->s = h->cs = s;
	h->n = 0;
	h->f = f;
	return h;
}
 
static void _heap_destroy(heap_t *heap)		/*free up memory space*/
{
	free(heap->h);
	free(heap);
}
 
#define swap_(I,J) do { int t_; t_ = a[(I)];	\
		a[(I)] = a[(J)]; a[(J)] = t_; } while(0)	/*funtion to swip values I and J*/

static void _heap_sort(heap_t *heap)
{
	int i=1, j=2; /* gnome sort */
	int *a = heap->h;

	while(i < heap->n) 
	{ /* smaller values are kept at the end */
		if ( heap->f[a[i-1]] >= heap->f[a[i]] ) 
		{
			i = j; j++;
		} else 
		{
			swap_(i-1, i);
			i--;
			i = (i==0) ? j++ : i;
		}
	}
}

#undef swap_
 
static void _heap_add(heap_t *heap, int c)		
{
	if ( (heap->n + 1) > heap->s ) 
	{
		heap->h = realloc(heap->h, heap->s + heap->cs);
		heap->s += heap->cs;
	}
	heap->h[heap->n] = c;
	heap->n++;
	_heap_sort(heap);
}
 
static int _heap_remove(heap_t *heap)
{
	if ( heap->n > 0 ) 
	{
		heap->n--;
		return heap->h[heap->n];
	}
	return -1;
}
 
/* huffmann code generator */
huffman_code_t **create_huffman_codes(long *freqs)
{
	huffman_code_t **codes;
	heap_t *heap;
	long efreqs[BYTES*2];
	int preds[BYTES*2];
	int i, extf=BYTES;
	int r1, r2;

	memcpy(efreqs, freqs, sizeof(long)*BYTES);
	memset(&efreqs[BYTES], 0, sizeof(long)*BYTES);

	heap = _heap_create(BYTES*2, efreqs);
	if ( heap == NULL ) return NULL;

	for(i=0; i < BYTES; i++) if ( efreqs[i] > 0 ) _heap_add(heap, i);

	while( heap->n > 1 )
	{
		r1 = _heap_remove(heap);
		r2 = _heap_remove(heap);
		efreqs[extf] = efreqs[r1] + efreqs[r2];
		_heap_add(heap, extf);
		preds[r1] = extf;
		preds[r2] = -extf;
		extf++;
	}
	r1 = _heap_remove(heap);
	preds[r1] = r1;
	_heap_destroy(heap);

	codes = malloc(sizeof(huffman_code_t *)*BYTES);

	int bc, bn, ix;
	for(i=0; i < BYTES; i++) 
	{
		bc=0; bn=0;
		if ( efreqs[i] == 0 ) 
		{
			codes[i] = NULL; continue; 
		}
		ix = i;
		while( abs(preds[ix]) != ix ) {
			bc |= ((preds[ix] >= 0) ? 1 : 0 ) << bn;
			ix = abs(preds[ix]);
			bn++;
		}
		codes[i] = malloc(sizeof(huffman_code_t));
		codes[i]->nbits = bn;
		codes[i]->code = bc;
	}

	return codes;
}
 
void free_huffman_codes(huffman_code_t **c)
{
	int i;

	for(i=0; i < BYTES; i++) free(c[i]);
	free(c);
}
 
#define MAXBITSPERCODE 100
 
void inttobits(int c, int n, char *s) /*generates each value, it's respective binary number*/
{
	s[n] = 0;
	while(n > 0) 
	{
		s[n-1] = (c%2) + '0';
		c >>= 1; n--;
	}
}

void print(huffman_code_t **r)
{
	int i;
	char strbit[MAXBITSPERCODE];
	for(i=0; i < BYTES; i++)		/*print results*/
	{
		if ( r[i] != NULL ) 
		{
			inttobits(r[i]->code, r[i]->nbits, strbit);
			printf("%c %s\n", i, strbit);
		}
	}
}
 
const char *test = "this is an example for huffman encoding";
 
int main()
{
	huffman_code_t **r;
	int i;
	const char *p;
	long freqs[BYTES];

	memset(freqs, 0, sizeof freqs);		/*used to fill a block of memory with the 0 value*/

	p = test;
	while(*p != '\0') freqs[*p++]++;		/*counting the frequecy witch is visited*/

	r = create_huffman_codes(freqs);

	print(r);

	free_huffman_codes(r);

	return 0;
}

