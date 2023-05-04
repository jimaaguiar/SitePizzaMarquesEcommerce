# SitePizzariaEcommerce
O meu projeto baseia-se na implementação de um site com sistema e-commerce, para uma pizzaria (Pizzaria Marquês).


O site é composto por:<br>
•	Registo: No registo é pedido ao utilizador que introduza o username, email, password, confirmação de password, morada e número de telemóvel. Estes campos serão guardados na base de dados, na classe perfil.<br><br>
•	Login: No login através do username e password  o cliente consegue fazer acesso sistema de encomendas, podendo adicionar ao carrinho, remover, e por fim, finalizar o seu pedido.<br><br>
•	Home: A home possui uma galeria de apresentação de promoções/imagens, um mapa com a localização do restaurante, e uma divisão onde há a possibilidade do cliente ser redirecionado para o login, ou caso não tenha conta, para o registo.<br><br>
•	Menu: O menu é um espaço onde são apresentados todos os produtos que podem ser encomendados, com botões que adicionam os produtos ao carrinho e com a possibilidade de aumentar a sua quantidade.<br><br>
•	Sobre nós: Espaço com uma breve descrição sobre o restaurante.<br><br>
•	Checkout: O checkout apresenta duas divisões, uma em que o cliente escolhe qual o método de envio desejado, qual a morada de entrega (possibilitando utilizar a morada do registo ou uma morada diferente). Na segunda divisão, são listados os produtos adicionados ao carrinho com a possibilidade de os remover, um sub-total e o botão para finalizar a encomenda. Após carregar no botão de finalização da encomenda, é mostrado ao cliente a confirmação do pedido com os respetivos dados.<br><br>
•	Perfil: Espaço onde o cliente pode visualizar os seus dados  de registo.<br><br>


A nível do Design em Css, utilizamos o Boostrap para facilitar a estruturação do site e ter uma implementação responsiva.<br>
A galeria utilizada na home foi retirada de:
https://getbootstrap.com/docs/4.0/components/carousel/ <br>
O mapa da localização foi retirado de:
https://developers.google.com/maps/documentation/javascript/adding-a-google-map#all<br>
 Para o back-end:<br>
Utilizamos a documentação do django, bootstrap, w3schools e Youtube. Para os forms de login utilizamos uma app chamada crispy-forms:
https://django-crispy-forms.readthedocs.io/en/latest/install.html<br>
instalar: pip install django-crispy-forms
