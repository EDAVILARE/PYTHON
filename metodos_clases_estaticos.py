#metodos _ clases _ estaticos
class pastel:
    def __init__(self, ingredientes, ):
        self.ingredientes = ingredientes

    def __repr__(self):
        return f'Pastel con ingredientes: ({self.ingredientes !r})'

    @classmethod
    def pastel_chocolate(cls):
        return cls(['Harina','leche','chocolate', 'dulce', 'azúcar'])

    @classmethod
    def pastel_vainilla(cls):
        return cls(['Harina','leche','vainilla', 'dulce', 'azúcar'])

print(pastel.pastel_chocolate())
print(pastel.pastel_vainilla())


















