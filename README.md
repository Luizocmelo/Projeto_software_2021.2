# Disciplina: Projeto de Software - Prof: Baldoino Fonseca

### Sistema de Folha de Pagamento Empresarial

O projeto é implementar um sistema de folha de pagamento. O sistema consiste no
gerenciamento de pagamentos dos empregados de uma empresa fictícia.

Algumas definições com relação ao funcionamento:

• Alguns empregados são horistas. Eles recebem um salário por hora trabalhada. Eles
submetem "cartões de ponto" todo dia para informar o número de horas trabalhadas naquele dia. Se um empregado trabalhar mais do que 8 horas, deve receber 1.5 a taxa normal Durante as horas extras. Eles são pagos toda sexta-feira.

• Alguns empregados recebem um salário fixo mensal. São pagos no último dia útil do mês. São chamados de "assalariados".

• Alguns empregados assalariados são comissionados e portanto recebem uma comissão, um
percentual das vendas que realizam. Eles submetem resultados de vendas que informam a data e valor da venda. O percentual de comissão varia de empregado para empregado. Eles são pagos a cada 2 sextas-feiras; neste momento, devem receber o equivalente de 2 semanas de salário fixo mais as comissões do período.

• O empregados que informa o método de pagamento:
Podem receber um cheque pelos correios ou um cheque em mãos ou depósito em conta bancária

• Alguns empregados pertencem ao sindicato:
O sindicato cobra uma taxa mensal do empregado e essa taxa pode variar entre
empregados, é deduzida do salário. Também, o sindicato pode ocasionalmente 
cobrar taxas de serviços adicionais a um empregado. A identificação do empregado no sindicato não é a mesma da
identificação no sistema de folha de pagamento.

• A folha de pagamento é rodada todo dia e deve pagar os empregados cujos salários vencem naquele dia. 
O sistema receberá a data até a qual o pagamento deve ser feito e calculará o pagamento para cada empregado desde a última vez em que este foi pago.

  
