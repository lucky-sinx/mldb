from importlib import resources
import csv
import numpy as np
from typing import Iterable, Iterator, Optional, Set, Union  # noqa: F401


def load_csv_data(
        data_file_path,
):
    """Loads `data_file_name` from `data_module with `importlib.resources`.

    Parameters
    ----------
    data_file_path : str
        Name of csv file to be loaded from `data_module/data_file_name`.
        For example `'wine_data.csv'`.
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

