from professor import Professor


class Aula():
    def __init__(self,assunto,aluno,professor):
        self.assunto = assunto
        self.aluno = aluno
        self.professor = professor
    
    def getListaPresenca(self):
        result = f"Aula de {self.assunto} \nProfessor: {self.professor.nome} \nAlunos Presentes"
        for aluno in self.aluno:
            result +=aluno.toString()

        return result