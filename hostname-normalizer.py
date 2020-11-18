def hostname_normalizer(hostname):
    return re.sub(r'\..*|\\\\.*|\\.*|/.*', '', hostname).upper()
