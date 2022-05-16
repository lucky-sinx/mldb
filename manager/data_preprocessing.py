def feature_filter(data, filter_str):
    return eval("data[:,{}]".format(filter_str))
