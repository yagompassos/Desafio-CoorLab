# Resultado - Desáfio CoorLab

## Desenvolvimento
Achei muito legal o projeto proposto demandar um serviço completo com backend e front end, mesmo que tenha sido muito desafiador.

Começei me atentando à ambientação, atualizando minha máquina, também linux, para tera as mesmas dependências descritas no README. Depois comecei a instalar as outras dependências e deixar tudo certinho pra rodar no script bash. 

Comecei a criar a tela inicial do Vue, e uma vez que já tinha algo, parti pra criar um endpoint que retornaria as cidades, pra poder colocar no drop-down de seleção. No python, peguei essa arquitetura no projeto de uma amiga, colega de trabalho que me indicou um projeto parecido que ela já havia feito. Tentei rodar o servidor em flask, mas troquei depois pra fastAPI e atualizei o script BASH. 

Consumir a api no front foi bem tranquilo, depois dei uma estilizada pra deixar o layout parecido com o protótipo e então parti para o segundo endpoint, que retornaria as melhores opções de viagem. Pra essa função, chamei outra função que fazia a comparação dos voos, e adicionei ela em services.py. Pra linkar no front foi um pouco mais trabalhoso, porém também muito tranquilo. 

Agora só restava estilizar o layout, fazer o result.md e enviar.

## Dificuldades
Embora a parte do backend tenha sido tranquila, deixei o front para o final e tive dificuldades para implementar algumas funcionalidades.

Pelo motivo do meu aniversário ser na segunda feira, um dia depois da data de entrega do desafio, tive um final de semana bem corrido e mal consegui mexer no projeto, então:
Primeiro a tela de modal, que não estava aparecendo de forma alguma, optei por deixar o alert do javascript mesmo, pois não tive tempo de debugar esse outro component ModalAlert que tentei criar. Já na parte de inserir a data, tentei utilizar o date-picker do próprio vue, mas estava tendo problemas com a instalação, o vue não estava reconhecendo o caminho de instalaçao isso estava afetando o mount de todo o component CalculatorSection, por isso, optei por tirá-lo, já que o mesmo não tinha impacto nenhum nos dados mostrados na tela, até por que nem tinham datas na base de dados.

Pela falta de tempo, também deixei os ícones pra trás, e não os incluí na versão final.

## Conclusão

Todavia, foi bem legal participar, achei desafiador e foi um projeto que, nesse nível de abrangência de demandas pedidas (setup de ambiente com o script, backend e front end juntos), nunca tinha desenvolvido **sozinho** algo nesse nível. Mesmo que não resulte em nada no PS, com certeza vou pegar uma semaninha pra tentar polir esse projeto e deixá-lo no padrão do protótipo proposto.

## Atualização (04/03/2024)

Como descrito antes, não fui capaz de entregar o projeto completo no prazo que a Coorlab pediu, mas a partir do dia 03/04/2024, voltei a mexer no projeto para tentar enxugá-lo e terminá-lo de acordo com os requisitos pedidos no [README](./README.md). 

Foi bem mais tranquilo resolver os problemas agora que não estava atribulado, comecei corrigindo o layout das opções de voo, adicionando os ícones e tentando deixar tudo igual ao protótipo fornecido. 

Logo após que eu terminei isso, tentei novamente instalar os datepickers do vue, mas novamente por causa de documentação desatualizada tive problemas na implementação. Utilizei o input type date do html e funcionou perfeitamente pro que o projeto pedia.

Então, para finalizar, fui consertar o modal. Com mais tempo, pude debugar o código e entender por que ele estava bugando a renderização da página, consegui corrigir bem rapidamente e isso concluiu o projeto, que agora está conforme o que foi proposto.
