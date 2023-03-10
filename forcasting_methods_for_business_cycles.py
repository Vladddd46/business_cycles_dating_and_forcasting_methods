

def moving_average(data_values, data_keys, n):
    """
    Computes the n-period moving average of the input data.
    """
    forecast = {}
    for i in range(len(data_values)):
        if i < n:
            pass
        else:
            forecast[data_keys[i]] = round(sum(data_values[i-n:i])/n, 2)
    return forecast
