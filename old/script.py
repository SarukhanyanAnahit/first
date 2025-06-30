import os

c_path = os.getcwd()

def create(fname, content=''):
    with open(fname, 'w') as f:
        f.write(content)

file_path = os.path.join(c_path, 'files')
if not os.path.exists(file_path):
    os.mkdir(file_path)
if not os.listdir(file_path):
    create(os.path.join(file_path, 'a.txt'))
    create(os.path.join(file_path, 'b.txt'))
    create(os.path.join(file_path, 'c.txt'))

def read(fname):
    with open(fname) as c:
        return c.read()

def write_into(cnt, filename):
    with open(filename, 'a') as file:
        file.write(cnt + '\n')

def main():
    result_file = os.path.join(c_path, 'result5.txt')
    if not os.path.exists(result_file):
        create(result_file)

    content = os.listdir(file_path)
    for el in content:
        a = read(os.path.join(file_path, el))
        write_into(el, result_file)
        write_into(a + '\n', result_file)



main()
