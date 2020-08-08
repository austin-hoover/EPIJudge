from test_framework import generic_test


def shortest_equivalent_path(path: str) -> str:

    add_slash = path.startswith('/')
    dirs = []

    for token in path.split('/'):
        if token == '..':
            if not dirs or dirs[-1] == '..':
                dirs.append(token)
            else:
                dirs.pop()
        elif token not in ['.', '']:
            dirs.append(token)

    equivalent_path = '/'.join(dirs)
    if add_slash:
        equivalent_path = '/' + equivalent_path

    return equivalent_path

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('directory_path_normalization.py',
                                       'directory_path_normalization.tsv',
                                       shortest_equivalent_path))
