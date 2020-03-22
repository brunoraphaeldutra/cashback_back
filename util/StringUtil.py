class StringUtil:

    @staticmethod
    def get_cpf(cpf):
        return ''.join(filter(str.isdigit, cpf))
