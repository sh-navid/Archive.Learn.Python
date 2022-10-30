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
- [Access](numpy_access.py)
  - `.copy(), .view()`
  - `.base` <sub>check if returned array is copy or view</sub>
  - `np.nditer(array), np.ndenumerate(array)`
- [Functions](numpy_functions.py)
  - `.reshape()`
  - `np.concatenate()`
  - `np.stack(), np.hstack(), np.vstack(), np.dstack()`
- Filter
  - [Where](numpy_filter_values.py)
- Access
  - One Row
  - One Column
  - Box