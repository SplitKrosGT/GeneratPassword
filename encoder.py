from Password import Password
import typer
import time
import os

app = typer.Typer()


@app.command()
def random(count_symbols: int, pin_code: str, check_summa: str):
    typer.echo(f'Колличество доступных символов: {count_symbols}')
    typer.echo(f'Пин код: {pin_code}')
    typer.echo(f'Ключ пароля: {check_summa}')

    start_time = time.time()
    count_random = 0

    while True:
        count_random += 1
        password = Password()
        password.generation(int(count_symbols), pin_code)

        typer.echo(f'Проверяем пароль: {password.password}')

        if check_summa == password.check_summa:
            typer.echo(f'Совпадение: {password.password}')
            typer.echo(f'Количество пройденых вариантов: {count_random}')
            typer.echo(f'Время подбора составило: {time.time() - start_time}')
            break
        else:
            os.system('cls||clear')


if __name__ == "__main__":
    app()