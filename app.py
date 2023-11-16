import json

DATABASE_FILE = 'database.json'

def load_database():
	try:
		with open(DATABASE_FILE, 'r') as f:
			return json.load(f)
	except FileNotFoundError:
		return {"maquinas": {}, "ordens_servico": {}}

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