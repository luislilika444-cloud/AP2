def verificar_assento(numero_assento):
  return True


def reservar_assento(numero_assento):
  return "Assento reservado"


def confirmar_reserva(numero_assento):
  if verificar_assento(numero_assento):
    return reservar_assento(numero_assento)
  else:
    return "Assento indisponível"