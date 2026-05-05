#include "matrix.h"
#define TOLERANCE 0.0001F

/* Reviewer: Anan */

void MatITest(void);
void MatDetTest(void);
void MatAddTest(void);
void MatMultTest(void);
void MatTraceTest(void);
void MatCreateTest(void);
void MatInvertTest(void);
void MatSubMatTest(void);
void MatCompareTest(void);
void MatDestroyTest(void);
void MatGetElemTest(void);
void MatTransposeTest(void);
void MatScalarMultTest(void);
void PrintMat(const matrix_t*);

int main()
{
/*	float det;
	matrix_t* mat;
	matrix_t* mat1;
	matrix_t* mat2;
	matrix_t* mat_sum;
	matrix_t* mat_mult;

	float arr[][3] = {{10, 8, 5},
					  {2, 0, 1},
					  {1, 1, 1}};
					  
	float arr1[][4] = {{1, 2, 3, 4},
					  {5, 6, 7, 8},
					  {9, 10, 11, 12}};

	float arr2[][4] = {{1, 2, 3, 4},
					   {5, 6, 7, 8},
					   {9, 111, 11, 12},
					   {8, 12, 0, 15.2}};
	 
	mat = MatCreate(3, 3, *arr);
	mat1 = MatCreate(3, 3, *arr1);
	mat2 = MatCreate(3, 3, *arr2);
	mat_sum = MatAdd(mat2, mat2);
	mat_mult = MatMult(mat1, mat2);

	printf("mat1 * mat2:\n");
	PrintMat(mat_mult);

	printf("\nmat2 + mat2:\n");
	PrintMat(mat_sum);

	MatDestroy(mat);
	MatDestroy(mat1);
    MatDestroy(mat2);
	MatDestroy(mat_sum);
    MatDestroy(mat_mult);
*/

	MatITest();
	MatAddTest();
	MatDetTest();
	MatMultTest();
	MatTraceTest();
	MatCreateTest();
	MatInvertTest();
	MatSubMatTest();
	MatDestroyTest();
	MatCompareTest();
	MatTransposeTest();
	MatScalarMultTest();
	
	printf("All tests passed successfully.\n");

	return 0;
}

/* Reviewer: Anan */

void MatCreateTest()
{
    matrix_t* mat;
    
    float arr[][3] = {{1.5, 2, 3},
                      {1, 0, 0},
                      {6, 8, 17}};
    
    mat = MatCreate(3, 3, *arr);

    assert(mat && "Matrix creation failed.");

    MatDestroy(mat);
} 

void MatDestroyTest()
{
    matrix_t* mat;

    float arr[][3] = {{1.5, 2, 3},
                      {1, 0, 0},
                      {6, 8, 17}};
    
    mat = MatCreate(3, 3, *arr);

    MatDestroy(mat);

    assert(mat != NULL && "Matrix not destroyed.");
}


void MatSubMatTest()
{
    size_t i;
    matrix_t* mat;
    matrix_t* sub_mat;
    
    float expected[] = {1.5, 2, 1, 0};
    float arr[][3] = {{1.5, 2, 3},
                      {1, 0, 0},
                      {6, 8, 17}};

    mat = MatCreate(3, 3, *arr);

    sub_mat = MatSubMat(mat, 2, 2);

    for (i = 0; i < sub_mat->rows * sub_mat->cols; i++)
    {
        assert(*(sub_mat->data + i) - *(expected + i) < TOLERANCE &&
               *(sub_mat->data + i) - *(expected + i) > -TOLERANCE);
    }

    MatDestroy(mat);
    MatDestroy(sub_mat);
}

void MatITest()
{
    matrix_t* I;
    matrix_t* unit_mat;

    float unit[][3] = {{1, 0, 0},
                       {0, 1, 0},
                       {0, 0, 1}};
    
    I = MatI(3);
    unit_mat = MatCreate(3, 3, *unit);

    assert(0 == MatCompare(I, unit_mat) && "Comparison failed.");

    MatDestroy(I);
    MatDestroy(unit_mat);
}

void MatAddTest()
{
    size_t i;
    matrix_t* mat1;
    matrix_t* mat2;
    matrix_t* mat3;

    float expected[] = {11.5, 8.2, 8,
                        3, 666, 2,
                        6, 6, 6};

    float arr1[][3] = {{10, 8, 5},
					   {2, 0, 1},
					   {1, 1, 1}};

	float arr2[][3] = {{1.5, 0.2, 3},
					   {1, 666, 1},
					   {5, 5, 5}};

    mat1 = MatCreate(3, 3, *arr1);
    mat2 = MatCreate(3, 3, *arr2);
	mat3 = MatAdd(mat1, mat2);

    for (i = 0; i < mat3->rows * mat3->cols; i++)
    {
        assert(*(mat3->data + i) - *(expected + i) < TOLERANCE &&
               *(mat3->data + i) - *(expected + i) > -TOLERANCE);
    }

    MatDestroy(mat1);
    MatDestroy(mat2);
    MatDestroy(mat3);
}

void MatMultTest()
{
    size_t i;
    matrix_t* mat1;
    matrix_t* mat2;
    matrix_t* mat3;

	float arr1[][4] = {{1, 2, 3, 4},
					   {5, 6, 7, 8},
					   {9, 10, 11, 12}};		

	float arr2[][4] = {{1, 2, 3, 4},
					   {5, 6, 7, 8},
					   {9, 111, 11, 12},
					   {8, 12, 0, 15.2}};

    float expected[] = {70, 395, 50, 116.8,
                        162, 919, 134, 273.6,
                        254, 1443, 218, 430.4};

    mat1 = MatCreate(3, 4, *arr1);
    mat2 = MatCreate(4, 4, *arr2);
	mat3 = MatMult(mat1, mat2);

    for (i = 0; i < mat3->rows * mat3->cols; i++)
    {
        assert(*(mat3->data + i) - *(expected + i) < TOLERANCE &&
        *(mat3->data + i) - *(expected + i) > -TOLERANCE);
    }

    MatDestroy(mat1);
    MatDestroy(mat2);
    MatDestroy(mat3);
}

void MatScalarMultTest()
{
    size_t i;
    int scalar = 2;
    /* expected: 2 0 0
    *            0 2 0
    *            0 0 2
    */
    matrix_t* unit_mat = MatI(3);             
    matrix_t* scaled_mat = MatScalarMult(unit_mat, scalar);
    
    for (i = 0; i < unit_mat->rows * unit_mat->cols; i++)
    {
        assert((*(scaled_mat->data + i) - *(unit_mat->data + i) * scalar < TOLERANCE &&
                *(scaled_mat->data + i) - *(unit_mat->data + i) * scalar > -TOLERANCE));
    }

    MatDestroy(unit_mat);
    MatDestroy(scaled_mat);
}

void MatCompareTest()
{
	size_t status;
    float unit[][3] = {{1, 0, 0},
                       {0, 1, 0},
                       {0, 0, 1}};

    matrix_t* unit_mat = MatI(3);
    matrix_t* I =  MatCreate(3, 3, *unit);

    status = MatCompare(unit_mat, I);

    assert(0 == status);

    MatDestroy(I);
    MatDestroy(unit_mat);
}

void MatTransposeTest()
{
	matrix_t* mat;
    matrix_t* transpose;
	matrix_t* supposed_transpose;

    float arr1[][4] = {{95, 118, 141, 164},
                       {11, 14, 17, 20},
                       {15, 18, 21, 24}};

    float expected[][3] = {{95, 11, 15},
                           {118, 14, 18},
                           {141, 17, 21},
                           {164, 20, 24}};

    mat = MatCreate(3, 4, *arr1);
    transpose = MatCreate(4, 3, *expected);
    supposed_transpose = MatTranspose(mat);

    assert(0 == MatCompare(supposed_transpose, transpose));
    
    MatDestroy(mat);
    MatDestroy(transpose);
    MatDestroy(supposed_transpose);
}

void MatTraceTest()
{
    matrix_t* mat;

	float trace = 10.15;
    float arr[][3] = {{1.5, 2, 11},
                      {6, 0.25, -6},
                      {1, 2, 8.4}};

    mat = MatCreate(3, 3, *arr);
    
    assert(MatTrace(mat) == trace);

    MatDestroy(mat);
}

void MatInvertTest()
{
    matrix_t* mat;
    matrix_t* inverse_mat;
    float arr[][3] = {{10, 8, 5},
                      {2, 0, 1},
                      {1, 1, 1}};

    mat = MatCreate(3, 3, *arr);
    inverse_mat = MatInvert(mat);
    
    MatDestroy(mat);
    MatDestroy(inverse_mat);
}

void MatDetTest()
{
    matrix_t* mat;
	float det = -8;
    float arr[][3] = {{10, 8, 5},
                      {2, 0, 1},
                      {1, 1, 1}};

    mat = MatCreate(3, 3, *arr);
    
    assert(MatDet(mat) - det < TOLERANCE && MatDet(mat) - det > -TOLERANCE);

    MatDestroy(mat);
}

void MatNormTest()
{
    matrix_t* mat;
    matrix_t* mat1;

    float norm = 14.0357;
    float norm1 = 268.8829;

    float arr[][3] = {{10, 8, 5},
                      {2, 0, 1},
                      {1, 1, 1}};

    float arr1[][4] = {{95, 118, 141, 164},
                       {11, 14, 17, 20},
                       {15, 18, 21, 24}};

    mat = MatCreate(3, 3, *arr);
    mat1 = MatCreate(4, 3, *arr1);

    assert(MatNorm(mat) - norm > TOLERANCE && MatNorm(mat) - norm > -TOLERANCE);
    assert(MatNorm(mat1) - norm1 > TOLERANCE && MatNorm(mat1) - norm1 > -TOLERANCE);

    MatDestroy(mat);
    MatDestroy(mat1);
}

void MatShapeTest()
{
    float arr[][3] = {{10, 8, 5},
                      {2, 0, 1},
                      {1, 1, 1}};
    short dims[2];
    matrix_t* mat = MatCreate(3, 3, *arr);

    MatShapeTest(mat, dims);

    assert(dims[0] == 3 && dims[1] == 3);

    MatDestroy(mat);
}

void MatGetElemTest()
{
    float arr[][3] = {{10, 8, 5},
                      {2, 0, 1},
                      {1, 1, 1}};

    matrix_t* mat = MatCreate(3, 3, *arr);

    assert(0 == MatGetElem(mat, 1, 1));

    MatDestroy(mat);
}

void PrintMat(const matrix_t* mat)
{
	size_t row;
	size_t col;
	
	for(row = 0; row < mat->rows; row++)
	{
		for(col = 0; col < mat->cols; col++)
		{
			printf(col != mat->cols - 1 ? "%.4f, " : "%.4f\n",  *(mat->data + (mat->cols * row) + col));
		}
	}
}