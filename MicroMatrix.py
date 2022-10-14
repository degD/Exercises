
class UMatrix:
    """Create a matrix object. UMatrix, or micro-matrix. 
    
    Offers some base functionalities to be used in other projects. 
    
    Matrix rows/columns are numbered from 1, which differs from the usual 0-indexing."""
    
    def __init__(self, w=1, h=1, init_c=0, pre_def=False):
        """Create a UMatrix object. If a pre-defined 2D array(list) exists, it can be used 
        as an argument for the pre_def parameter. Otherwise, use w, h, init_c to define
        the matrix.
        
        w: width
        h: height
        init_c: initial element
        """
        
        if pre_def:
            
            if self._check_pre_def(pre_def):
                self.matrix_data = pre_def
                self.width = len(self.matrix_data[0])
                self.height = len(self.matrix_data)
            else:
                raise ValueError('Pre-defined 2D array is incorrect!')

        else:
            self.width = w
            self.height = h
            row = [init_c for _ in range(w)]
            self.matrix_data = [list(row) for _ in range(h)]
                
    def _check_pre_def(self, test_input):
        """Checks the test_input, to be sure that it's a 2-dimensional array,
        that's suitable to form a matrix. 
        
        Returns True if it is, and False otherwise.
        """
        
        if isinstance(test_input, list) and len(test_input) > 0:
            
            if isinstance(test_input[0], list):
                elem_len = len(test_input[0])
            else:
                return False
            
            for elem in test_input[1:]:
                if not isinstance(elem, list) or elem_len != len(elem):
                    return False
            
            return True
        return False
    
    def ret_row_n(self, n):
        """Return the n-th row."""
        
        return self.matrix_data[n-1]
        
    def ret_col_n(self, n):
        """Return the n-th column."""
        
        res_col = []
        for row in self.matrix_data:
            res_col.append(row[n-1])
    
        return res_col
    
    def dimensions(self):
        """Return the dimensions of matrix."""
        
        return f'{self.width}x{self.height}'
    
    def change_elem(self, row, column, value):
        """Changes value of the desired location."""
        
        self.matrix_data[row-1][column-1] = value
        
    def get_elem(self, row, column):
        """Gets value of the desired location."""
        
        return self.matrix_data[row-1][column-1]
    
    def __str__(self):
        
        res = ''
        for row in self.matrix_data: 
            res += str(row)
            res += '\n'
        
        return res
            
    def __repr__(self):
        return str(self.matrix_data)
        

if __name__ == '__main__':
    
    print('Lets do some experiments.')
    
    m1 = UMatrix(w=4, h=3, init_c='k')
    print(m1.ret_row_n(1))
    print(m1.ret_col_n(1))
    print(m1.dimensions())
    print('Changing 1,1 from k to K')
    m1.change_elem(1, 1, 'K')
    print(m1.get_elem(1, 1))
    print(m1)
    
    m_data = [[1, 2, 3],
              [1, 2, 3]]
    m2 = UMatrix(pre_def=m_data)
    print(m2)