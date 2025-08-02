document.addEventListener('DOMContentLoaded', () => {
    // Referências aos elementos do DOM
    const form = document.getElementById('curso-form');
    const formTitle = document.getElementById('form-title');
    const cursoList = document.getElementById('curso-list');
    const cursoIdInput = document.getElementById('curso-id');
    const btnSubmit = document.getElementById('btn-submit');
    const feedbackMessage = document.getElementById('mensagem-feedback');

    const apiUrl = 'http://127.0.0.1:5000/api/cursos';

    // --- READ: Função para buscar e renderizar os cursos da API ---
    const fetchCursos = async () => {
        try {
            const response = await fetch(apiUrl);
            if (!response.ok) {
                throw new Error('Falha ao buscar cursos.');
            }
            const cursos = await response.json();
            
            cursoList.innerHTML = ''; // Limpa a lista antes de renderizar
            cursos.forEach(curso => {
                const tr = document.createElement('tr');
                tr.innerHTML = `
                    <td>${curso.nome}</td>
                    <td>${curso.nivel}</td>
                    <td>${curso.duracao} anos</td>
                    <td>${curso.vagas}</td>
                    <td>${curso.carga_horaria}h</td>
                    <td>
                        <button class="btn-acao btn-editar" data-id="${curso.id}">Editar</button>
                        <button class="btn-acao btn-excluir" data-id="${curso.id}">Excluir</button>
                    </td>
                `;
                cursoList.appendChild(tr);
            });
        } catch (error) {
            console.error('Erro:', error);
            showFeedback('Não foi possível carregar os cursos. Verifique se o servidor backend está rodando.', 'red');
        }
    };

    // --- CREATE / UPDATE: Lógica do formulário ---
    form.addEventListener('submit', async (event) => {
        event.preventDefault();

        const id = cursoIdInput.value;
        const nome = document.getElementById('nome-curso').value;
        const nivel = document.getElementById('nivel-curso').value;
        const duracao = document.getElementById('duracao-anos').value;
        const vagas = document.getElementById('quantidade-vagas').value;
        const carga_horaria = document.getElementById('carga-horaria').value;

        const cursoData = { 
            nome, 
            nivel, 
            duracao: parseInt(duracao), 
            vagas: parseInt(vagas), 
            carga_horaria: parseInt(carga_horaria)
        };

        try {
            if (id) {
                // --- UPDATE ---
                const response = await fetch(`${apiUrl}/${id}`, { 
                    method: 'PUT', 
                    headers: { 'Content-Type': 'application/json' }, 
                    body: JSON.stringify(cursoData) 
                });
                if (!response.ok) throw new Error('Falha ao atualizar o curso.');
                showFeedback(`Curso "${nome}" atualizado com sucesso!`, 'green');
            } else {
                // --- CREATE ---
                const response = await fetch(apiUrl, { 
                    method: 'POST', 
                    headers: { 'Content-Type': 'application/json' }, 
                    body: JSON.stringify(cursoData) 
                });
                if (!response.ok) throw new Error('Falha ao cadastrar o curso.');
                showFeedback(`Curso "${nome}" cadastrado com sucesso!`, 'green');
            }
        } catch (error) {
            console.error('Erro:', error);
            showFeedback(error.message, 'red');
        }

        resetForm();
        fetchCursos(); // Recarrega a lista após criar ou atualizar
    });

    // --- Lógica para os botões de EDITAR e EXCLUIR ---
    cursoList.addEventListener('click', async (event) => {
        const target = event.target;
        const id = target.getAttribute('data-id');

        if (target.classList.contains('btn-excluir')) {
            // --- DELETE ---
            if (confirm('Tem certeza que deseja excluir este curso?')) {
                try {
                    const response = await fetch(`${apiUrl}/${id}`, { method: 'DELETE' });
                    if (!response.ok) throw new Error('Falha ao excluir o curso.');
                    showFeedback(`Curso excluído com sucesso!`, 'red');
                    fetchCursos(); // Recarrega a lista
                } catch (error) {
                    console.error('Erro:', error);
                    showFeedback(error.message, 'red');
                }
            }
        } else if (target.classList.contains('btn-editar')) {
            // --- Prepara para UPDATE ---
            const row = target.closest('tr');
            const nome = row.cells[0].textContent;
            const nivel = row.cells[1].textContent;
            const duracao = parseInt(row.cells[2].textContent); 
            const vagas = parseInt(row.cells[3].textContent);
            const cargaHoraria = parseInt(row.cells[4].textContent);
            
            // Preenche o formulário com os dados do curso
            cursoIdInput.value = id;
            document.getElementById('nome-curso').value = nome;
            document.getElementById('nivel-curso').value = nivel;
            document.getElementById('duracao-anos').value = duracao;
            document.getElementById('quantidade-vagas').value = vagas;
            document.getElementById('carga-horaria').value = cargaHoraria;
            
            // Muda a aparência do formulário para o modo de edição
            formTitle.textContent = 'Editando Curso';
            btnSubmit.textContent = 'Salvar Alterações';
            window.scrollTo(0, 0); // Rola a página para o topo
        }
    });

    const resetForm = () => {
        form.reset();
        cursoIdInput.value = '';
        formTitle.textContent = 'Cadastrar Novo Curso';
        btnSubmit.textContent = 'Salvar Curso';
    };

    const showFeedback = (message, color) => {
        feedbackMessage.textContent = message;
        feedbackMessage.style.color = color;
        setTimeout(() => { feedbackMessage.textContent = ''; }, 3000);
    };

    // Carrega a lista de cursos quando a página é aberta
    fetchCursos();
});