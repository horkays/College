from factordb.factordb import FactorDB

f = FactorDB(510143758735509025530880200653196460532653147)
f.connect()
print(min(f.get_factor_list()))