#include "matrix.h"

/* Reviewer: Ran */

matrix_t* MatCreate(size_t rows, size_t cols, const float* data)
{
	matrix_t* mat;
	assert(rows > 0 && cols > 0 && "Matrix dimensions are impossible.\n");
	
	if (!(mat = malloc(rows *cols * sizeof(matrix_t))))
	{
		return NULL;
	}

	mat->rows = rows;
	mat->cols = cols;
	
	if (!data)
	{
		mat->data = calloc(mat->rows * mat-> cols, sizeof(float));

		if (!mat->data)
		{
			free(mat);

			return NULL;
		}
	}
	else
	{
		mat->data = malloc(rows * cols * sizeof(float));
		memcpy(mat->data, data, rows * cols * sizeof(float));
	}
	
	return mat;
}

void MatDestroy(matrix_t* mat)
{
	free(mat->data);
	free(mat);
	mat = NULL;
}

matrix_t* MatSubMat(const matrix_t* mat, size_t row, size_t col)
{
	size_t i, j, k;
	matrix_t* new_mat;
	
	k = 0;

	if (!mat)
	{
		return NULL;
	}

	assert(row <= mat->rows && col <= mat->cols && "Row or col are non-existent.");

	new_mat = MatCreate(mat->rows - 1, mat->cols -1, NULL);

	for (i = 0; i < mat->rows; i++)
	{
		if (i == row)
		{
			continue;
		}

		for (j = 0; j < mat->cols; j++)
		{
			if (j == col)
			{
				continue;
			}
			new_mat->data[k] = mat->data[mat->cols * i + j];

			k++;
		}
	}

	return new_mat;
}

matrix_t* MatI(size_t n)
{
	size_t i;
	matrix_t* mat;

	assert(n > 0 && "Dimensions are not possible");
	
	mat = MatCreate(n, n, NULL);
	
	for (i = 0; i < n; i++)
	{
		mat->data[i * (n + 1)] = 1;
	}
	
	return mat;
}

matrix_t* MatAdd(const matrix_t* mat1, const matrix_t* mat2)
{
	size_t i;
	matrix_t* result;
	
	assert(mat1 && mat2 && "One matrix or more is NULL");
	
	if (mat1->rows != mat2->rows || mat1->cols != mat2->cols)
	{
		return NULL;
	}
	
	result = MatCreate(mat1->rows, mat1->cols, NULL);
	
	for (i = 0; i < mat1->rows * mat1->cols; i++)
	{
		  result->data[i] = mat2->data[i] + mat1->data[i];
	}
	
	return result;
}

matrix_t* MatMult(const matrix_t* mat1, const matrix_t* mat2)
{
	matrix_t* result;
	size_t mat1_rows, mat2_columns, row_x_col;
	
	assert(mat1 && mat2 && "One matrix or more is NULL");
	
	if (mat1->cols != mat2->rows)
	{
		return NULL;
	}
	
	result = MatCreate(mat1->rows, mat2->cols, NULL);

    for (mat1_rows = 0; mat1_rows < result->rows; mat1_rows++)
    {        
        for (mat2_columns = 0; mat2_columns < result->cols; mat2_columns++)
        {
            for (row_x_col = 0; row_x_col < mat2->rows; row_x_col++)
            {    
                result->data[mat1_rows * result->cols + mat2_columns] +=
                mat1->data[mat1_rows * mat1->cols + row_x_col] *
                mat2->data[row_x_col * mat2->cols + mat2_columns];
            }

        }
    }

	return result;
}

matrix_t* MatScalarMult(matrix_t* mat, float scalar)
{
	size_t i;
	matrix_t* result;

	assert(scalar >= TOLERANCE || scalar <= -TOLERANCE);

	if (!mat)
	{
		return NULL;
	}

	result = MatCreate(mat->rows, mat->cols, NULL);

	for (i = 0; i < mat->rows * mat->cols; i++)
	{
		result->data[i] = mat->data[i] * scalar;
	}
	
	return result;
}

int MatCompare(const matrix_t* mat1, const matrix_t* mat2)
{
	size_t i;

	assert(mat1 && mat2 && (mat1->rows == mat2->rows && mat1->cols == mat2->cols));

	for (i = 0; i < mat1->rows * mat1->cols; i++)
	{
		if (mat1->data[i] - mat2->data[i] >= TOLERANCE ||
			mat1->data[i] - mat2->data[i] <= -TOLERANCE)
		{
			return mat1->data[i] - mat2->data[i];
		}
	}

	return 0;
}
 
matrix_t* MatTranspose(const matrix_t* mat)
{
	size_t i, j;
	matrix_t* result;

	assert(mat);

	result = MatCreate(mat->cols, mat->rows, NULL);

	for (i = 0; i < result->rows; i++)
	{
		for ( j = 0; j < result->cols; j++)
		{
			result->data[i * result->cols + j] = mat->data[j * result->rows + i];
		}
	}

	return result;
}

float MatTrace(const matrix_t* mat)
{

	size_t i;
	float result = 0;

	assert(mat && "Matrix is NULL, cannot compute.");
	assert(mat->cols == mat->rows && "Matrix is not a square matrix.");

	for (i = 0; i < mat->rows; i++)
	{
		result += *(mat->data + i * (mat->cols + 1));
	}
	
	return result;
}

matrix_t* MatInvert(const matrix_t* mat)
{
	short sign;
	size_t row, col;
	matrix_t* adj;
	matrix_t* inv;
	matrix_t* temp_mat;
	matrix_t* transpose;
	
	if (!mat)
	{
		return NULL;
	}

	assert(mat->rows == mat->cols && "Matrix is not square.");
	assert((MatDet(mat) >= TOLERANCE || MatDet(mat) <= -TOLERANCE) && "Matrix is non-invertible.");

	adj = MatCreate(mat->rows, mat->cols, NULL);

	for (row = 0; row < mat->rows; row++)
	{
		for (col = 0; col < mat->cols; col++)
		{
			sign = (row + col) % 2 == 0 ? 1 : -1;

			temp_mat = MatSubMat(mat, row, col);

			*(adj->data + row * mat->cols + col) = sign * MatDet(temp_mat);

			MatDestroy(temp_mat);
		}
	}

	
	transpose = MatTranspose(adj);

	inv = MatScalarMult(transpose, 1 / MatDet(mat));

	MatDestroy(transpose);
	MatDestroy(adj);

	return inv;
}

float MatDet(const matrix_t* mat)
{
	size_t col;
	float det = 0;
    short sign = 1;
	
	assert(mat && "Matrix is NULL.");
	assert(mat->rows == mat->cols && "Matrix is not square.");

    if (mat->rows == 2 && mat->cols == 2)
    {
        return mat->data[0] * mat->data[3] - mat->data[1] * mat->data[2];
    }

    for (col = 0; col < mat->cols; col++)
    {
        matrix_t* sub_mat = MatSubMat(mat, 0, col);

        det += sign * mat->data[col] * MatDet(sub_mat);

        sign *= -1;

        MatDestroy(sub_mat);
    }

    return det;
}

float MatNorm(const matrix_t* mat)
{
	size_t i;
	float result = 0;

	assert(mat && "Matrix is NULL.");

	for (i = 0; i < mat->cols * mat->rows; i++)
	{
		result += pow(mat->data[i], 2);
	}

	return sqrt(result);

}

void MatShape(const matrix_t* mat, size_t dims[2])
{
	if (!mat)
	{
		dims[0] = 0;
		dims[1] = 0;
	}
	else
	{
		dims[0] = mat->rows;
		dims[1] = mat->cols;
	}
}

float MatGetElem(const matrix_t* mat, size_t row, size_t col)
{
	assert(mat && "Matrix is NULL.");
	assert(row < mat->rows && col < mat->cols && "One dimension or more are 0.");

	return mat->data[row * mat->cols + col];
}

