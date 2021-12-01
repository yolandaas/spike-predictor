# Author: Yolanda Shen
# November - December 2021

from water_to_fasta import *
from get_stats import *
from predict_seq import *

f = "test_align"

process_align(f"./fastas/{f}.fasta")
print_tensor("A\n", A_tensor)
print_tensor("C\n", C_tensor)
print_tensor("T\n", T_tensor)
print_tensor("G\n", G_tensor)
print_tensor("Qi\n", Qi_tensor)
print_tensor("Qm\n", Qm_tensor)

A_rate_tensor = calc_tensor_rate(A_tensor)
C_rate_tensor = calc_tensor_rate(C_tensor)
T_rate_tensor = calc_tensor_rate(T_tensor)
G_rate_tensor = calc_tensor_rate(G_tensor)
Qi_rate_tensor = calc_tensor_rate(Qi_tensor)
Qm_rate_tensor = calc_tensor_rate(Qm_tensor)

write_tensor("A_rate", A_rate_tensor)
write_tensor("C_rate", C_rate_tensor)
write_tensor("T_rate", T_rate_tensor)
write_tensor("G_rate", G_rate_tensor)
write_tensor("Qi_rate", Qi_rate_tensor)
write_tensor("Qm_rate", Qm_rate_tensor)