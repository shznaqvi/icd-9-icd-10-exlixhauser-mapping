from hcuppy.elixhauser_v19 import ElixhauserEngineV19

# ee = ElixhauserEngine()
ee = ElixhauserEngineV19()
dx_full_lst = ["V1201"]
dx_poa_lst = ["E119", "B190"]
out = ee.get_elixhauser(dx_full_lst)
print(out)
# {'cmrbdt_lst': ['WGHTLOSS', 'DIAB_UNCX', 'LIVER_SEV'],
#  'mrtlt_scr': 31,
#  'rdmsn_scr': 16}
