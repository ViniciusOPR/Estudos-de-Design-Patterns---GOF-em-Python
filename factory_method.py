"""
Factory method é um padrão de criação que permite definir uma interface para
criar objetos, mas deixa as subclasses decidirem quais objetos criar. O
Factory method permite adiar a instanciação para as subclasses, garantindo o
baixo acoplamento entre classes.
"""
from abc import ABC, abstractmethod


class Veiculo(ABC):
    @abstractmethod
    def buscar_cliente(self) -> None: pass


class CarroLuxo(Veiculo):
    def buscar_cliente(self) -> None:
        print('Carro de luxo está buscando o cliente...')


class CarroPopular(Veiculo):
    def buscar_cliente(self) -> None:
        print('Carro popular está buscando o cliente...')


class MotoLuxo(Veiculo):
    def buscar_cliente(self) -> None:
        print('Moto de luxo está buscando o cliente...')


class MotoPopular(Veiculo):
    def buscar_cliente(self) -> None:
        print('Moto popular está buscando o cliente...')

class VeiculoFactory(ABC):
    def __init__(self, tipo) -> None:
        self.veiculo = self.get_veiculo(tipo)

    @staticmethod
    @abstractmethod
    def get_veiculo(tipo: str) -> Veiculo: pass

    def buscar_cliente(self) -> None:
        self.veiculo.buscar_cliente()

class ZonaNorteVeiculoFactory(VeiculoFactory):
    @staticmethod
    def get_veiculo(tipo: str) -> Veiculo: # type: ignore
        if tipo == 'luxo':
            return CarroLuxo()
        if tipo == 'popular':
            return CarroPopular()
        if tipo == 'moto':
            return MotoPopular()
        if tipo == 'moto_luxo':
            return MotoLuxo()
        assert 0, 'Veiculo não existe'

class ZonaSulVeiculoFactory(VeiculoFactory):
    @staticmethod
    def get_veiculo(tipo: str) -> Veiculo:  # type: ignore
        if tipo == 'popular':
            return CarroPopular()
        if tipo == 'moto':
            return MotoPopular()
        assert 0, 'Veiculo não existe'

if __name__ == '__main__':
    from random import choice
    veiculos_disponiveis_zona_norte = ['luxo', 'popular', 'moto', 'moto_luxo']
    veiculos_disponiveis_zona_sul = ['popular', 'moto']
    
    print('ZONA NORTE')
    for i in range(10):
        veiculo = ZonaNorteVeiculoFactory(choice(veiculos_disponiveis_zona_norte)) 
        veiculo.buscar_cliente()
    
    print()

    print('ZONA SUL')
    for i in range(10):
        veiculo2 = ZonaSulVeiculoFactory(choice(veiculos_disponiveis_zona_sul))
        veiculo2.buscar_cliente()