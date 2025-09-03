document.addEventListener('DOMContentLoaded', () => {

    // Todos os elementos da pagina
    const formulario = document.getElementById('form-universidade');
    const idInput = document.getElementById('universidade-id');
    const nomeInput = document.getElementById('uni-nome');
    const siglaInput = document.getElementById('uni-sigla');
    const dataCriacaoInput = document.getElementById('uni-data-criacao');
    const publicaInput = document.getElementById('uni-publica');
    const tituloFormulario = document.getElementById('titulo-formulario');
    const btnSalvar = document.getElementById('btn-salvar');
    const lista = document.getElementById('lista-universidades');
    
    const apiUrl = 'http://127.0.0.1:5000/api/universidade';

    //Get: Busca todas as universidades na API e as exibe na tabela.
    async function buscarUniversidades() {
        try {
            const resposta = await fetch(apiUrl);
            if (!resposta.ok) throw new Error('Erro ao buscar dados.');
            const universidades = await resposta.json();
            
            lista.innerHTML = ''; 
            
            universidades.forEach(uni => {
                const linha = document.createElement('tr');
                linha.innerHTML = `
                    <td>${uni.id}</td>
                    <td>${uni.nome}</td>
                    <td>${uni.sigla}</td>
                    <td>${new Date(uni.data_criacao).toLocaleDateString()}</td>
                    <td>${uni.publica ? 'Sim' : 'Não'}</td>
                    <td>
                        <button class="btn-editar" data-id="${uni.id}">Editar</button>
                        <button class="btn-excluir" data-id="${uni.id}">Excluir</button>
                    </td>
                `;
                lista.appendChild(linha);
            });
        } catch (erro) {
            console.error('Falha na busca:', erro);
        }
    }

    // Create/Update: salva uma universidade editando ou criando
    async function salvarUniversidade(evento) {
        evento.preventDefault();

        const id = idInput.value;
        const dados = {
            nome: nomeInput.value,
            sigla: siglaInput.value,
            data_criacao: dataCriacaoInput.value,
            publica: publicaInput.value == "1" 
        };

        const ehEdicao = id !== '';
        const metodo = ehEdicao ? 'PUT' : 'POST';
        const url = ehEdicao ? `${apiUrl}/${id}` : apiUrl;

        try {
            const resposta = await fetch(url, {
                method: metodo,
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(dados)
            });

            if (!resposta.ok) throw new Error('Erro ao salvar.');
            
            resetarFormulario();
            buscarUniversidades();

        } catch (erro) {
            console.error('Falha ao salvar:', erro);
        }
    }

    // Update: prepara as informações de uma universidade para editar
    async function prepararEdicao(id) {
        try {
            // Observação: O back-end precisa ter uma rota para buscar um item por ID
            const resposta = await fetch(`${apiUrl}/${id}`);
            if (!resposta.ok) throw new Error('Falha ao buscar dados para edição.');
            
            const uni = await resposta.json();

            idInput.value = uni.id;
            nomeInput.value = uni.nome;
            siglaInput.value = uni.sigla;
            dataCriacaoInput.value = uni.data_criacao.split('T')[0]; 
            publicaInput.value = uni.publica ? "1" : "0";

            tituloFormulario.textContent = 'Editando Universidade';
            btnSalvar.textContent = 'Salvar Alterações';

        } catch (erro) {
            console.error('Erro ao preparar edição:', erro);
        }
    }

    // Delete: exclui a universidade pelo ID
    async function excluirUniversidade(id) {
        if (!confirm('Tem certeza que deseja excluir esta universidade?')) return;

        try {
            const resposta = await fetch(`${apiUrl}/${id}`, { method: 'DELETE' });
            if (!resposta.ok) throw new Error('Erro ao excluir universidade.');
            
            buscarUniversidades();

        } catch (erro) {
            console.error('Falha ao excluir:', erro);
        }
    }
    function resetarFormulario() {
        formulario.reset();
        idInput.value = '';
        tituloFormulario.textContent = 'Cadastrar Universidade';
        btnSalvar.textContent = 'Salvar Universidade';
    }

    formulario.addEventListener('submit', salvarUniversidade);
    
    lista.addEventListener('click', (evento) => {
        if (evento.target.classList.contains('btn-editar')) {
            prepararEdicao(evento.target.dataset.id);
        }
        if (evento.target.classList.contains('btn-excluir')) {
            excluirUniversidade(evento.target.dataset.id);
        }
    });

    buscarUniversidades();
});