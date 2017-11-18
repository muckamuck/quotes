import random


data_file = 'data'
data = None


def lambda_handler(event, context):
    global data

    if not data:
        data = read_data()

    idx = random.randint(0, len(data) - 1)
    wisdom = data[idx]
    return {
        'statusCode': 200,
        'body': wisdom,
        'headers': {
            'Content-Type': 'text/plain'
        }
    }


def read_data():
    print('read_data() called')
    with open(data_file) as f:
        content = f.readlines()
        content = [x.strip('\n') for x in content]

    return content


if __name__ == '__main__':
    r = lambda_handler(None, None)
    print(r)
