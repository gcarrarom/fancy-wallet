import click
import requests

@click.group()
def fancywallet():
    '''
    Fancy Commands to manage your assets
    '''
    pass


@click.group(name='get')
def get_group():
    '''
    Group of commands to get something
    '''
    pass


@click.command(name='price')
@click.argument('stock')
def get_stock_price(stock):
    '''
    Gets the stock price
    '''
    result = requests.get(
        'https://query1.finance.yahoo.com/v8/finance/chart/' + stock)
    if result.status_code == 404:
        click.echo(f'Company {stock} not found!')
        exit(404)
    result_dict = result.json()
    click.echo(result_dict['chart']['result'][0]['meta']['regularMarketPrice'])


get_group.add_command(get_stock_price)

fancywallet.add_command(get_group)
