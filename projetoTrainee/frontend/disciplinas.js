document.addEventListener('DOMContentLoaded', () => {

    const formulario = document.getElementById('form-disciplina');
    const idInput = document.getElementById('disciplina-id');
    const nomeInput = document.getElementById('disciplina-nome');
    const cargaHorariaInput = document.getElementById('disciplina-carga');
    const semestreInput = document.getElementById('disciplina-semestre');
    const seletorCurso = document.getElementById('disciplina-curso');
    const tituloFormulario = document.getElementById('titulo-formulario');
    const btnSalvar = document.getElementById('btn-salvar');
    const lista = document.getElementById('lista-disciplinas');

    const apiUrlDisciplinas = 'http://127.0.0.1:5000/api/disciplinas';
    const apiUrlCursos = 'http://127.0.0.1:5000/api/cursos';

    async function popularSeletorCursos() {
        try {
            const resposta = await fetch(apiUrlCursos);
            if (!resposta.ok) throw new Error('Falha ao carregar cursos.');
            const cursos = await resposta.json();
            
            seletorCurso.innerHTML = '<option value=""> Selecione o Curso </option>';
            cursos.forEach(curso => {
                const opcao = document.createElement('option');
                opcao.value = curso.id;
                opcao.textContent = `${curso.nome} (${curso.universidade_nome})`;
                seletorCurso.appendChild(opcao);
            });
        } catch (erro) {
            console.error(erro);
        }
    }
    
    async function buscarDisciplinas() {
        try {
            const resposta = await fetch(apiUrlDisciplinas);
            if (!resposta.ok) throw new Error('Erro ao buscar disciplinas');
            const disciplinas = await resposta.json();
            
            lista.innerHTML = '';
            disciplinas.forEach(disciplina => {
                const linha = document.createElement('tr');
                linha.innerHTML = `
                    <td>${disciplina.nome}</td>
                    <td>${disciplina.carga_horaria}h</td>
                    <td>${disciplina.curso_nome}</td>
                    <td>${disciplina.semestre}</td>
                    <td>
                        <button class="btn-editar" data-id="${disciplina.id}">Editar</button>
                        <button class="btn-excluir" data-id="${disciplina.id}">Excluir</button>
                    </td>
                `;
                lista.appendChild(linha);
            });
        } catch (erro) {
            console.error('Falha ao buscar disciplinas:', erro);
        }
    }

    async function salvarDisciplina(evento) {
        evento.preventDefault();
        const id = idInput.value;
        if (!seletorCurso.value) {
            alert('Por favor, selecione um curso.');
            return;
        }
        const dados = {
            nome: nomeInput.value,
            carga_horaria: parseInt(cargaHorariaInput.value),
            semestre: semestreInput.value,
            curso_id: parseInt(seletorCurso.value)
        };

        const ehEdicao = id !== '';
        const metodo = ehEdicao ? 'PUT' : 'POST';
        const url = ehEdicao ? `${apiUrlDisciplinas}/${id}` : apiUrlDisciplinas;

        try {
            const resposta = await fetch(url, {
                method: metodo,
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(dados)
            });
            if (!resposta.ok) throw new Error('Erro ao salvar disciplina');
            resetarFormulario();
            buscarDisciplinas();
        } catch (erro) {
            console.error('Falha ao salvar disciplina:', erro);
        }
    }
    
    async function prepararEdicao(id) {
        try {
            const resposta = await fetch(`${apiUrlDisciplinas}/${id}`); // Back-end precisa ter GET /api/disciplinas/<id>
            if (!resposta.ok) throw new Error('Falha ao buscar dados da disciplina.');
            const disciplina = await resposta.json();
            
            idInput.value = disciplina.id;
            nomeInput.value = disciplina.nome;
            cargaHorariaInput.value = disciplina.carga_horaria;
            semestreInput.value = disciplina.semestre;
            seletorCurso.value = disciplina.curso_id;

            tituloFormulario.textContent = 'Editando Disciplina';
            btnSalvar.textContent = 'Salvar Alterações';
        } catch (erro) {
            console.error('Erro ao preparar edição:', erro);
        }
    }

    async function excluirDisciplina(id) {
        if (!confirm('Tem certeza que deseja excluir esta disciplina?')) return;
        try {
            const resposta = await fetch(`${apiUrlDisciplinas}/${id}`, { method: 'DELETE' });
            if (!resposta.ok) throw new Error('Erro ao excluir disciplina.');
            buscarDisciplinas();
        } catch (erro) {
            console.error('Falha ao excluir disciplina:', erro);
        }
    }
    
    function resetarFormulario() {
        formulario.reset();
        idInput.value = '';
        tituloFormulario.textContent = 'Cadastrar Disciplina';
        btnSalvar.textContent = 'Salvar Disciplina';
    }

    formulario.addEventListener('submit', salvarDisciplina);
    lista.addEventListener('click', (evento) => {
        if (evento.target.classList.contains('btn-editar')) prepararEdicao(evento.target.dataset.id);
        if (evento.target.classList.contains('btn-excluir')) excluirDisciplina(evento.target.dataset.id);
    });
    
    popularSeletorCursos();
    buscarDisciplinas();
});