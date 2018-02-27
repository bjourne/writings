def configure(ctx):
    ctx.load('tex')
    ctx.env.append_unique('PDFLATEXFLAGS', ['-shell-escape'])

def build(ctx):
    ctx(features = 'tex',
        source = 'mlexercises/mlexercises.tex',
        outs = 'pdf')
