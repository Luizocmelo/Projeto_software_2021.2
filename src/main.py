from Company.Company import Company
from Employees.Comissioned import Comissioned
from Employees.Hourly import Hourly
from Employees.Salaried import Salaried
from PayMethods.PayMethod import PayMethod
from Sindicate.Sindicate import Sindicate
import json
import os

datapath = os.path.join("Projeto_software_2020.2", "")

#C:\Users\lala_\Desktop\Projeto_software_2020.2-main

f = open(r'\Users\lala_\Desktop\Projeto_software_2020.2-main\employees.json')
#f = open(r'\Users\lala_\OneDrive\Documentos\PROJETO_SOFTWARE\Projeto_software_2020.2-main\employees.json')
data = json.load(f)

AsaBranca = Company("Asa Branca", "001", "1234-9", "12345-9")

for emp in data:
    AsaBranca.add_employee(emp['nome'], emp['rg'], emp['endereco'], emp['sindMember'], emp['emp_type'],
                                emp['payMethod'], emp['date'], emp['wage'], emp['hour_value'],
                                bankAcc={'bankID':emp['bankID'], 'agency':emp['agency'], 'account':emp['account']})
print(AsaBranca.employeesList)
f.close()

sindicato = Sindicate(25.31)

while(1):
    hour_value, wage = None, None
    print("Escolha uma opção: ")
    print("0 - Opção de exibir detalhes do empregado\n1 - Opção para adicionar empregado\n2 - Opção de remover empregado\n3 - Opção de lançar um Cartão de Ponto\n4 - Opção para lançar um Resultado Venda\n5 - Opção para lançar uma taxa de serviço\n6 - Opção para alterar dados do empregado\n7 - Opção para rodar a folha de pagamento do dia\n8 - Opção da agenda de pagamento\n9 - Opção para criação de agenda de pagamento\n\n10 - Opção Sair\n\n")
    op = int(input("Escolha: "))
    if op == 10:
        break
    elif op == 1:
        name = input("Digite Nome: ")
        rg = input("Digite Rg: ")
        adress = input("Digite Endereço: ")
        sindMember = input("Usuario membro do sindicato? Se sim digite 1, se não 0: ")
        print("Digite o tipo de empregado, opções: \n")
        print("1 - Comissionado\n2 - Horista\n3 - Salariado")
        escolha = int(input("Digite a opção: "))
        if escolha == 1:
            emp_type = "Comissioned"
        elif escolha == 2:
            emp_type = "Hourly"
        else:
            emp_type = "Salaried"
        if emp_type == "Hourly":
            hour_value = float(input("digite o valor da hora de trabalho: "))
        print("Qual o metodo de pagamento, opções: \n")
        print("1 - Crédito em Conta\n2 - Cheque em mãos\n3 - Cheque via correios\n")
        escolha = int(input("Metodo escolhido: "))
        if escolha == 1:
            payMethod = "AccountCredit"
        elif escolha == 2:
            payMethod = "CheckOnHands"
        else:
            payMethod = "DeliveryCheck"
        print("Digete a data do contrato: ")
        date = input("Digite no formato ANO-MES-DIA: ")
        if not hour_value:
            wage = float(input("Digite salário: "))
        print("Digite os dados bancários, informações: ")
        bankID = input("Banco: ")
        agency = input("Agência: ")
        account = input("Conta: ")
        AsaBranca.add_employee(emp_type=emp_type, sindMember=sindMember, date=date, name=name, rg=rg, adress=adress, bankAcc={'bankID':bankID, 'agency':agency, 'account':account}, payMethod=payMethod, wage=wage)
        print(AsaBranca.employeesList)
    elif op == 2:
        id = int(input("Digite o ID do empregado que será removido: "))
        AsaBranca.remove_employee(id)
        print(AsaBranca.employeesList)
    elif op==3:
        id = int(input("Digite o ID do empregado: "))
        date = input("Digite data do ponto: ")
        hours = float(input("Digite horas trabalhadas: "))
        AsaBranca.timeRegister(id, date, hours)
    elif op==4:
        id = int(input("Digite ID do empregado: "))
        date = input("Digite a data da venda: ")
        value = float(input("Digite o valor da venda: "))
        AsaBranca.set_sale_to_employee(id, date, value)
    elif op==5:
        id = int(input("Digite ID do empregado: "))
        tax_value = float(input("Digite o valor da taxa: "))
        sindicato.tax_associator(id, tax_value)
    elif op==6:
        id = int(input("Digite ID do empregado: "))
        print("Escolha o atributo que será alterado, opções: ")
        while(1):
            print("1 - Tipo de empregado\n2 - Nome\n3 - RG\n4 - Endereço\n5 - Dados Bancários\n6 - Método de pagamento\n7 - Salário\n8 - Valor da hora de trabalho\n\n9 - Alterar\n10 - Sair sem alterar")
            emp_type, name, rg, bankID, agency, account, payMethod, new_wage, hour_value = None, None, None, None, None, None, None, None, None
            opcao = int(input())
            if opcao == 1:
                print("Digite o tipo de empregado, opções: \n")
                print("1 - Comissionado\n2 - Horista\n3 - Salariado")
                escolha = int(input("Digite a opção: "))
                if escolha == 1:
                    emp_type = "Comissioned"
                elif escolha == 2:
                    emp_type = "Hourly"
                else:
                    emp_type = "Salaried"
                if emp_type == "Comissioned":
                    hour_value = float(input("Digite o valor da hora de trabalho: "))
            elif opcao == 2:
                name = input("Digite Nome: ")
            elif opcao == 3:
                rg = input("Digite RG: ")
            elif opcao == 4:
                adress = input("Digite Endereço: ")
            elif opcao == 5:
                bankID = input("Digite Banco: ")
                agency = input("Digite Agência: ")
                account = input("Digite Conta: ")
            elif opcao == 6:
                print("Opções:\n1 - Crédito em Conta\n2 - Cheque em mãos\n3 - Cheque via correios\n")
                escolha = int(input("Novo método: "))
                if escolha == 1:
                    payMethod = "AccountCredit"
                elif escolha == 2:
                    payMethod = "CheckOnHands"
                else:
                    payMethod = "DeliveryCheck"
            elif opcao == 7:
                new_wage = float(input("Digite Salário: "))
            elif opcao == 8:
                hour_value = float(input("Digite o valor da hora de trabalho: "))
            elif opcao == 9:
                AsaBranca.change_employee_details(id, emp_t=emp_type, name=name, rg=rg, adress=adress, bankAcc={'bankID':bankID, 'agency':agency, 'account':account}, payMethod=payMethod, wage=new_wage)
                print("Dados alterados com sucesso!\n")
                break
            elif opcao == 10:
                break
    elif op == 7:
        date = input("Digite a data para rodar a folha de pagamento, formato (AAAA-MM-DD): ")
        AsaBranca.pay_employees(date)
    elif op == 8:
        id = int(input("Digite ID do empregado: "))
        AsaBranca.set_employee_pay_date(id)
        print("Data alterada com sucesso!")
    elif op == 9:
        print("informe a quantidade de datas que deseja criar? ")
        i = int(input())
        for c in range(i):
            schedule = []
            t = input("1 - weekly-1\n2 - weekly-2\n3 - Monthly\n0 - Sair")
            if t == 0:
                break
            else:
                if t == 1:
                    prazo = "weekly-1"
                elif t == 2:
                    prazo = "weekly-2"
                else: prazo = "monthly"
                if prazo == "monthly":
                    print("\nCaso o dia seja o último dia útil do mês escreva: 'util'\n")
                    t = input("Dia: ")
                    if t == "util":
                        dia = "$"
                    else:
                        dia = t
                else:
                    t = input("Digite o Dia: ")
                final = prazo+"-"+dia
                #escolha = input("Deseja adicionar data a agenda? 1 - SIM / 2 - NAO: ")
                #if escolha == 1:
                   # schedule.append(final)
        if len(schedule) >= 1:
            AsaBranca.set_new_pay_schedule(schedule)
            print(AsaBranca.pay_schedule)
            print("\n")
    elif op == 0:
        id = int(input("Digite ID do Empregado: "))
        i = AsaBranca.get_employee(id)
        emp = AsaBranca.employeesList[i]
        wage, hour_value = 0, 0
        if isinstance(emp, Hourly):
            emp_t = "Horista"
            hour_value = emp.hour_value
        elif isinstance(emp, Salaried):
            emp_t = "Assalariado"
            wage = emp.wage
        else:
            emp_t = "Comissionado"
            wage = emp.wage
        print("\n\nID:",emp.id,"\nTipo de Empregado:",emp_t, "\nNome:", emp.name,"\nRG:", emp.rg,"\nEndereco", emp.adress,"\nMembro do Sindicato:", emp.sindMember,"\nDados Bancarios:", emp.bankAcc,"\nMetodo de pagemento:", emp.paymentMethod, "\nData de pagemento:", emp.payDate, "\nSalario:", wage, "\nValor da hora de trabalho:", hour_value, "\n\n")
    elif op == 11:
        break

            
            