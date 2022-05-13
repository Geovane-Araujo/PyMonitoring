import os

def monitoring():
    value = os.popen(' docker stats --no-stream --format "{{json .}}"').read()
    values = value.split("\n")
    print(value)
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    monitoring()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
