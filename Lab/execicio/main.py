from professor import Professor
from aluno import Aluno
from aula import Aula

alunoA = Aluno(
    nome="Carlão do Idea",
    matricula="1554",
    curso="GEC",
    periodo=7
)
alunoB = Aluno(
    nome="Marinoca",
    matricula="190",
    curso="GEC",
    periodo=7
)
alunoC = Aluno(
    nome="Ceci",
    matricula="191",
    curso="GEC",
    periodo=7
)

alunos = [alunoA,alunoB,alunoC]

professor = Professor(
    nome = "Lereut",
    especialidade = "Ser Vagabunda"
)

aula = Aula(assunto="putaria",aluno = alunos,professor = professor)

print(aula.getListaPresenca())
