

class NoHaySaldoException(Exception):
    pass
class UsuarioDesactivadoException(Exception):
    pass
class EstadoNoExistenteException(Exception):
    pass

PRIMARIO = 'primario'
SECUNDARIO = 'secundario'
UNIVERSITARIO = 'universitario'
JUBILADO = 'jubilado'
DESACTIVADO = "desactivado"
ACTIVADO = "activado"
PRECIO_TICKET = 70

DESCUENTOS = {
    PRIMARIO: 35,
    SECUNDARIO: 42,
    UNIVERSITARIO: 30,
    JUBILADO: 25,
}


class Sube:
    def __init__(self):
        self.saldo = 0
        self.estado = 'activado'
        self.grupo_beneficiario = None

    def obtener_precio_ticket(self):
        if self.grupo_beneficiario == None:
            return PRECIO_TICKET
        elif self.grupo_beneficiario in DESCUENTOS:
            if self.grupo_beneficiario == PRIMARIO:
                return (DESCUENTOS[PRIMARIO])
            elif self.grupo_beneficiario == SECUNDARIO:
                return (DESCUENTOS[SECUNDARIO])
            elif self.grupo_beneficiario == UNIVERSITARIO:
                return (DESCUENTOS[UNIVERSITARIO])
            elif self.grupo_beneficiario == JUBILADO:
                return (DESCUENTOS[JUBILADO])


    def pagar_pasaje(self):
            if self.estado == DESACTIVADO:
                raise UsuarioDesactivadoException()
            elif self.saldo >= self.obtener_precio_ticket():
                if self.grupo_beneficiario == None:
                    self.saldo -= PRECIO_TICKET
                elif self.grupo_beneficiario == PRIMARIO:
                    self.saldo -= DESCUENTOS[PRIMARIO]
                elif self.grupo_beneficiario == SECUNDARIO:
                    self.saldo -= DESCUENTOS[SECUNDARIO]
                elif self.grupo_beneficiario == UNIVERSITARIO:
                    self.saldo -= DESCUENTOS[UNIVERSITARIO]
                elif self.grupo_beneficiario == JUBILADO:
                    self.saldo -= DESCUENTOS[JUBILADO]
            else: 
                raise NoHaySaldoException()

    def cambiar_estado(self, estadoValido):
        if estadoValido == ACTIVADO:
            self.estado = ACTIVADO
        elif estadoValido == DESACTIVADO:
            self.estado = DESACTIVADO
        else: 
            raise EstadoNoExistenteException()

