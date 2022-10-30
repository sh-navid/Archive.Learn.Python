# NumPy
### Installation
- `pip install numpy`
### Import
- `import numpy as np`
### Concepts
- [Array](numpy_array.py)
  - `.array()`
  - `.dtype, .ndim, .shape`
- [DataTypes](numpy_datatypes.py)
  - `i: int, u: unsigned int, c: complex, f: float`
  - `M: datetime, m: timedelta`
  - `b: bool`
  - `O: object`
  - `S: string, U: unicode string`
  - `V: byte-like object` ??
- [Convert Data Type](numpy_convert_data_type.py)
  - `.astype()`
- Functions
  - [`.reshape()`](numpy_reshape.py)
  - [`np.concatenate(), np.stack(), np.hstack(), np.vstack(), np.dstack()`](numpy_functions.py)
  - [`np.nditer(array), np.ndenumerate(array)`](numpy_access.py)
- Filter
  - [Where](numpy_filter_values.py)
- Access
  - [One Row](numpy_access_one_row.py)
  - [One Column](numpy_access_one_column.py)
  - [Box](numpy_access_range.py)
  - [`.copy()` va `.view()`, `.base`](numpy_access_copy_view.py) <sub>check if returned array is copy or view</sub>
- Math