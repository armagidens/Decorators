from datetime import datetime
import requests
from fake_headers import Headers 


headers = Headers(os='win', browser='opera')


def log_decorator(oldfunction):

    def foo(*args, **kwargs):
        date_time = datetime.now()
        str_time = date_time.strftime('%Y-%m-%d время %H-%M-%S')
        func_name = oldfunction.__name__
        result = oldfunction(*args, **kwargs)
        with open('log/main_logs.txt', 'a', encoding='utf-8') as file:
            file.write(f'\nДата вызова функции: {str_time}\n'
                       f'Имя функции: {func_name}\n'
                       f'Аргументы функции: {args, kwargs}\n'
                       f'Возвращаемое значение функции: {result}\n'
                       f'{"*"*50}\n')
        return result
    return foo


@log_decorator
def get_status(*args):
    url = ','.join(args)
    response = requests.get(url=url, headers=headers.generate())
    return response.status_code




if __name__ == '__main__':
    get_status('https://spb.hh.ru/search/vacancy?text=python&area=1&area=2')
