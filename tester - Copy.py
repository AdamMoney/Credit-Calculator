def generate(self):
        args=[
            '--type=annuity',
            '--payment=8722',
            '--periods=120',
            '--interest=5.6',
        ],
        attach=('principal', 800018, 246622),
        print (args)
        print (attach)
generate(1)
