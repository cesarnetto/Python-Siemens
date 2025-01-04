import snap7
from snap7.util import get_int, set_int

# Configurações do PLC
PLC_IP = '192.168.0.1'  # Endereço IP do PLC
RACK = 0                # Rack do PLC
SLOT = 1                # Slot do PLC

# Conectar ao PLC
client = snap7.client.Client()
client.connect(PLC_IP, RACK, SLOT)

if client.get_connected():
    print("Conexão bem-sucedida com o PLC!")

    #Ler dados de um bloco de dados (DB)
    db_namber = 3           # Número do bloco de dados (DB)
    start_address = 0       # Endereço inicial
    size = 2                # Tamanho em bytes

    data = client.db_read(db_namber, start_address, size)
    valor = get_int(data, 0) # Ler um inteiro a partir do byte 0
    print(f"Valor lido: {valor}")

    #Escrever dados no bloco de dados
    new_data = bytearray(size)
    set_int(new_data, 0, 1234)  # Escreve o valor 1234 no byte 0
    client.db_write(db_namber, start_address, new_data)
    print("Dados escritos com sucesso!")
else:
    print("Falha ao conectar com o PLC.")

# Fechar conexão
client.disconnect()

