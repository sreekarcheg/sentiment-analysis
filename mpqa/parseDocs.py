
from __future__ import print_function
import pandas as pd
import mpqa

df = pd.DataFrame(columns=mpqa.FEAT_COLS)
for path, fname, topic in mpqa.iter_docs('doclist.combinedUnique'):
    print(path, fname)
    doc = mpqa.Doc(
            mpqa_dir='database.mpqa.2.0',
            path=path,
            fname=fname,
            topic=topic,
            sc_path='subjclues.tff',
            int_path='intensifiers.tff')
    df = df.append(doc.feat_df)

sparse_cols = ['word', 'before', 'after']
pack_cols = mpqa.pack_df(df, sparse_cols)
for c in sparse_cols:
    df['p' + c] = pack_cols[c]

