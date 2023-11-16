import json

DATABASE_FILE = 'database.json'

def load_database():
	try:
		with open(DATABASE_FILE, 'r') as f:
			return json.load(f)
	except FileNotFoundError:
		return {"machine": {}, "ordens_servico": {}}

def save_database(database):
	with open(DATABASE_FILE, 'w') as f:
		json.dump(database, f, indent=4)

def main_menu(database):
	while True:
		print("\nMenu Principal:")
		print("1 - Gerenciar Máquinas")
		print("2 - Gerenciar Ordens de Serviço")
		print("3 - Visualizar Estado das Máquinas")
		print("4 - Visualizar Ordens de Serviço")
		print("5 - Sair")
		choice = input("Escolha uma opção: ")

		if choice == '1':
			manage_machines(database)
		elif choice == '2':
			manage_service_orders(database)
		elif choice == '3':
			view_state_machines(database)
		elif choice == '4':
			view_service_orders(database)
		elif choice == '5':
			print("Saindo do programa...")
			break
		else:
			print("Opção inválida! Tente novamente.")

def manage_machines(database):
	while True:
		print("\nGerenciamento de Máquinas:")
		print("1 - Listar Máquinas")
		print("2 - Adicionar Máquina")
		print("3 - Remover Máquina")
		print("4 - Voltar ao Menu Principal")
		choice = input("Escolha uma opção: ")

		if choice == '1':
			list_machines(database)
		elif choice == '2':
			name = input("Qual nome da maquina: ")
			add_machine(database, name)
			pass
		elif choice == '3':
			machine_id = input("Digite o ID da máquina a ser removida: ")
			if delete_machine(database, machine_id):
				print(f"Máquina com ID {machine_id} removida com sucesso.")
			else:
				print(f"Máquina com ID {machine_id} não encontrada.")
		elif choice == '4':
			break
		else:
			print("Opção inválida! Tente novamente.")

def list_machines(database):
	print(database)
	if not database['machine']:
		print("Ainda não há maquinas no banco de dados")
		return
	for id, machine in database['machine'].items():
		print(f"Maquina {id}: {machine['name']} - Estado: {machine['state']}")

def add_machine(database, name, state='Ociosa'):
	machine = database['machine']
	machine_id = str(max([int(x) for x in machine.keys()] + [0]) + 1)
	machine[machine_id] = {'name': name, 'state': state}
	save_database(database)
	return machine_id

def delete_machine(database, machine_id):
	if not database['machine']:
		print("Ainda não há maquinas no banco de dados")
		return
	if machine_id in database['machine']:
		del database['machine'][machine_id]
		save_database(database)
		return True
	return False



database = load_database()
main_menu(database)