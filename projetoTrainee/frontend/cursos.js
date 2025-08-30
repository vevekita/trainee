document.addEventListener('DOMContentLoaded', () => {

    const formulario = document.getElementById('form-curso');
    const idInput = document.getElementById('curso-id');
    const nomeInput = document.getElementById('curso-nome');
    const nivelInput = document.getElementById('curso-nivel');
    const duracaoInput = document.getElementById('curso-duracao');
    const seletorUniversidade = document.getElementById('curso-universidade');
    const tituloFormulario = document.getElementById('titulo-formulario');
    const btnSalvar = document.getElementById('btn-salvar');
    const lista = document.getElementById('lista-cursos');

    const apiUrlCursos = 'http://127.0.0.1:5000/api/cursos';
    const apiUrlUniversidades = 'http://127.0.0.1:5000/api/universidades';

    async function popularSeletorUniversidades() {
        try {
            const resposta = await fetch(apiUrlUniversidades);
            if (!resposta.ok) throw new Error('Falha ao carregar universidades.');
            const universidades = await resposta.json();
            
            seletorUniversidade.innerHTML = '<option value=""> Selecione a Universidade </option>';
            universidades.forEach(uni => {
                const opcao = document.createElement('option');
                opcao.value = uni.id;
                opcao.textContent = `${uni.nome} (${uni.sigla})`;
                seletorUniversidade.appendChild(opcao);
            });
        } catch (erro) {
            console.error(erro);
        }
    }
    
    async function buscarCursos() {
        try {
            const resposta = await fetch(apiUrlCursos);
            if (!resposta.ok) throw new Error('Erro ao buscar cursos');
            const cursos = await resposta.json();
            
            lista.innerHTML = '';
            cursos.forEach(curso => {
                const linha = document.createElement('tr');
                linha.innerHTML = `
                    <td>${curso.nome}</td>
                    <td>${curso.nivel}</td>
                    <td>${curso.universidade_nome}</td>
                    <td>${curso.duracao} anos</td>
                    <td>
                        <button class="btn-editar" data-id="${curso.id}">Editar</button>
                        <button class="btn-excluir" data-id="${curso.id}">Excluir</button>
                    </td>
                `;
                lista.appendChild(linha);
            });
        } catch (erro) {
            console.error('Falha ao buscar cursos:', erro);
        }
    }

    async function salvarCurso(evento) {
        evento.preventDefault();
        const id = idInput.value;
        if (!seletorUniversidade.value) {
            alert('Por favor, selecione uma universidade.');
            return;
        }
        const dados = {
            nome: nomeInput.value,
            nivel: nivelInput.value,
            duracao: parseInt(duracaoInput.value),
            universidade_id: parseInt(seletorUniversidade.value)
        };

        const ehEdicao = id !== '';
        const metodo = ehEdicao ? 'PUT' : 'POST';
        const url = ehEdicao ? `${apiUrlCursos}/${id}` : apiUrlCursos;

        try {
            const resposta = await fetch(url, {
                method: metodo,
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(dados)
            });
            if (!resposta.ok) throw new Error('Erro ao salvar curso');
            resetarFormulario();
            buscarCursos();
        } catch (erro) {
            console.error('Falha ao salvar curso:', erro);
        }
    }

    async function prepararEdicao(id) {
        try {
            const resposta = await fetch(`${apiUrlCursos}/${id}`); // Back-end precisa ter GET /api/cursos/<id>
            if (!resposta.ok) throw new Error('Falha ao buscar dados do curso.');
            const curso = await resposta.json();
            
            idInput.value = curso.id;
            nomeInput.value = curso.nome;
            nivelInput.value = curso.nivel;
            duracaoInput.value = curso.duracao;
            seletorUniversidade.value = curso.universidade_id; 

            tituloFormulario.textContent = 'Editando Curso';
            btnSalvar.textContent = 'Salvar Alterações';
        } catch (erro) {
            console.error('Erro ao preparar edição:', erro);
        }
    }

    async function excluirCurso(id) {
        if (!confirm('Tem certeza que deseja excluir este curso?')) return;
        try {
            const resposta = await fetch(`${apiUrlCursos}/${id}`, { method: 'DELETE' });
            if (!resposta.ok) throw new Error('Erro ao excluir curso.');
            buscarCursos();
        } catch (erro) {
            console.error('Falha ao excluir curso:', erro);
        }
    }
    
    function resetarFormulario() {
        formulario.reset();
        idInput.value = '';
        tituloFormulario.textContent = 'Cadastrar Curso';
        btnSalvar.textContent = 'Salvar Curso';
    }

    formulario.addEventListener('submit', salvarCurso);
    lista.addEventListener('click', (evento) => {
        if (evento.target.classList.contains('btn-editar')) prepararEdicao(evento.target.dataset.id);
        if (evento.target.classList.contains('btn-excluir')) excluirCurso(evento.target.dataset.id);
    });
    
    popularSeletorUniversidades();
    buscarCursos();
});