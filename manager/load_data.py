from importlib import resources
import csv
import numpy as np
from typing import Iterable, Iterator, Optional, Set, Union  # noqa: F401


DATA_MODULE = "sklearn.datasets.data"
DESCR_MODULE = "sklearn.datasets.descr"
IMAGES_MODULE = "sklearn.datasets.images"


def load_csv_data(
        data_file_path,
        *,
        data_module=DATA_MODULE,
        descr_module=DESCR_MODULE,
):
    """Loads `data_file_name` from `data_module with `importlib.resources`.

    Parameters
    ----------
    data_file_path : str
        Name of csv file to be loaded from `data_module/data_file_name`.
        For example `'wine_data.csv'`.

    data_module : str or module, default='sklearn.datasets.data'
        Module where data lives. The default is `'sklearn.datasets.data'`.

    descr_file_name : str, default=None
        Name of rst file to be loaded from `descr_module/descr_file_name`.
        For example `'wine_data.rst'`. See also :func:`load_descr`.
        If not None, also returns the corresponding description of
        the dataset.
    """
    with open(data_file_path) as csv_file:
        data_file = csv.reader(csv_file)
        temp = next(data_file)
        n_samples = int(temp[0])
        n_features = int(temp[1])
        target_names = np.array(temp[2:])
        data = np.empty((n_samples, n_features))
        target = np.empty((n_samples,), dtype=int)

        for i, ir in enumerate(data_file):
            data[i] = np.asarray(ir[:-1], dtype=np.float64)
            target[i] = np.asarray(ir[-1], dtype=int)

    return data, target, target_names

