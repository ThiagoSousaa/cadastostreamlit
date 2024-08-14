import streamlit as st

# CRIANDO MENU INICIAL

st.title('CADASTRO DE CLIENTES')
name_cte = st.text_input('Digite o nome completo do aluno: ')
endereco_cte = st.text_input('Digite o endereço do aluno: ')
data_cte = st.date_input('Informe a data de nascimento do aluno: ')

# CRIANDO INTERFACE \ TIPO CLIENTE

tipo_cliente = st.selectbox('Tipo de cliente',
                            ['Pessoa física', 'Pessoa jurídica'])
 
cadastrar = st.button('Cadastrar cliente')

if cadastrar:
    with open('clientes.csv', 'a', encoding='utf8') as arquivo:
        arquivo.write(f'{name_cte}, {endereco_cte}, {data_cte}\n')
        st.success('Cliente cadastrado com sucesso :)')



