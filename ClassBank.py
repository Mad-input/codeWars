"""
1. Cree una clase llamada "CuentaBancaria" que tenga atributos privados para el número de cuenta, 
el titular de la cuenta y el saldo. Cree métodos para depositar, retirar y transferir dinero entre cuentas. 
Asegúrese de que no se puedan modificar ni el número de cuenta ni el titular de la cuenta una vez creada la instancia 
de la clase. Además, que el saldo nunca sea negativo y que las transferencias solo puedan realizarse entre cuentas de
la misma moneda.
2. Cree una Interface llamada Juego con los métodos abstractos iniciar, mostrar_puntaje, terminar.  
Cree un juego sencillo que implemente la interfaz Juego y compruebe el funcionamiento del mismo.
Mi trabajo

"""

# class CuentaBancaria:
#     def __init__(self, numero_cuenta: int, titular: str, saldo: float, moneda='COP'):
#         self.__numero_cuenta = numero_cuenta
#         self.__titular = titular
#         self.__saldo = saldo
#         self.moneda = moneda

#     def obtener_titular(self):
#         return self.__titular
    
#     def obtener_numero_cuenta(self):
#         return self.__numero_cuenta
    
#     def obtener_saldo(self):
#         return self.__saldo
       
#     def depositar(self, monto, moneda='COP'):
#         if(moneda != self.moneda):
#             return print('Monena Invalida')
#         else:
#             if not str(monto).isnumeric(): return print('Dato Invalido\n')
#             elif monto <= 0: return print('Valor muy bajo para depositar\n') 
            
#             print(f'Depositando dinero en la cuenta de {self.obtener_titular()}....')
#             self.__saldo += float(monto)
#             print(f"""Dinero Depositado!\nSaldo nuevo: {self.__saldo:,}\n""")
        
#     def retirar(self,monto):
#         if not str(monto).isnumeric(): return print('Dato Invalido')
#         elif monto > self.__saldo or monto <= 0: return print(f'Saldo invalido, saldo de tu cuenta {self.__saldo}')
        
#         print(f'Retirando dinero de la cuenta de {self.obtener_titular()}....')
#         self.__saldo -= float(monto)
#         print(f"""Dinero Retirado! \n Saldo nuevo: {self.__saldo:,}\n""")
        
#     def transferir(self, cuenta, monto, moneda='COP'):
#         #Tranferir dinero a otra cuenta verificando que la cuenta exista y, que la moneda sea la misma
#         if isinstance(cuenta, CuentaBancaria) and moneda == self.moneda:
#             if monto <= 0 or monto > self.__saldo: return print('Monto invalido')
            
#             print(f'Enviando Dinero a {cuenta.obtener_titular()}...')
#             self.__saldo -= monto
#             cuenta.__saldo += monto
#             print(f'Dinero enviado!, saldo actual de tu cuenta: {self.__saldo:,}\n')
#         else:
#             return print('Cuenta Invalida!, revise el tipo de moneda que esta enviando o el numero de cuenta')

#? usage
# cuenta1 = CuentaBancaria(424324234,'Miguel', 100000, 'COP')
# cuenta2 = CuentaBancaria(424324234,'Daniela', 20_000)
# cuenta3 = CuentaBancaria(424324234,'Juan', 30_000)
# cuenta2.depositar(40_000)
# cuenta3.transferir(cuenta1, 10_000, 'COP')
# cuenta1.retirar(30_000)


#? Game

from abc import abstractmethod, ABCMeta
import time

class ControllerGame(metaclass= ABCMeta):
    @abstractmethod
    def Start(self):
        pass
    
    @abstractmethod
    def game_over(self):
        pass
    
    @abstractmethod
    def show_points(self):
        pass
    
    
class GameCountry(ControllerGame):
    #Colores de la consola
    RESET = "\033[0m"
    RED = "\033[31m"
    MAGENTA = "\033[35m"
    BG_YELLOW = "\033[43m"
    BG_BLUE = "\033[44m"
    BG_MAGENTA = "\033[45m"
    BG_CYAN = "\033[46m"
    BG_WHITE = "\033[47m"
    # Códigos ANSI para estilos de texto
    BRIGHT = "\033[1m"
    DIM = "\033[2m"
    
    points = 0
    attempts = 0
    maxAttempts = 5
    choices = [
    {
        "choice": "¿Cuál es la capital de Francia?",
        "answer": "paris"
    },
    {
        "choice": "¿Cuál es la capital de España?",
        "answer": "madrid"
    },
    {
        "choice": "¿Cuál es la capital de Alemania?",
        "answer": "berlin"
    },
    {
        "choice": "¿Cuál es la capital de Italia?",
        "answer": "roma"
    },
    {
        "choice": "¿Cuál es la capital de Reino Unido?",
        "answer": "londres"
    },
    {
        "choice": "¿Cuál es la capital de Japón?",
        "answer": "tokio"
    },
    {
        "choice": "¿Cuál es la capital de Canadá?",
        "answer": "ottawa"
    },
    {
        "choice": "¿Cuál es la capital de Australia?",
        "answer": "canberra"
    },
    {
        "choice": "¿Cuál es la capital de Brasil?",
        "answer": "brasilia"
    },
    {
        "choice": "¿Cuál es la capital de México?",
        "answer": "ciudad de mexico"
    }
]

    def Start(self):
        
        #Inicia el juego
        print('Bienvenio al juego de los paises.\nDonde tendras que responder preguntas\n')
        print('Iniciando...')
        time.sleep(1)
        print('Iniciando..')
        time.sleep(1)
        print('Iniciando.')
        time.sleep(1)
        
        pases = 0
        while True:
            if self.attempts > self.maxAttempts:
                self.game_over(f'{self.BG_MAGENTA}{self.BRIGHT}Perdiste, Juego Terminado{self.RESET}')
                break
            else:
                if pases > len(self.choices) - 1:
                    self.game_over(f'{self.BG_CYAN}Felicidades Ganaste!{self.RESET}')
                    break 
                else:
                    choice = self.choices[pases]
                    userAnswer = input(f'{choice.get('choice')}: ')
                    
                if userAnswer.lower() == choice.get('answer'):
                    print(f'{self.MAGENTA}Respuesta Correcta!, +1 punto{self.RESET}')
                    self.points += 1
                else:
                    self.attempts += 1
                    if self.points > 0:
                        self.points -= 1 
                    print(f'{self.RED}Respuesta Incorrecta! -1 punto{self.RESET}')
                    print(f'{self.RED}Intentos Restantes: {self.maxAttempts - self.attempts}{self.RESET}')
                        
                pases += 1
    def game_over(self, message):
        return  print(message, self.show_points())
    def show_points(self):
        return f"{self.BG_BLUE}Cantidad total de puntos: {self.points}{self.RESET}"
    
GameCountry().Start() 