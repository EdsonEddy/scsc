code_a = """
n=int(input())
def np(n):# np numero primo
    for j in range(2,int(n**(1/2))+1):
        if n%j==0 and n!=j:
            return False
    return True
for p in range(n):
    s = int(input())
    pw = False
    for j in range(1000):
        h = s * (2 ** j) + 1
        if np(h):
            print(h)
            pw = True
            break
    if pw == False:
        print('-1')
"""
code_b = """
def primo(n):
    for i in range(2,int(n**(1/2))+1):
        if n%i==0 and n!=i:
            return False
            break
    return True

n=int(input())
for i in range(n):
    k=int(input())
    sw=False
    for j in range(1000):
        m=k*(2**j)+1
        if primo(m):
            print(m)
            sw=True
            break
    if sw==False:
        print('-1')
"""

from scsc import Compare

similarity_index = Compare(code_a, code_b, method="ted")
print(f"Similarity Index (ted): {similarity_index}")

similarity_index = Compare(code_a, code_b, method="mdiff")
print(f"Similarity Index (mdiff): {similarity_index}")

similarity_index = Compare(code_a, code_b, method="trs")
print(f"Similarity Index (trs): {similarity_index}")

similarity_index = Compare(code_a, code_b, method="csim")
print(f"Similarity Index (csim): {similarity_index}")

similarity_index = Compare(code_a, code_b, method="gst")
print(f"Similarity Index (gst): {similarity_index}")

similarity_index = Compare(code_a, code_b, method="lf")
print(f"Similarity Index (lf): {similarity_index}")